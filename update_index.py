"""
Auto-update index.html with new newsletter entries
Run this after generating each newsletter to update the archive page
"""
import re
from pathlib import Path
from datetime import datetime

def extract_newsletter_info(md_file):
    """Extract title, date, and topics from newsletter markdown"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract volume and issue from first line (e.g., "# Volume 1, Issue 2")
    volume_match = re.search(r'Volume (\d+), Issue (\d+)', content)
    volume = volume_match.group(1) if volume_match else "1"
    issue = volume_match.group(2) if volume_match else "?"

    # Extract first headline as title (after the volume/issue header)
    title_match = re.search(r'\n##\s+(.+)', content)
    title = title_match.group(1) if title_match else "Weekly Newsletter"

    # Extract topics from section headers
    topics = re.findall(r'\n##\s+\d+\.\s+(.+?)(?:\n|$)', content)
    topics_str = " • ".join(topics[:5]) if topics else "RCM updates and insights"

    return {
        'volume': volume,
        'issue': issue,
        'title': title,
        'topics': topics_str
    }

def update_index_html(newsletter_files):
    """Update index.html with newsletter entries"""
    project_dir = Path(__file__).parent
    index_file = project_dir / "index.html"

    # Read current index.html
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build newsletter items HTML
    items_html = []
    for md_file in sorted(newsletter_files, reverse=True):
        # Extract date from filename (RCM_Weekly_Newsletter_2026-02-23.md)
        date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', md_file.name)
        if not date_match:
            continue

        date_str = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")

        # Get newsletter info
        info = extract_newsletter_info(md_file)

        # Build HTML filename
        html_file = md_file.stem + ".html"

        # Create item HTML
        item = f'''            <div class="newsletter-item">
                <a href="{html_file}">{info['title']}</a>
                <div class="newsletter-meta">
                    <span class="newsletter-date">{formatted_date}</span>
                    <span class="newsletter-volume">Volume {info['volume']}, Issue {info['issue']}</span>
                </div>
                <div class="newsletter-topics">
                    {info['topics']}
                </div>
            </div>'''
        items_html.append(item)

    # Join all items
    all_items = "\n\n".join(items_html)

    # Replace the newsletter items section
    pattern = r'(<h2 class="section-title">Latest Issues</h2>\s*)(.*?)(\s*</div>\s*<footer)'
    replacement = r'\1\n\n' + all_items + r'\n        \3'
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Update the stats (issue count)
    issue_count = len(newsletter_files)
    updated_content = re.sub(
        r'<div class="stat-number">\d+</div>\s*<div class="stat-label">Issues</div>',
        f'<div class="stat-number">{issue_count}</div>\n                    <div class="stat-label">Issues</div>',
        updated_content
    )

    # Write updated index.html
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"[SUCCESS] Updated index.html with {issue_count} newsletters")

if __name__ == "__main__":
    project_dir = Path(__file__).parent

    # Find all newsletter markdown files
    newsletter_files = list(project_dir.glob("RCM_Weekly_Newsletter_*.md"))

    if newsletter_files:
        update_index_html(newsletter_files)
    else:
        print("[ERROR] No newsletter files found")
