"""
RCM Newsletter Weekly Generation Script
Runs automatically via Windows Task Scheduler every Friday
"""
import subprocess
import sys
from datetime import datetime
from pathlib import Path

def main():
    """Generate weekly RCM newsletter using Claude Code CLI"""
    project_dir = Path(__file__).parent
    log_file = project_dir / f"newsletter_generation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    print(f"Starting RCM Newsletter generation at {datetime.now()}")
    print(f"Project directory: {project_dir}")
    print(f"Log file: {log_file}")

    # Command to run Claude Code CLI with the newsletter generation prompt
    claude_exe = r"C:\Users\shanm\.local\bin\claude.exe"
    prompt = "Generate the next weekly RCM newsletter following the full workflow"

    try:
        # Run claude in non-interactive print mode (-p) with the project dir as cwd
        result = subprocess.run(
            [claude_exe, "-p", prompt,
             "--allowedTools", "WebSearch,WebFetch,Read,Write,Edit,Bash"],
            capture_output=True,
            text=True,
            cwd=str(project_dir),
            timeout=600  # 10 minute timeout
        )

        # Write output to log file
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"=== RCM Newsletter Generation Log ===\n")
            f.write(f"Started: {datetime.now()}\n")
            f.write(f"\n--- STDOUT ---\n{result.stdout}\n")
            f.write(f"\n--- STDERR ---\n{result.stderr}\n")
            f.write(f"\nReturn code: {result.returncode}\n")

        if result.returncode == 0:
            print("[SUCCESS] Newsletter generated successfully!")
            print(f"Check log: {log_file}")

            # Update index.html with new newsletter
            print("\n[UPDATE] Updating index page...")
            try:
                subprocess.run(["python", "update_index.py"], cwd=project_dir, check=True)
            except subprocess.CalledProcessError as e:
                print(f"[WARNING] Failed to update index: {e}")

            # Auto-publish to GitHub Pages
            print("\n[PUBLISH] Publishing to GitHub Pages...")
            try:
                # Git add new files
                subprocess.run(["git", "add", "."], cwd=project_dir, check=True)

                # Git commit
                commit_msg = f"Add newsletter for {datetime.now().strftime('%Y-%m-%d')}"
                subprocess.run(["git", "commit", "-m", commit_msg], cwd=project_dir, check=True)

                # Git push to publish
                subprocess.run(["git", "push"], cwd=project_dir, check=True)

                print("[SUCCESS] Newsletter published to https://shanmukund.github.io/rcm-newsletter/")
                return 0
            except subprocess.CalledProcessError as e:
                print(f"[WARNING] Failed to publish to GitHub: {e}")
                print("[INFO] Newsletter generated but not published - manual push required")
                return 0  # Still consider it success since newsletter was generated
        else:
            print(f"[ERROR] Generation failed with code {result.returncode}")
            print(f"Check log: {log_file}")
            return result.returncode

    except subprocess.TimeoutExpired:
        print("[ERROR] Newsletter generation timed out after 10 minutes")
        return 1
    except FileNotFoundError:
        print("[ERROR] Claude CLI not found. Please ensure 'claude' is in your PATH")
        return 1
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
