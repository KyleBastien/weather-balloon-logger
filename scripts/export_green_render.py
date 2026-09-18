"""Rasterize the tracked 2D board plot over a green PCB background."""

from __future__ import annotations

from pathlib import Path

import cairosvg


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outputs" / "renders" / "board-full-color.svg"
OUTPUT = ROOT / "outputs" / "renders" / "board-green-top.png"
BOARD_GREEN = "#174a34"


def main() -> None:
    svg = SOURCE.read_text(encoding="utf-8")
    svg_start = svg.find("<svg")
    opening_end = svg.find(">", svg_start)
    if svg_start < 0 or opening_end < 0:
        raise RuntimeError("Could not find the SVG root element")

    background = (
        f'\n<rect x="0" y="0" width="100%" height="100%" '
        f'fill="{BOARD_GREEN}"/>\n'
    )
    composited = svg[: opening_end + 1] + background + svg[opening_end + 1 :]

    cairosvg.svg2png(
        bytestring=composited.encode("utf-8"),
        write_to=str(OUTPUT),
        output_width=2400,
    )
    print(f"Wrote flat green-board render to '{OUTPUT}'")


if __name__ == "__main__":
    main()
