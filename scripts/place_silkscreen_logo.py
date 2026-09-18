"""Place the generated logo footprint without reformatting the KiCad board.

Run after generate_silkscreen_logo.py:

    python scripts/place_silkscreen_logo.py

The script deliberately edits the S-expression as text. Loading and saving the
whole board through pcbnew rewrites unrelated footprint geometry and obscures
the actual review diff.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOARD_PATH = ROOT / "weather-balloon-logger.kicad_pcb"
FOOTPRINT_PATH = (
    ROOT
    / "library"
    / "WeatherBalloon.pretty"
    / "CoffeeBalloon_7.5x11.25mm.kicad_mod"
)
FOOTPRINT_START = '\n\t(footprint "CoffeeBalloon_7.5x11.25mm"'


def matching_close(text: str, start: int) -> int:
    depth = 0
    quoted = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index + 1
    raise RuntimeError("Unbalanced footprint expression")


def main() -> None:
    board = BOARD_PATH.read_text(encoding="utf-8")

    existing = board.find(FOOTPRINT_START)
    if existing >= 0:
        close = matching_close(board, existing + 2)
        board = board[:existing] + board[close:]

    footprint = FOOTPRINT_PATH.read_text(encoding="utf-8").rstrip()
    footprint = footprint.replace(
        '  (layer "F.Cu")',
        '  (layer "F.Cu")\n'
        '  (uuid "d21d9b33-a69e-5b1c-a4dc-4ff70ed4de0e")\n'
        "  (at 140 164)",
        1,
    )
    footprint = footprint.replace('"G***"', '"G1"', 1)
    footprint = footprint.replace(
        '"CoffeeBalloon_7.5x11.25mm" (at 0 0 0)',
        '"Coffee Balloon Logo" (at 0 0 0)',
        1,
    )
    embedded = "\n".join("\t" + line for line in footprint.splitlines())

    insertion = board.find("\n\t(gr_rect")
    if insertion < 0:
        raise RuntimeError("Could not find board graphics insertion point")
    board = board[:insertion] + "\n" + embedded + "\n" + board[insertion:]

    old_caption = '(gr_text "U2 DRIVER - LEFT DIP"\n\t\t(at 140 158.5 0)'
    new_caption = '(gr_text "U2 DRIVER - LEFT DIP"\n\t\t(at 140 157 0)'
    if old_caption in board:
        board = board.replace(old_caption, new_caption, 1)
    elif new_caption not in board:
        raise RuntimeError("Could not find the U2 driver caption")

    BOARD_PATH.write_text(board, encoding="utf-8", newline="\n")
    print("Placed G1 on F.SilkS at (140, 164) mm and moved U2 caption to y=157 mm")


if __name__ == "__main__":
    main()
