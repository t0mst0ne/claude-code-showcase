#!/usr/bin/env python3
"""
Heptabase Card Sync — Create cards via Playwright browser automation.

Heptabase has no public write API, so this script uses Playwright with a
persistent browser context to automate card creation in the Card Library.

Usage:
    python scripts/heptabase_sync.py --setup                                 # First-time login
    python scripts/heptabase_sync.py Research/digest/2026-02-07.md           # Headless
    python scripts/heptabase_sync.py somefile.md --title "My Card"           # Custom title
    python scripts/heptabase_sync.py Research/digest/2026-02-07.md --headed  # Visible browser
"""

import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# === Configuration ===
HEPTABASE_URL = "https://app.heptabase.com"
SESSION_DIR = Path.home() / ".heptabase-playwright"
SCREENSHOT_DIR = Path(__file__).parent / "logs"

# Timeouts (ms)
NAV_TIMEOUT = 30_000
ACTION_TIMEOUT = 10_000


def take_screenshot(page, name: str) -> Path:
    """Save a debug screenshot and return its path."""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SCREENSHOT_DIR / f"{name}_{ts}.png"
    page.screenshot(path=str(path), full_page=True)
    return path


def is_logged_in(page) -> bool:
    """Detect whether the user is logged in by checking for app UI elements."""
    # Look for sidebar or workspace indicators that appear after login
    selectors = [
        '[data-testid="sidebar"]',
        'nav',
        '.sidebar',
        'text="Card Library"',
        'text="Whiteboard"',
        'text="Journal"',
    ]
    for sel in selectors:
        try:
            if page.locator(sel).first.is_visible(timeout=2000):
                return True
        except (PlaywrightTimeout, Exception):
            continue
    return False


def wait_for_login(page) -> bool:
    """Wait for the user to log in manually (up to 5 minutes)."""
    print("Waiting for you to log in...")
    print("(You have 5 minutes. The script will continue once it detects the app UI.)")
    deadline = time.time() + 300  # 5 minutes
    while time.time() < deadline:
        if is_logged_in(page):
            print("Login detected!")
            return True
        time.sleep(2)
    print("Timed out waiting for login.")
    return False


def navigate_to_card_library(page) -> bool:
    """Navigate to the Card Library section."""
    # Try clicking Card Library in the sidebar using multiple selectors
    selectors = [
        'text="Card Library"',
        '[aria-label="Card Library"]',
        '[data-testid="card-library"]',
        'a:has-text("Card Library")',
        'div:has-text("Card Library")',
    ]
    for sel in selectors:
        try:
            loc = page.locator(sel).first
            if loc.is_visible(timeout=3000):
                loc.click()
                time.sleep(2)
                return True
        except (PlaywrightTimeout, Exception):
            continue

    # Fallback: try navigating via URL if sidebar click fails
    try:
        page.goto(f"{HEPTABASE_URL}/card-library", timeout=NAV_TIMEOUT)
        time.sleep(2)
        return True
    except Exception:
        pass

    return False


def create_card(page, title: str, content: str) -> bool:
    """Create a new card with the given title and content."""
    # Step 1: Create new card with Cmd+N
    print("  Creating new card (Cmd+N)...")
    page.keyboard.press("Meta+n")
    time.sleep(2)

    # Step 2: Type the title
    print(f"  Typing title: {title}")
    page.keyboard.type(title, delay=30)
    time.sleep(0.5)

    # Step 3: Press Enter to move to the card body
    page.keyboard.press("Enter")
    time.sleep(1)

    # Step 4: Paste content
    # Try clipboard-based paste first, fall back to keyboard.type()
    print("  Pasting content...")
    try:
        page.evaluate(
            "text => navigator.clipboard.writeText(text)",
            content,
        )
        page.keyboard.press("Meta+v")
        time.sleep(2)
    except Exception as e:
        print(f"  Clipboard paste failed ({e}), falling back to keyboard.type()...")
        # type() is slower but more reliable
        page.keyboard.type(content, delay=5)
        time.sleep(1)

    print("  Card created.")
    return True


