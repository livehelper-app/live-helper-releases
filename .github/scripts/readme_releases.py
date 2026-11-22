#!/usr/bin/env python3
"""Rewrite the release list inside README.md.

Usage: readme_releases.py README.md < releases.json

releases.json is what the GitHub API returns for the releases of this repository (a list, or a list of pages).
Only published releases that are not prereleases are listed, newest first, at most MAX_RELEASES of them.
Drafts are never listed and never linked, because visitors cannot open them.
Everything read from a release is data: it is escaped before it goes into the README.
"""

import html
import json
import os
import re
import sys
from urllib.parse import quote

START = "<!-- releases:start -->"
END = "<!-- releases:end -->"
MAX_RELEASES = 10
SUMMARY_MAX = 280
EMPTY = "No release is public yet. Check back soon."

MARKER_LINE = re.compile(r"^\s*(summary\s+[a-z]{2}|mandatory)\s*:", re.IGNORECASE)
SUMMARY_EN = re.compile(r"^\s*summary\s+en\s*:\s*(.*)$", re.IGNORECASE)
MANDATORY = re.compile(r"^\s*mandatory\s*:\s*yes\s*$", re.IGNORECASE | re.MULTILINE)


def flatten(data):
    """Accept one page (a list of releases) or several pages (a list of lists)."""
    out = []
    for item in data:
        if isinstance(item, list):
            out.extend(i for i in item if isinstance(i, dict))
        elif isinstance(item, dict):
            out.append(item)
    return out


def english_summary(body):
    """The text after `Summary EN:`, continued on the next lines until the next marker line."""
    parts = []
    inside = False
    for line in (body or "").splitlines():
        match = SUMMARY_EN.match(line)
        if match:
            inside = True
            parts.append(match.group(1))
        elif inside and MARKER_LINE.match(line):
            break
        elif inside:
            parts.append(line)
    text = " ".join(" ".join(parts).split())
    if len(text) > SUMMARY_MAX:
        text = text[: SUMMARY_MAX - 3].rstrip() + "..."
    return text


def escape(text):
    """Make plain text safe inside one Markdown line: no HTML, no links, no table breaks."""
    text = html.escape(text, quote=False)
    return re.sub(r"([\\`*_\[\]()|~])", r"\\\1", text)


def entry(release, repo):
    tag = str(release.get("tag_name") or "")
    published = str(release.get("published_at") or "")[:10]
    summary = english_summary(release.get("body"))
    url = "https://github.com/{}/releases/tag/{}".format(repo, quote(tag, safe=""))
    line = "- **{}**".format(escape(tag))
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", published):
        line += " ({})".format(published)
    line += ": "
    line += escape(summary) if summary else "No summary was written for this release."
    if MANDATORY.search(release.get("body") or ""):
        line += " Mandatory update."
    line += " [Release page]({})".format(url)
    return line


def build_block(releases, repo):
    public = [
        r
        for r in releases
        if not r.get("draft") and not r.get("prerelease") and r.get("tag_name") and r.get("published_at")
    ]
    public.sort(key=lambda r: str(r["published_at"]), reverse=True)
    lines = [entry(r, repo) for r in public[:MAX_RELEASES]] or [EMPTY]
    return "{}\n{}\n{}".format(START, "\n".join(lines), END)


def replace_block(readme, block):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README.md must hold the start marker and the end marker exactly once each.")
    start = readme.index(START)
    end = readme.index(END)
    if end < start:
        raise ValueError("The end marker comes before the start marker.")
    return readme[:start] + block + readme[end + len(END):]


def main(argv):
    if len(argv) != 2:
        print("Usage: readme_releases.py README.md < releases.json", file=sys.stderr)
        return 2
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        print("Error: GITHUB_REPOSITORY is not set (GitHub Actions sets it).", file=sys.stderr)
        return 2
    releases = flatten(json.load(sys.stdin))
    with open(argv[1], encoding="utf-8") as f:
        readme = f.read()
    try:
        updated = replace_block(readme, build_block(releases, repo))
    except ValueError as error:
        print("Error: {}".format(error), file=sys.stderr)
        return 1
    if updated != readme:
        with open(argv[1], "w", encoding="utf-8", newline="") as f:
            f.write(updated)
        print("README.md updated.")
    else:
        print("README.md is already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
