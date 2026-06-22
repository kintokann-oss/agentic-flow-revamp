#!/usr/bin/env python3
"""Validate that task handoff exports are registered in the correct context catalogs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

PLACEHOLDER_PURPOSES = {"", "(sync — add purpose)", "(sync - add purpose)", "tbd", "todo"}


def load_profile(repo: Path) -> dict:
    path = repo / "docs" / "project.profile.yaml"
    if yaml is None:
        raise SystemExit("PyYAML required: pip install pyyaml")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_slot(profile: dict, slot: str) -> Path:
    if slot.startswith("context."):
        key = slot.removeprefix("context.")
        rel = profile["context_slots"][key]
        return Path(rel)
    raise ValueError(f"Unknown slot: {slot}")


def normalize_path(p: str) -> str:
    return p.replace("\\", "/").strip()


def parse_markdown_table(lines: list[str], start: int) -> tuple[list[str], list[list[str]], int]:
    """Parse a markdown table starting at header row index."""
    if start >= len(lines) or "|" not in lines[start]:
        return [], [], start
    header = [c.strip() for c in lines[start].strip().strip("|").split("|")]
    i = start + 1
    if i < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i].strip()):
        i += 1
    rows: list[list[str]] = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if len(row) == len(header):
            rows.append(row)
        i += 1
    return header, rows, i


def find_section(lines: list[str], heading: str) -> int | None:
    target = heading.strip().lower()
    for i, line in enumerate(lines):
        if line.startswith("## ") and line[3:].strip().lower() == target:
            return i
    return None


def section_has_symbol(lines: list[str], section_start: int, symbol: str, file_path: str) -> tuple[bool, bool]:
    """Return (section_exists, has_valid_purpose_row)."""
    sym = symbol.lower()
    fp = normalize_path(file_path).lower()
    i = section_start + 1
    found_row = False
    has_purpose = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            break
        if line.startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", line.strip()):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            row_text = " ".join(cells).lower()
            if sym in row_text or fp in row_text or any(fp.endswith(c.lower()) for c in cells if c):
                found_row = True
                purpose_idx = None
                header_line = None
                for j in range(section_start + 1, i):
                    if lines[j].startswith("|") and "---" not in lines[j]:
                        header_line = [c.strip().lower() for c in lines[j].strip().strip("|").split("|")]
                        break
                if header_line and "purpose" in header_line:
                    purpose_idx = header_line.index("purpose")
                elif header_line and "handler" in header_line:
                    purpose_idx = None  # api-list uses handler not purpose on route rows
                    has_purpose = True  # route rows valid if symbol/handler matches
                if purpose_idx is not None and purpose_idx < len(cells):
                    purpose = cells[purpose_idx].strip().lower()
                    if purpose and purpose not in PLACEHOLDER_PURPOSES:
                        has_purpose = True
                elif purpose_idx is None and found_row:
                    has_purpose = True
        i += 1
    return found_row, has_purpose


def parse_exports(handoff_path: Path) -> list[dict]:
    if not handoff_path.exists():
        return []
    lines = handoff_path.read_text(encoding="utf-8").splitlines()
    exports: list[dict] = []
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## new or changed exports"):
            header, rows, _ = parse_markdown_table(lines, i + 1)
            if not header:
                header, rows, _ = parse_markdown_table(lines, i + 2)
            col = {h.lower(): idx for idx, h in enumerate(header)}
            sym_i = col.get("symbol", 0)
            file_i = col.get("file", 1)
            kind_i = col.get("kind", 2)
            for row in rows:
                if len(row) <= max(sym_i, file_i, kind_i):
                    continue
                sym = row[sym_i].strip()
                fp = row[file_i].strip()
                kind = row[kind_i].strip().lower()
                if sym or fp:
                    exports.append({"symbol": sym, "file": fp, "kind": kind})
            break
    return exports


def parse_i18n_keys(handoff_path: Path) -> list[dict]:
    if not handoff_path.exists():
        return []
    lines = handoff_path.read_text(encoding="utf-8").splitlines()
    keys: list[dict] = []
    for i, line in enumerate(lines):
        if "i18n keys added" in line.lower():
            header, rows, _ = parse_markdown_table(lines, i + 1)
            if not header:
                continue
            col = {h.lower(): idx for idx, h in enumerate(header)}
            key_i = col.get("namespace.key", col.get("key", 0))
            for row in rows:
                if len(row) <= key_i:
                    continue
                key = row[key_i].strip()
                if key and not key.startswith("<!--"):
                    keys.append({"key": key})
            break
    return keys


def parse_suggested_tests(handoff_path: Path) -> list[str]:
    if not handoff_path.exists():
        return []
    lines = handoff_path.read_text(encoding="utf-8").splitlines()
    files: list[str] = []
    for i, line in enumerate(lines):
        if "suggested test files" in line.lower():
            header, rows, _ = parse_markdown_table(lines, i + 1)
            if not header:
                continue
            col = {h.lower(): idx for idx, h in enumerate(header)}
            test_i = col.get("test file", col.get("test file (colocated)", 1))
            if "test file" not in col and len(header) > 1:
                test_i = 1
            for row in rows:
                if len(row) > test_i:
                    tf = row[test_i].strip()
                    if tf and not tf.startswith("<!--"):
                        files.append(normalize_path(tf))
            break
    return files


def i18n_key_in_catalog(catalog_text: str, key: str) -> bool:
    """Check namespace.key exists in fe-i18n table."""
    if "." in key:
        ns, k = key.split(".", 1)
    else:
        ns, k = "app", key
    pattern = rf"\|\s*{re.escape(ns)}\s*\|\s*{re.escape(k)}\s*\|"
    return bool(re.search(pattern, catalog_text, re.IGNORECASE))


def test_file_in_catalog(catalog_text: str, test_file: str) -> bool:
    tf = normalize_path(test_file)
    return tf in catalog_text.replace("\\", "/")


def audit_task(repo: Path, task_id: str, profile: dict) -> tuple[list[str], list[str]]:
    task_dir = repo / "docs" / "working" / task_id
    errors: list[str] = []
    ok: list[str] = []

    routing = profile.get("context_routing", {})
    be_handoff = task_dir / profile["artifact_slots"]["be_test_handoff"]
    fe_handoff = task_dir / profile["artifact_slots"]["fe_test_handoff"]
    sql_handoff = task_dir / profile["artifact_slots"]["be_sql_handoff"]

    kind_map = routing.get("be_test_handoff", {})
    sql_kind_map = routing.get("be_sql_handoff", {})
    fe_kind_map = routing.get("fe_test_handoff", {})

    for exp in parse_exports(sql_handoff):
        kind = exp["kind"]
        slot = sql_kind_map.get(kind)
        if not slot:
            errors.append(f"SQL export {exp['symbol']}: unknown kind '{kind}'")
            continue
        rel = resolve_slot(profile, slot)
        catalog_path = repo / rel
        if not catalog_path.exists():
            errors.append(f"SQL export {exp['symbol']}: catalog missing {rel}")
            continue
        text = catalog_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        fp = normalize_path(exp["file"])
        sec = find_section(lines, fp)
        if sec is None and kind == "table":
            table_heading = f"## Table: {exp['symbol']}"
            sec = find_section(lines, table_heading.removeprefix("## "))
        if sec is None:
            errors.append(
                f"SQL export {exp['symbol']} ({kind}): missing section in {rel} for {fp}"
            )
            continue
        found, has_purpose = section_has_symbol(lines, sec, exp["symbol"], fp)
        if not found:
            errors.append(
                f"SQL export {exp['symbol']}: no row in section of {rel}"
            )
        elif not has_purpose and kind in ("migration", "db_module"):
            errors.append(
                f"SQL export {exp['symbol']}: row in {rel} missing human purpose"
            )
        else:
            ok.append(f"SQL {exp['symbol']} → {rel}")

    for exp in parse_exports(be_handoff):
        kind = exp["kind"]
        slot = kind_map.get(kind)
        if not slot:
            errors.append(f"BE export {exp['symbol']}: unknown kind '{kind}'")
            continue
        rel = resolve_slot(profile, slot)
        catalog_path = repo / rel
        if not catalog_path.exists():
            errors.append(f"BE export {exp['symbol']}: catalog missing {rel}")
            continue
        text = catalog_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        fp = normalize_path(exp["file"])
        sec = find_section(lines, fp)
        if sec is None:
            errors.append(
                f"BE export {exp['symbol']} ({kind}): missing ## {fp} in {rel}"
            )
            continue
        found, has_purpose = section_has_symbol(lines, sec, exp["symbol"], fp)
        if not found:
            errors.append(
                f"BE export {exp['symbol']}: no row in ## {fp} section of {rel}"
            )
        elif not has_purpose and kind in ("service", "component", "hook"):
            errors.append(
                f"BE export {exp['symbol']}: row in {rel} missing human purpose"
            )
        else:
            ok.append(f"BE {exp['symbol']} → {rel}")

    for exp in parse_exports(fe_handoff):
        kind = exp["kind"]
        slot = fe_kind_map.get(kind)
        if not slot:
            errors.append(f"FE export {exp['symbol']}: unknown kind '{kind}'")
            continue
        rel = resolve_slot(profile, slot)
        catalog_path = repo / rel
        if not catalog_path.exists():
            errors.append(f"FE export {exp['symbol']}: catalog missing {rel}")
            continue
        text = catalog_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        fp = normalize_path(exp["file"])
        sec = find_section(lines, fp)
        if sec is None:
            errors.append(
                f"FE export {exp['symbol']} ({kind}): missing ## {fp} in {rel}"
            )
            continue
        found, has_purpose = section_has_symbol(lines, sec, exp["symbol"], fp)
        if not found:
            errors.append(
                f"FE export {exp['symbol']}: no row in ## {fp} section of {rel}"
            )
        elif not has_purpose:
            errors.append(
                f"FE export {exp['symbol']}: row in {rel} missing human purpose"
            )
        else:
            ok.append(f"FE {exp['symbol']} → {rel}")

    fe_i18n_path = repo / resolve_slot(profile, routing["fe_test_handoff_i18n"]["target"])
    fe_i18n_text = fe_i18n_path.read_text(encoding="utf-8") if fe_i18n_path.exists() else ""
    for item in parse_i18n_keys(fe_handoff):
        key = item["key"]
        if not i18n_key_in_catalog(fe_i18n_text, key):
            errors.append(f"i18n key '{key}' missing from fe-i18n.md")
        else:
            ok.append(f"i18n {key} → fe-i18n.md")

    be_tests_path = repo / resolve_slot(profile, routing["be_test_handoff_tests"]["suggested_test_files"])
    be_tests_text = be_tests_path.read_text(encoding="utf-8") if be_tests_path.exists() else ""
    for tf in parse_suggested_tests(be_handoff):
        if not test_file_in_catalog(be_tests_text, tf):
            errors.append(f"BE test file '{tf}' missing from be-tests.md")
        else:
            ok.append(f"BE test {tf} → be-tests.md")

    fe_tests_path = repo / resolve_slot(profile, routing["fe_test_handoff_tests"]["suggested_test_files"])
    fe_tests_text = fe_tests_path.read_text(encoding="utf-8") if fe_tests_path.exists() else ""
    for tf in parse_suggested_tests(fe_handoff):
        if not test_file_in_catalog(fe_tests_text, tf):
            errors.append(f"FE test file '{tf}' missing from fe-tests.md")
        else:
            ok.append(f"FE test {tf} → fe-tests.md")

    return ok, errors


def format_report(task_id: str, ok: list[str], errors: list[str]) -> str:
    lines = [f"# Context catalog audit - {task_id}", ""]
    if errors:
        lines.append("## Failures")
        lines.append("")
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")
    if ok:
        lines.append("## Passed")
        lines.append("")
        for p in ok:
            lines.append(f"- {p}")
        lines.append("")
    lines.append(f"**Result:** {'PASS' if not errors else 'FAIL'} ({len(ok)} passed, {len(errors)} failed)")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate context catalog rows for a task")
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--task", required=True, help="TASK-ID e.g. TASK-002")
    parser.add_argument("--write", type=Path, help="Write report to this path")
    args = parser.parse_args()

    repo = args.repo.resolve()
    profile = load_profile(repo)
    ok, errors = audit_task(repo, args.task, profile)
    report = format_report(args.task, ok, errors)
    print(report)

    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(report, encoding="utf-8")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
