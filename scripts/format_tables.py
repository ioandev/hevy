#!/usr/bin/env python3
"""Format markdown tables in routine files so columns align in a monospace editor."""

import re
from pathlib import Path


def fmt_row(cells, widths):
    parts = [c.ljust(w) for c, w in zip(cells, widths)]
    return "| " + " | ".join(parts) + " |"


def fmt_sep(widths):
    return "| " + " | ".join("-" * w for w in widths) + " |"


def format_table(lines):
    """Given a list of raw table lines, return formatted lines."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)

    if not rows:
        return lines

    header = rows[0]
    data_rows = [r for r in rows[1:] if not all(set(c) <= {"-", " "} for c in r)]
    all_rows = [header] + data_rows
    widths = [max(len(r[i]) for r in all_rows) for i in range(len(header))]

    result = [fmt_row(header, widths), fmt_sep(widths)]
    for row in data_rows:
        result.append(fmt_row(row, widths))
    return result


def format_file(path):
    text = path.read_text()
    out_lines = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|"):
            table_raw = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_raw.append(lines[i])
                i += 1
            out_lines.extend(format_table(table_raw))
        else:
            out_lines.append(line)
            i += 1
    path.write_text("\n".join(out_lines) + "\n")
    print(f"Formatted {path}")


if __name__ == "__main__":
    routines_dir = Path(__file__).parent.parent / "routines"
    for md_file in sorted(routines_dir.glob("*.md")):
        format_file(md_file)
