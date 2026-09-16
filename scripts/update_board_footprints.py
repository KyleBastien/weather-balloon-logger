"""Replace embedded KiCad board footprints with exact library geometry.

Run with KiCad's bundled Python, for example:

    "C:\\Program Files\\KiCad\\10.0\\bin\\python.exe" \
        scripts/update_board_footprints.py --group pass1

The replacement preserves each footprint's reference, value, schematic path,
position, orientation, board side, lock state, and pad nets by pad number.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pcbnew


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BOARD_PATH = PROJECT_ROOT / "weather-balloon-logger.kicad_pcb"
KICAD_FOOTPRINT_ROOT = Path(r"C:\Program Files\KiCad\10.0\share\kicad\footprints")


TARGETS = {
    "H1": ("MountingHole", "MountingHole_2.2mm_M2"),
    "H2": ("MountingHole", "MountingHole_2.2mm_M2"),
    "H3": ("MountingHole", "MountingHole_2.2mm_M2"),
    "H4": ("MountingHole", "MountingHole_2.2mm_M2"),
    "J1": ("Connector_JST", "JST_PH_S2B-PH-K_1x02_P2.00mm_Horizontal"),
    "SW1": ("WeatherBalloon", "SW_CK_7101SYZQE"),
    "J2": ("Connector_PinHeader_2.54mm", "PinHeader_1x11_P2.54mm_Vertical"),
    "A1": ("WeatherBalloon", "SparkFun_OpenLog_DEV-13712_Carrier"),
    "J5": ("Connector_JST", "JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal"),
    "J6": ("Connector_PinHeader_2.54mm", "PinHeader_1x01_P2.54mm_Vertical"),
    "J7": ("Connector_PinHeader_2.54mm", "PinHeader_1x01_P2.54mm_Vertical"),
    "U1": ("Package_SO", "SOIC-16_3.9x9.9mm_P1.27mm"),
    "C1": ("Capacitor_SMD", "C_0603_1608Metric"),
    "C2": ("Capacitor_SMD", "C_0603_1608Metric"),
    "C3": ("Capacitor_SMD", "C_0603_1608Metric"),
    "J3": ("Connector_Coaxial", "SMA_Amphenol_132134_Vertical"),
    "J4": ("Connector_Coaxial", "SMA_Amphenol_132134_Vertical"),
    "Q1": ("Package_TO_SOT_SMD", "SOT-23"),
    "R1": ("Resistor_SMD", "R_0603_1608Metric"),
    "R2": ("Resistor_SMD", "R_0603_1608Metric"),
    "R3": ("Resistor_SMD", "R_0603_1608Metric"),
    "D1": ("LED_SMD", "LED_0603_1608Metric"),
}


GROUPS = {
    "pass1": [
        "C1", "C2", "C3", "R1", "R2", "R3", "D1", "U1", "Q1",
        "H1", "H2", "H3", "H4", "J2", "J6", "J7",
    ],
    "power": ["J1", "J5", "SW1"],
    "openlog": ["A1"],
    "sma": ["J3", "J4"],
    "connectors": ["J1", "J5", "SW1", "A1", "J3", "J4"],
    "all": list(TARGETS),
}

# The legacy J2 placeholder was drawn with its pad row on the local X axis and
# rotated 270 degrees on the board. KiCad's stock 1x11 footprint is drawn along
# local Y, so 0 degrees preserves the existing vertical connector orientation.
ORIENTATION_OVERRIDES_DEGREES = {
    "J2": 0.0,
}


def library_dir(nickname: str) -> Path:
    if nickname == "WeatherBalloon":
        return PROJECT_ROOT / "library" / "WeatherBalloon.pretty"
    return KICAD_FOOTPRINT_ROOT / f"{nickname}.pretty"


def replace_footprint(
    board: pcbnew.BOARD, old_by_reference: dict[str, pcbnew.FOOTPRINT], reference: str
) -> None:
    old = old_by_reference.get(reference)
    if old is None:
        raise RuntimeError(f"footprint {reference} not found on board")

    nickname, item_name = TARGETS[reference]
    lib_dir = library_dir(nickname)
    new = pcbnew.FootprintLoad(str(lib_dir), item_name)
    if new is None:
        raise RuntimeError(f"could not load {nickname}:{item_name} from {lib_dir}")

    old_nets = {pad.GetNumber(): pad.GetNet() for pad in old.Pads() if pad.GetNumber()}
    new_numbers = {pad.GetNumber() for pad in new.Pads() if pad.GetNumber()}
    missing = sorted(set(old_nets) - new_numbers)
    if missing:
        raise RuntimeError(
            f"{reference} target {nickname}:{item_name} lacks pad(s) {missing}"
        )

    new.SetReference(old.GetReference())
    new.SetValue(old.GetValue())
    new.SetPosition(old.GetPosition())
    new.SetOrientation(old.GetOrientation())
    if reference in ORIENTATION_OVERRIDES_DEGREES:
        new.SetOrientationDegrees(ORIENTATION_OVERRIDES_DEGREES[reference])
    new.SetLayer(old.GetLayer())
    new.SetPath(old.GetPath())
    new.SetSheetfile(old.GetSheetfile())
    new.SetSheetname(old.GetSheetname())
    new.SetLocked(old.IsLocked())
    if hasattr(new, "SetAttributes") and hasattr(old, "GetAttributes"):
        new.SetAttributes(old.GetAttributes())

    for pad in new.Pads():
        net = old_nets.get(pad.GetNumber())
        if net is not None:
            pad.SetNet(net)

    board.Remove(old)
    board.Add(new)
    print(f"{reference}: {nickname}:{item_name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", choices=GROUPS, required=True)
    parser.add_argument("--board", type=Path, default=BOARD_PATH)
    args = parser.parse_args()

    board_path = args.board.resolve()
    board = pcbnew.LoadBoard(str(board_path))
    old_by_reference = {fp.GetReference(): fp for fp in list(board.GetFootprints())}
    for reference in GROUPS[args.group]:
        replace_footprint(board, old_by_reference, reference)
    pcbnew.SaveBoard(str(board_path), board)


if __name__ == "__main__":
    main()