def run_setup():
    """Interactive setup: open headed browser for manual login."""
    print("=== Heptabase Sync — First-Time Setup ===")
    print(f"Session will be saved to: {SESSION_DIR}")
    SESSION_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(SESSION_DIR),
            channel="chrome",
            headless=False,
            viewport={"width": 1280, "height": 800},
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(HEPTABASE_URL, timeout=NAV_TIMEOUT)

        if is_logged_in(page):
            print("Already logged in! Session is valid.")
        else:
            print("\nPlease log in to Heptabase in the browser window.")
            if not wait_for_login(page):
                print("Setup incomplete — login timed out.")
                context.close()
                return False

        # Give time for session cookies to be fully written
        time.sleep(3)
        print("\nSetup complete! Session saved. You can close the browser.")
        print("The browser will close automatically in 10 seconds...")
        time.sleep(10)
        context.close()

    return True


def extract_title(file_path: Path, content: str) -> str:
    """Extract a card title from the markdown file.

    Priority: YAML frontmatter 'title' > first H1 heading > filename stem.
    """
    # Try YAML frontmatter title
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).splitlines():
            m = re.match(r"^title:\s*(.+)", line)
            if m:
                return m.group(1).strip().strip('"').strip("'")

    # Try first H1 heading
    h1_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()

    # Fallback to filename
    return file_path.stem


def run_sync(file_path: Path, headed: bool = False, title: str | None = None):
    """Sync a markdown file to Heptabase as a new card."""
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return False

    content = file_path.read_text(encoding="utf-8")

    # Determine card title
    if title:
        card_title = title
    else:
        card_title = extract_title(file_path, content)

    if not SESSION_DIR.exists():
        print("Error: No saved session found. Run with --setup first.")
        return False

    print(f"Syncing to Heptabase: {card_title}")
    print(f"  Mode: {'headed' if headed else 'headless'}")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(SESSION_DIR),
            channel="chrome",
            headless=not headed,
            viewport={"width": 1280, "height": 800},
        )
        page = context.pages[0] if context.pages else context.new_page()

        try:
            # Navigate to Heptabase
            print("  Navigating to Heptabase...")
            page.goto(HEPTABASE_URL, timeout=NAV_TIMEOUT)
            time.sleep(3)

            # Check login status
            if not is_logged_in(page):
                print("  Session expired! Relaunching in headed mode for re-login...")
                context.close()
                # Relaunch headed for manual re-login
                context = p.chromium.launch_persistent_context(
                    user_data_dir=str(SESSION_DIR),
                    channel="chrome",
                    headless=False,
                    viewport={"width": 1280, "height": 800},
                )
                page = context.pages[0] if context.pages else context.new_page()
                page.goto(HEPTABASE_URL, timeout=NAV_TIMEOUT)

                if not wait_for_login(page):
                    screenshot = take_screenshot(page, "login_timeout")
                    print(f"  Login timed out. Screenshot: {screenshot}")
                    context.close()
                    return False

                time.sleep(3)

            # Navigate to Card Library
            print("  Opening Card Library...")
            if not navigate_to_card_library(page):
                screenshot = take_screenshot(page, "card_library_nav_failed")
                print(f"  Could not navigate to Card Library. Screenshot: {screenshot}")
                context.close()
                return False

            # Create the card
            if not create_card(page, card_title, content):
                screenshot = take_screenshot(page, "card_creation_failed")
                print(f"  Card creation failed. Screenshot: {screenshot}")
                context.close()
                return False

            # Brief pause to let Heptabase save
            time.sleep(3)
            print("  Sync complete!")

        except PlaywrightTimeout as e:
            screenshot = take_screenshot(page, "timeout_error")
            print(f"  Timeout error: {e}")
            print(f"  Screenshot: {screenshot}")
            context.close()
            return False
        except Exception as e:
            screenshot = take_screenshot(page, "unexpected_error")
            print(f"  Unexpected error: {e}")
            print(f"  Screenshot: {screenshot}")
            context.close()
            return False

        context.close()

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Sync markdown files to Heptabase Card Library"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to the markdown file",
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="First-time setup: open browser for manual login",
    )
    parser.add_argument(
        "--title",
        help="Override card title (default: extracted from file)",
    )
    parser.add_argument(
        "--headed",
        action="store_true",
        help="Run with visible browser (for debugging)",
    )
    args = parser.parse_args()

    if args.setup:
        success = run_setup()
        sys.exit(0 if success else 1)

    if not args.file:
        parser.error("Please provide a markdown file path, or use --setup")

    file_path = Path(args.file)
    success = run_sync(file_path, headed=args.headed, title=args.title)
    sys.exit(0 if success else 2)


if __name__ == "__main__":
    main()
