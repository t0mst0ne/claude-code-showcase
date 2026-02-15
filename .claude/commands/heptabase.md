---
description: Upload a markdown file to Heptabase as a card
allowed-tools: Read, Bash(python:*)
---

# Heptabase Card Upload

Upload a markdown file to Heptabase Card Library: $ARGUMENTS

## Instructions

### 1. Resolve the File

Resolve `$ARGUMENTS` to an absolute file path. Verify the file exists and is a markdown file (`.md`).

### 2. Preview the Card

Read the file and display:
- **Title** that will be used (from YAML frontmatter `title:` field → first `# H1` heading → filename)
- **Content length** (approximate word count)

Ask the user to confirm before uploading.

### 3. Upload to Heptabase

Run the sync script:

```bash
python scripts/heptabase_sync.py "<absolute-path>" --headed
```

To override the auto-detected title:

```bash
python scripts/heptabase_sync.py "<absolute-path>" --title "Custom Title" --headed
```

### 4. Report Result

Tell the user whether the upload succeeded or failed. If it failed, check `scripts/logs/` for debug screenshots.

## First-Time Setup

If the user has never logged in, run setup first:

```bash
python scripts/heptabase_sync.py --setup
```

This opens a browser for manual Heptabase login. The session is saved to `~/.heptabase-playwright/`.

## How It Works

The script uses Playwright browser automation (Heptabase has no public write API):
1. Opens Heptabase with a persistent browser session
2. Navigates to Card Library
3. Creates a new card (Cmd+N)
4. Types the title and pastes the markdown content

## Title Detection

The card title is auto-detected in this order:
1. YAML frontmatter `title:` field
2. First `# H1` heading in the file
3. Filename stem (without extension)
