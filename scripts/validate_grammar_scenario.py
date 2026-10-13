#!/usr/bin/env python3
"""Validate the structural and interaction contract of a grammar-scenario lesson."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REQUIRED_STAGES = {"context", "meaning", "pattern-discovery", "application", "output"}

REQUIRED_TOKENS = {
    "responsive styles": "@media",
    "keyboard focus": ":focus-visible",
    "live feedback": 'aria-live="polite"',
    "speech support": "speechSynthesis",
    "safe speech reset": "window.speechSynthesis?.cancel()",
    "global reset": 'id="resetAll"',
}


def fail(errors: list[str]) -> int:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_grammar_scenario.py /absolute/path/to/lesson.html")
        return 2

    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.is_file():
        return fail([f"HTML file not found: {path}"])

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not re.search(r"<!doctype html>", text, re.I):
        errors.append("Missing HTML5 doctype")
    if not re.search(r'<body[^>]+data-lesson-mode=["\']grammar-scenario["\']', text, re.I):
        errors.append('Body must include data-lesson-mode="grammar-scenario"')

    grammar_target = re.search(r'data-grammar-target=["\']([^"\']+)["\']', text, re.I)
    if not grammar_target or not grammar_target.group(1).strip():
        errors.append("Body needs a non-empty data-grammar-target")

    stages = set(re.findall(r'data-stage=["\']([^"\']+)["\']', text, re.I))
    missing_stages = sorted(REQUIRED_STAGES - stages)
    if missing_stages:
        errors.append("Missing learning stages: " + ", ".join(missing_stages))

    section_count = len(re.findall(r"<section\b", text, re.I))
    if section_count < 5:
        errors.append(f"Need at least five lesson sections; found {section_count}")

    contrast_count = len(re.findall(r'data-contrast=["\'][^"\']+["\']', text, re.I))
    if contrast_count < 2:
        errors.append("Meaning stage needs at least two data-contrast states")

    for label, token in REQUIRED_TOKENS.items():
        if token not in text:
            errors.append(f"Missing required function: {label}")

    if not re.search(r'id=["\'](?:showAnswers|showModel|revealModel)["\']', text):
        errors.append("Missing a model-answer reveal control")
    if "correct" not in text or "wrong" not in text:
        errors.append("Missing immediate correct/wrong feedback states")

    listener_count = len(re.findall(r"addEventListener\s*\(", text))
    if listener_count < 5:
        errors.append(f"Need several meaningful interactions; found {listener_count} event listeners")

    ids = re.findall(r'\bid=["\']([^"\']+)["\']', text)
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append("Duplicate IDs: " + ", ".join(duplicates))

    anchors = re.findall(r'href=["\']#([^"\']+)["\']', text)
    missing_anchors = sorted(set(anchors) - set(ids))
    if missing_anchors:
        errors.append("Navigation targets missing: " + ", ".join(missing_anchors))

    if not re.search(r"<style(?:\s[^>]*)?>.*?</style>", text, re.S | re.I):
        errors.append("Missing inline CSS")
    if re.search(r'(?:src|href)=["\']https?://', text, re.I):
        errors.append("Remote asset found; lesson must work offline")

    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.S | re.I)
    if not scripts:
        errors.append("Missing inline JavaScript")
    elif shutil.which("node"):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tmp:
            tmp.write("\n".join(scripts))
            tmp_path = Path(tmp.name)
        try:
            result = subprocess.run(["node", "--check", str(tmp_path)], capture_output=True, text=True)
            if result.returncode:
                errors.append("JavaScript syntax error: " + (result.stderr.strip() or result.stdout.strip()))
        finally:
            tmp_path.unlink(missing_ok=True)

    if errors:
        return fail(errors)

    target = grammar_target.group(1) if grammar_target else "unknown"
    print(f"PASS: {path}")
    print(
        f"Grammar target: {target}; stages: {len(stages)}; sections: {section_count}; "
        f"contrast states: {contrast_count}; event listeners: {listener_count}; unique IDs: {len(ids)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
