# Hosting RCM Newsletter on GitHub Pages

## Setup Steps

### 1. Initialize Git Repository (if not already done)
```bash
cd "c:/Users/shanm/OneDrive/Desktop/RCM newsletter blog"
git init
git add .
git commit -m "Initial commit - RCM Newsletter"
```

### 2. Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `rcm-newsletter` (or your preferred name)
3. Keep it Public (required for free GitHub Pages)
4. Don't initialize with README (we already have files)
5. Click "Create repository"

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/rcm-newsletter.git
git branch -M main
git push -u origin main
```

### 4. Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" → "Pages" (left sidebar)
3. Source: Deploy from a branch
4. Branch: `main` → `/` (root)
5. Click "Save"

### 5. Your Newsletter is Live!
Your site will be available at:
```
https://YOUR_USERNAME.github.io/rcm-newsletter/
```

Individual newsletters:
```
https://YOUR_USERNAME.github.io/rcm-newsletter/RCM_Weekly_Newsletter_2026-02-23.html
```

## Create an Index Page

Create `index.html` to list all newsletters:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RCM Pulse Weekly - Newsletter Archive</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2563eb;
            --primary-dark: #1e40af;
            --text: #1f2937;
            --text-muted: #6b7280;
            --border: #e5e7eb;
            --bg: #f9fafb;
        }
        body {
            font-family: 'Inter', sans-serif;
            max-width: 720px;
            margin: 0 auto;
            padding: 40px 20px;
            background: var(--bg);
            color: var(--text);
        }
        h1 {
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            margin-bottom: 12px;
            color: var(--text);
        }
        .subtitle {
            color: var(--text-muted);
            font-size: 18px;
            margin-bottom: 40px;
        }
        .newsletter-list {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .newsletter-item {
            padding: 16px;
            border-bottom: 1px solid var(--border);
        }
        .newsletter-item:last-child {
            border-bottom: none;
        }
        .newsletter-item a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            font-size: 18px;
        }
        .newsletter-item a:hover {
            color: var(--primary-dark);
            text-decoration: underline;
        }
        .newsletter-date {
            color: var(--text-muted);
            font-size: 14px;
            margin-top: 4px;
        }
        .newsletter-meta {
            color: var(--text-muted);
            font-size: 14px;
            margin-top: 4px;
        }
    </style>
</head>
<body>
    <h1>RCM Pulse Weekly</h1>
    <p class="subtitle">Revenue Cycle Management insights for medical practices</p>

    <div class="newsletter-list">
        <div class="newsletter-item">
            <a href="RCM_Weekly_Newsletter_2026-02-23.html">Volume 1, Issue 2 - Medicare Advantage Market Disruption</a>
            <div class="newsletter-date">February 23, 2026</div>
        </div>
        <div class="newsletter-item">
            <a href="RCM_Weekly_Newsletter_2026-02-16.html">Volume 1, Issue 1 - Launch Issue</a>
            <div class="newsletter-date">February 16, 2026</div>
        </div>
        <!-- Add new issues here as they're generated -->
    </div>
</body>
</html>
```

## Automated Updates

After each weekly generation:
```bash
git add .
git commit -m "Add newsletter for [date]"
git push
```

GitHub Pages will automatically rebuild (takes 1-2 minutes).

## Custom Domain (Optional)

If you want `newsletter.yourcompany.com`:
1. Buy domain from Namecheap, GoDaddy, etc.
2. Add CNAME file to repository with your domain
3. Configure DNS with your registrar
4. In GitHub Settings → Pages, add custom domain
