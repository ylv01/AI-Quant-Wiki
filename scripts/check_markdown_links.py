#!/usr/bin/env python3
"""Check that local relative links in Markdown files resolve to existing paths."""

from __future__ import annotations

import re
import sys
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit


INLINE_LINK_RE = re.compile(
    r"!?\[[^\]\n]*\]\((?P<target><[^>\n]+>|(?:\\.|[^)\n])+)\)"
)
REFERENCE_LINK_RE = re.compile(
    r"^\s*\[[^\]\n]+\]:\s*(?P<target><[^>\n]+>|\S+)"
)
IGNORED_SCHEMES = {"http", "https", "mailto"}


def normalize_target(raw_target: str) -> str:
    """Remove Markdown title syntax and surrounding angle brackets."""
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1].strip()
    return target.split(maxsplit=1)[0].replace("\\ ", " ")


def is_relative_local_link(target: str) -> bool:
    if not target or target.startswith("#") or target.startswith("//"):
        return False
    parsed = urlsplit(target)
    if parsed.scheme.lower() in IGNORED_SCHEMES:
        return False
    if parsed.scheme:
        return False
    local_path = unquote(parsed.path)
    if not local_path:
        return False
    if Path(local_path).is_absolute() or PureWindowsPath(local_path).is_absolute():
        return False
    return True


def iter_targets(line: str):
    for match in INLINE_LINK_RE.finditer(line):
        yield normalize_target(match.group("target"))
    reference_match = REFERENCE_LINK_RE.match(line)
    if reference_match:
        yield normalize_target(reference_match.group("target"))


def check_file(markdown_file: Path):
    errors = []
    in_fence = False
    for line_number, line in enumerate(
        markdown_file.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for target in iter_targets(line):
            if not is_relative_local_link(target):
                continue
            parsed = urlsplit(target)
            local_path = unquote(parsed.path)
            candidate = (markdown_file.parent / local_path).resolve()
            if not candidate.exists():
                errors.append((line_number, target))
    return errors


def main() -> int:
    repository_root = Path(__file__).resolve().parents[1]
    failures = []
    for markdown_file in sorted(repository_root.rglob("*.md")):
        for line_number, target in check_file(markdown_file):
            failures.append(
                (markdown_file.relative_to(repository_root), line_number, target)
            )

    if failures:
        for file_path, line_number, target in failures:
            print(f"{file_path}:{line_number}: invalid relative link: {target}")
        print(f"Found {len(failures)} invalid relative link(s).")
        return 1

    print("All Markdown relative links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
