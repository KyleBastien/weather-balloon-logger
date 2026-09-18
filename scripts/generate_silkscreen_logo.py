"""Generate the front-silkscreen coffee/balloon logo footprint.

Run with:

    uv run --with pillow python scripts/generate_silkscreen_logo.py

The raster is thresholded, tightly cropped, and emitted as filled 0.15 mm
silkscreen cells.  That grid matches common low-cost PCB silkscreen limits and
keeps the footprint deterministic without depending on external vector tools.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "silkscreen" / "coffee-balloon-original.jpg"
PREVIEW = ROOT / "assets" / "silkscreen" / "coffee-balloon-silkscreen.png"
FOOTPRINT = (
    ROOT
    / "library"
    / "WeatherBalloon.pretty"
    / "CoffeeBalloon_7.5x11.25mm.kicad_mod"
)

THRESHOLD = 100
CELL_MM = 0.15
TARGET_WIDTH_CELLS = 50
PADDING_CELLS = 1


def runs(row: list[bool]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    start: int | None = None
    for index, value in enumerate(row + [False]):
        if value and start is None:
            start = index
        elif not value and start is not None:
            result.append((start, index))
            start = None
    return result


def main() -> None:
    grayscale = Image.open(SOURCE).convert("L")
    dark = grayscale.point(lambda value: 255 if value < THRESHOLD else 0)
    bbox = dark.getbbox()
    if bbox is None:
        raise RuntimeError("No dark artwork found in source image")

    cropped = dark.crop(bbox)
    aspect = cropped.height / cropped.width
    target_height = round(TARGET_WIDTH_CELLS * aspect)
    raster = cropped.resize(
        (TARGET_WIDTH_CELLS, target_height), Image.Resampling.LANCZOS
    ).point(lambda value: 255 if value >= 128 else 0)

    preview = Image.new(
        "L",
        (
            raster.width + 2 * PADDING_CELLS,
            raster.height + 2 * PADDING_CELLS,
        ),
        0,
    )
    preview.paste(raster, (PADDING_CELLS, PADDING_CELLS))
    preview.resize(
        (preview.width * 8, preview.height * 8), Image.Resampling.NEAREST
    ).save(PREVIEW)

    width_mm = raster.width * CELL_MM
    height_mm = raster.height * CELL_MM
    x_origin = -width_mm / 2
    y_origin = -height_mm / 2

    rectangles: list[str] = []
    pixels = raster.load()
    for row_index in range(raster.height):
        row = [pixels[column, row_index] != 0 for column in range(raster.width)]
        for start, end in runs(row):
            x0 = x_origin + start * CELL_MM
            x1 = x_origin + end * CELL_MM
            y0 = y_origin + row_index * CELL_MM
            y1 = y0 + CELL_MM
            rectangles.append(
                "  (fp_rect "
                f"(start {x0:.3f} {y0:.3f}) (end {x1:.3f} {y1:.3f})\n"
                "    (stroke (width 0) (type default)) "
                '(fill solid) (layer "F.SilkS"))'
            )

    content = "\n".join(
        [
            '(footprint "CoffeeBalloon_7.5x11.25mm"',
            "  (version 20240108)",
            '  (generator "generate_silkscreen_logo.py")',
            '  (layer "F.Cu")',
            '  (descr "Coffee cup and weather balloon front-silkscreen artwork")',
            '  (tags "logo graphic silkscreen coffee weather balloon")',
            '  (property "Reference" "G***" (at 0 0 0) (layer "F.SilkS") hide',
            "    (effects (font (size 1 1) (thickness 0.15))))",
            '  (property "Value" "CoffeeBalloon_7.5x11.25mm" '
            '(at 0 0 0) (layer "F.Fab") hide',
            "    (effects (font (size 1 1) (thickness 0.15))))",
            "  (attr board_only exclude_from_pos_files exclude_from_bom)",
            *rectangles,
            ")",
            "",
        ]
    )
    FOOTPRINT.write_text(content, encoding="utf-8", newline="\n")
    print(
        f"Generated {FOOTPRINT.relative_to(ROOT)}: "
        f"{width_mm:.2f} x {height_mm:.2f} mm, {len(rectangles)} filled runs"
    )


if __name__ == "__main__":
    main()
