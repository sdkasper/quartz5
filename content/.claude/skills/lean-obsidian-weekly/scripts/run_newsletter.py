#!/usr/bin/env python3
"""
Lean Obsidian Weekly Newsletter Orchestration Script

Orchestrates the full newsletter pipeline: CLI data collection, caching, generation, and git ops.
Supports full pipeline (all CLIs + generate + commit) and preview-only modes.

Usage:
    python run_newsletter.py --mode full
    python run_newsletter.py --mode preview
    python run_newsletter.py --mode full --start-date 2026-05-01 --end-date 2026-05-07
    python run_newsletter.py --mode full --skip-commit
    python run_newsletter.py --mode full --output "custom_newsletter.md"
"""

import json
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Any
import argparse


class NewsletterOrchestrator:
    """Orchestrates the full newsletter pipeline."""

    def __init__(
        self,
        mode: str = "preview",
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        skip_commit: bool = False,
        output_file: Optional[str] = None,
    ):
        self.mode = mode
        self.skip_commit = skip_commit
        self.project_root = Path("D:\\GitProjects\\lean-obsidian-weekly")
        self.cache_dir = self.project_root / "cache"
        self.cache_file = self.cache_dir / "latest_research.json"
        self.scripts_dir = self.project_root / "scripts"
        self.newsletter_dir = Path("D:\\Lean Notes\\09 Blog\\Substack")

        # Date range
        if end_date:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        else:
            self.end_date = datetime.now().date()

        if start_date:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        else:
            self.start_date = self.end_date - timedelta(days=7)

        # Output file
        if output_file:
            self.output_file = Path(output_file)
        else:
            week_num = self.end_date.isocalendar()[1]
            self.output_file = (
                self.newsletter_dir / f"Lean Obsidian Weekly {week_num:03d}.md"
            )

        self.errors = []
        self.skipped_sources = []

    def log(self, msg: str, level: str = "INFO"):
        """Log with timestamp."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefix = f"[{ts}] {level:8s}"
        print(f"{prefix} {msg}")

    def error(self, msg: str):
        """Log error and track it."""
        self.log(msg, "ERROR")
        self.errors.append(msg)

    def warn(self, msg: str):
        """Log warning."""
        self.log(msg, "WARN")

    def run_cli_command(
        self, name: str, cmd: List[str], days: int = 7
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Run a CLI command and parse JSON output.

        Args:
            name: Source name (for logging)
            cmd: Command as list (for subprocess)
            days: Days parameter for date-based CLIs

        Returns:
            Parsed JSON lines as list of dicts, or None if failed
        """
        self.log(f"Fetching {name}...")
        try:
            # Change to project root for CLI execution
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                self.error(f"{name} failed: {result.stderr}")
                self.skipped_sources.append(name)
                return None

            # Parse output
            output = result.stdout.strip()
            if not output:
                self.warn(f"{name} returned empty result")
                self.skipped_sources.append(name)
                return None

            # Handle both single JSON objects per line and JSON arrays
            lines = output.split("\n")
            items = []

            for line in lines:
                if line.strip():
                    try:
                        item = json.loads(line)
                        items.append(item)
                    except json.JSONDecodeError:
                        # If single line is array, parse once
                        if "[" in output and "]" in output:
                            items = json.loads(output)
                            break

            self.log(f"  -> Fetched {len(items)} items from {name}")
            return items

        except subprocess.TimeoutExpired:
            self.error(f"{name} timed out (30s)")
            self.skipped_sources.append(name)
            return None
        except Exception as e:
            self.error(f"{name} exception: {e}")
            self.skipped_sources.append(name)
            return None

    def fetch_plugins_new(self, days: int = 7) -> Optional[List[Dict]]:
        """Fetch newly released plugins."""
        cmd = [
            "python",
            "bin/obsidian-community-pp-cli",
            "plugins",
            "new",
            "--days",
            str(days),
            "--min-rating",
            "90",
        ]
        return self.run_cli_command("Plugins (New)", cmd, days)

    def fetch_plugins_updated(self, days: int = 7) -> Optional[List[Dict]]:
        """Fetch recently updated plugins."""
        cmd = [
            "python",
            "bin/obsidian-community-pp-cli",
            "plugins",
            "updated",
            "--days",
            str(days),
            "--min-rating",
            "90",
        ]
        return self.run_cli_command("Plugins (Updated)", cmd, days)

    def fetch_plugins_trending(self) -> Optional[List[Dict]]:
        """Fetch trending plugins (top 3 this week)."""
        cmd = [
            "python",
            "bin/obsidian-community-pp-cli",
            "plugins",
            "trending",
            "--limit",
            "3",
        ]
        return self.run_cli_command("Plugins (Trending)", cmd)

    def fetch_forum_topics(self, days: int = 7) -> Optional[List[Dict]]:
        """Fetch forum topics from Obsidian community."""
        cmd = [
            "python",
            "bin/obsidian-forum-pp-cli",
            "topics",
            "--latest",
            "--days",
            str(days),
            "--sort",
            "views",
            "--limit",
            "5",
        ]
        return self.run_cli_command("Forum Topics", cmd, days)

    def fetch_reddit_posts(self) -> Optional[List[Dict]]:
        """Fetch top Reddit posts from r/ObsidianMD."""
        cmd = [
            "python",
            "bin/scrape-creators-pp-cli",
            "reddit",
            "--subreddit",
            "ObsidianMD",
            "--sort",
            "top",
            "--time",
            "week",
            "--limit",
            "5",
        ]
        return self.run_cli_command("Reddit (r/ObsidianMD)", cmd)

    def fetch_youtube_videos(self) -> Optional[List[Dict]]:
        """Fetch YouTube videos about Obsidian."""
        # Check for API key
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            self.warn(
                "YOUTUBE_API_KEY not set - YouTube videos will be skipped. "
                "Set the env var to include YouTube content."
            )
            self.skipped_sources.append("YouTube")
            return None

        cmd = [
            "python",
            "bin/scrape-creators-pp-cli",
            "youtube",
            "--query",
            "obsidian",
            "--latest",
            "5",
        ]
        return self.run_cli_command("YouTube (Obsidian)", cmd)

    def fetch_bluesky_posts(self, days: int = 7) -> Optional[List[Dict]]:
        """Fetch Bluesky posts about Obsidian."""
        cmd = [
            "python",
            "bin/scrape-creators-pp-cli",
            "bluesky",
            "--query",
            "obsidian.md",
            "--days",
            str(days),
            "--limit",
            "5",
        ]
        return self.run_cli_command("Bluesky (@obsidian.md)", cmd, days)

    def merge_research_data(self, data: Dict[str, Any]) -> None:
        """Merge collected data into cache file."""
        self.log("Merging research data into cache...")

        # Ensure cache dir exists
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Build cache structure
        cache = {
            "week": f"{self.end_date.year}-W{self.end_date.isocalendar()[1]:02d}",
            "generated_at": datetime.now().isoformat() + "Z",
            "date_range": {
                "start": self.start_date.isoformat(),
                "end": self.end_date.isoformat(),
            },
            "newcomers": data.get("plugins_new", []),
            "latest_updates": data.get("plugins_updated", []),
            "most_downloaded": data.get("plugins_trending", []),
            "forum_topics": data.get("forum_topics", []),
            "community_buzz": {
                "reddit": data.get("reddit_posts", []),
                "youtube": data.get("youtube_videos", []),
                "bluesky": data.get("bluesky_posts", []),
            },
            "quick_tips": [
                {
                    "title": "Vim key bindings with Obsidian",
                    "description": "Enable Vim mode in Settings > Editor to use vi/vim shortcuts for navigation and editing.",
                },
                {
                    "title": "Sync backups across devices",
                    "description": "Use Obsidian Sync or Git integration to keep vaults in sync without vendor lock-in.",
                },
                {
                    "title": "Daily notes with templates",
                    "description": "Create a template for daily notes and auto-insert date with the Daily Notes plugin.",
                },
            ],
            "featured_post": {
                "title": "From LeanProductivity",
                "url": "https://blog.sascha-kasper.com",
                "description": "Check the latest from the LeanProductivity blog.",
            },
        }

        # Write cache
        with open(self.cache_file, "w") as f:
            json.dump(cache, f, indent=2, default=str)

        self.log(f"  -> Cache written to {self.cache_file}")

    def generate_newsletter(self) -> Optional[str]:
        """Run newsletter_generator.py and return output."""
        self.log("Generating newsletter from cache...")

        # Ensure output dir exists
        self.newsletter_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            "python",
            str(self.scripts_dir / "newsletter_generator.py"),
            "--input",
            str(self.cache_file),
            "--output",
            str(self.output_file),
            "--dry-run",  # Always dry-run; user decides when to post
        ]

        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode != 0:
                self.error(f"Newsletter generation failed: {result.stderr}")
                return None

            self.log(f"  -> Newsletter generated: {self.output_file}")
            return result.stdout

        except subprocess.TimeoutExpired:
            self.error("Newsletter generation timed out (10s)")
            return None
        except Exception as e:
            self.error(f"Newsletter generation exception: {e}")
            return None

    def validate_output_file(self) -> bool:
        """Verify output file was created."""
        if self.output_file.exists():
            size = self.output_file.stat().st_size
            self.log(f"  -> Output file verified: {size} bytes")
            return True
        else:
            self.error(f"Output file not found: {self.output_file}")
            return False

    def check_git_status(self) -> bool:
        """Check if git working tree is clean."""
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                timeout=5,
            )

            if result.returncode != 0:
                self.error("Git status check failed")
                return False

            if result.stdout.strip():
                self.error(
                    "Git working tree not clean. Stash changes with 'git stash' first."
                )
                return False

            return True

        except Exception as e:
            self.error(f"Git status check exception: {e}")
            return False

    def commit_and_push(self) -> bool:
        """Commit cache and push to origin."""
        self.log("Committing cache to git...")

        # Check clean state
        if not self.check_git_status():
            return False

        try:
            # Add cache file
            subprocess.run(
                ["git", "add", "cache/latest_research.json"],
                cwd=str(self.project_root),
                capture_output=True,
                timeout=5,
                check=True,
            )

            # Commit
            week_num = self.end_date.isocalendar()[1]
            msg = f"chore: newsletter research W{week_num:02d}"
            subprocess.run(
                ["git", "commit", "-m", msg],
                cwd=str(self.project_root),
                capture_output=True,
                timeout=5,
                check=True,
            )

            self.log(f"  -> Committed: {msg}")

            # Push
            subprocess.run(
                ["git", "push", "origin", "master"],
                cwd=str(self.project_root),
                capture_output=True,
                timeout=10,
                check=True,
            )

            self.log("  -> Pushed to origin/master")
            return True

        except subprocess.CalledProcessError as e:
            self.error(f"Git operation failed: {e.stderr}")
            return False
        except Exception as e:
            self.error(f"Git exception: {e}")
            return False

    def show_preview(self, newsletter_text: Optional[str]) -> None:
        """Display newsletter preview."""
        self.log("\n" + "=" * 80)
        self.log("NEWSLETTER PREVIEW", "INFO")
        self.log("=" * 80)

        if self.output_file.exists():
            with open(self.output_file, "r") as f:
                content = f.read()
                print(content)
        else:
            self.warn("Newsletter file not found for preview")

        self.log("=" * 80)

    def run_full_pipeline(self) -> bool:
        """Run complete pipeline: fetch all CLIs, merge, generate, commit, push."""
        self.log(f"Starting FULL PIPELINE (date range: {self.start_date} to {self.end_date})")
        self.log(f"Working directory: {self.project_root}")

        # Calculate days for CLI commands
        days = (self.end_date - self.start_date).days or 7

        # Fetch all data
        data = {}
        data["plugins_new"] = self.fetch_plugins_new(days) or []
        data["plugins_updated"] = self.fetch_plugins_updated(days) or []
        data["plugins_trending"] = self.fetch_plugins_trending() or []
        data["forum_topics"] = self.fetch_forum_topics(days) or []
        data["reddit_posts"] = self.fetch_reddit_posts() or []
        data["youtube_videos"] = self.fetch_youtube_videos() or []
        data["bluesky_posts"] = self.fetch_bluesky_posts(days) or []

        # Merge and generate
        self.merge_research_data(data)
        newsletter_text = self.generate_newsletter()

        if not newsletter_text:
            self.error("Newsletter generation failed, aborting")
            return False

        if not self.validate_output_file():
            self.error("Output file validation failed, aborting commit")
            return False

        # Show preview
        self.show_preview(newsletter_text)

        # Commit and push
        if not self.skip_commit:
            if not self.commit_and_push():
                self.error("Commit/push failed")
                return False
        else:
            self.log("Skipping git operations (--skip-commit)")

        return True

    def run_preview_mode(self) -> bool:
        """Run preview-only: use cached data, generate, show preview."""
        self.log("Starting PREVIEW-ONLY mode")

        if not self.cache_file.exists():
            self.error(f"Cache file not found: {self.cache_file}")
            self.log("Run with --mode full to fetch fresh data")
            return False

        newsletter_text = self.generate_newsletter()

        if not newsletter_text:
            self.error("Newsletter generation failed")
            return False

        if not self.validate_output_file():
            self.error("Output file validation failed")
            return False

        self.show_preview(newsletter_text)
        return True

    def run(self) -> bool:
        """Execute the requested mode."""
        if self.mode == "full":
            return self.run_full_pipeline()
        elif self.mode == "preview":
            return self.run_preview_mode()
        else:
            self.error(f"Unknown mode: {self.mode}")
            return False

    def print_summary(self) -> None:
        """Print execution summary."""
        self.log("\n" + "=" * 80)
        self.log("SUMMARY", "INFO")
        self.log("=" * 80)

        self.log(f"Mode: {self.mode}")
        self.log(f"Date Range: {self.start_date} to {self.end_date}")
        self.log(f"Output File: {self.output_file}")

        if self.skipped_sources:
            self.log(f"Skipped Sources: {', '.join(self.skipped_sources)}")

        if self.errors:
            self.log(f"Errors Encountered: {len(self.errors)}")
            for err in self.errors:
                self.log(f"  - {err}")

        if not self.errors:
            self.log("Status: SUCCESS")
            if self.mode == "full":
                self.log("\nNext Steps:")
                self.log("  1. Review the newsletter preview above")
                self.log("  2. Verify all sections are populated (no empty Newcomers, etc.)")
                self.log("  3. Check 2-3 links are valid URLs")
                if not self.skip_commit:
                    self.log("  4. Cache committed and pushed to origin/master")
                    self.log("  5. Use /substack-publish to post the draft to Substack")
                else:
                    self.log("  4. Use /substack-publish to post the draft to Substack")
        else:
            self.log("Status: FAILED")
            self.log("\nDebug Steps:")
            self.log("  1. Check YOUTUBE_API_KEY is set if videos are needed")
            self.log("  2. Verify network connectivity to CLI sources")
            self.log("  3. Check git working tree is clean (git status)")
            self.log("  4. Review error log above for details")

        self.log("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Lean Obsidian Weekly Newsletter Orchestration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_newsletter.py --mode full
  python run_newsletter.py --mode preview
  python run_newsletter.py --mode full --start-date 2026-05-01 --end-date 2026-05-07
  python run_newsletter.py --mode full --skip-commit
  python run_newsletter.py --mode full --output "custom_name.md"
        """,
    )

    parser.add_argument(
        "--mode",
        choices=["full", "preview"],
        default="preview",
        help="Execution mode: full pipeline or preview-only (default: preview)",
    )
    parser.add_argument(
        "--start-date",
        help="Start date (YYYY-MM-DD, default: 7 days ago)",
    )
    parser.add_argument(
        "--end-date",
        help="End date (YYYY-MM-DD, default: today)",
    )
    parser.add_argument(
        "--skip-commit",
        action="store_true",
        help="Skip git commit and push operations",
    )
    parser.add_argument(
        "--output",
        help="Custom output filename (default: Lean Obsidian Weekly NNN.md)",
    )

    args = parser.parse_args()

    orchestrator = NewsletterOrchestrator(
        mode=args.mode,
        start_date=args.start_date,
        end_date=args.end_date,
        skip_commit=args.skip_commit,
        output_file=args.output,
    )

    success = orchestrator.run()
    orchestrator.print_summary()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
