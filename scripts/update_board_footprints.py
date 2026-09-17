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
    "U1": ("Package_DIP", "DIP-16_W7.62mm"),
    "C1": ("WeatherBalloon", "KEMET_C322C475K5R5TA"),
    "C2": ("WeatherBalloon", "KEMET_C315C104K5R5TA"),
    "C3": ("WeatherBalloon", "KEMET_C315C104K5R5TA"),
    "J3": ("Connector_Coaxial", "SMA_Amphenol_132134_Vertical"),
    "J4": ("Connector_Coaxial", "SMA_Amphenol_132134_Vertical"),
    "Q1": ("Package_TO_SOT_THT", "TO-220-3_Vertical"),
    "R1": ("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal"),
    "R2": ("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal"),
    "R3": ("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal"),
    "D1": ("LED_THT", "LED_D3.0mm"),
}


GROUPS = {
    "pass1": [
        "C1", "C2", "C3", "R1", "R2", "R3", "D1", "U1", "Q1",
        "H1", "H2", "H3", "H4", "J2", "J6", "J7",
    ],
    "tht_existing": ["C1", "C2", "C3", "R1", "R2", "R3", "D1", "U1", "Q1"],
    "add_driver": [],
    "power": ["J1", "J5", "SW1"],
    "openlog": ["A1"],
    "sma": ["J3", "J4"],
    "connectors": ["J1", "J5", "SW1", "A1", "J3", "J4"],
    "all": list(TARGETS),
}

ADDITIONS = {
    "U2": {
        "library": ("Package_DIP", "DIP-8_W7.62mm"),
        "value": "TC4422AVPA",
        "position": (114.0, 133.0),
        "rotation": 0.0,
        "nets": {
            "1": "LOGGER_5V", "2": "CUTDOWN_CTRL", "4": "GND",
            "5": "GND", "6": "CUTDOWN_DRIVE", "7": "CUTDOWN_DRIVE",
            "8": "LOGGER_5V",
        },
    },
    "C4": {
        "library": ("WeatherBalloon", "KEMET_C315C104K5R5TA"),
        "value": "100nF",
        "position": (104.0, 146.0),
        "rotation": 0.0,
        "nets": {"1": "LOGGER_5V", "2": "GND"},
    },
    "C5": {
        "library": ("WeatherBalloon", "KEMET_C322C475K5R5TA"),
        "value": "4.7uF",
        "position": (101.0, 151.0),
        "rotation": 0.0,
        "nets": {"1": "LOGGER_5V", "2": "GND"},
    },
}

# The legacy J2 placeholder was drawn with its pad row on the local X axis and
# rotated 270 degrees on the board. KiCad's stock 1x11 footprint is drawn along
# local Y, so 0 degrees preserves the existing vertical connector orientation.
ORIENTATION_OVERRIDES_DEGREES = {
    "J2": 0.0,
    "D1": 0.0,
    "Q1": 0.0,
    "R1": 0.0,
    "R2": 0.0,
    "R3": 180.0,
}

POSITION_OVERRIDES_MM = {
    "C1": (173.0, 115.0),
    "C2": (173.0, 121.0),
    "C3": (173.0, 132.0),
    "U1": (161.0, 121.5),
    "R1": (160.0, 145.0),
    "D1": (174.0, 145.0),
    "Q1": (115.7, 147.0),
    "R2": (108.0, 151.0),
    "R3": (115.7, 155.0),
}

# Q1 changes from AO3400A G/S/D = 1/2/3 to IRLZ44N G/D/S = 1/2/3.
OLD_PAD_FOR_NEW_PAD = {"Q1": {"1": "1", "2": "3", "3": "2"}}


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
    if reference in POSITION_OVERRIDES_MM:
        x_mm, y_mm = POSITION_OVERRIDES_MM[reference]
        new.SetPosition(pcbnew.VECTOR2I_MM(x_mm, y_mm))
    new.SetLayer(old.GetLayer())
    new.SetPath(old.GetPath())
    new.SetSheetfile(old.GetSheetfile())
    new.SetSheetname(old.GetSheetname())
    new.SetLocked(old.IsLocked())
    if hasattr(new, "SetAttributes") and hasattr(old, "GetAttributes"):
        new.SetAttributes(old.GetAttributes())

    for pad in new.Pads():
        old_number = OLD_PAD_FOR_NEW_PAD.get(reference, {}).get(
            pad.GetNumber(), pad.GetNumber()
        )
        net = old_nets.get(old_number)
        if net is not None:
            pad.SetNet(net)

    board.Remove(old)
    board.Add(new)
    print(f"{reference}: {nickname}:{item_name}")


def ensure_net(board: pcbnew.BOARD, name: str) -> pcbnew.NETINFO_ITEM:
    net = board.FindNet(name)
    if net is None:
        net = pcbnew.NETINFO_ITEM(board, name)
        board.Add(net)
    return net


def add_missing_footprints(board: pcbnew.BOARD) -> None:
    existing = {fp.GetReference() for fp in board.GetFootprints()}
    for reference, spec in ADDITIONS.items():
        if reference in existing:
            continue
        nickname, item_name = spec["library"]
        footprint = pcbnew.FootprintLoad(str(library_dir(nickname)), item_name)
        if footprint is None:
            raise RuntimeError(f"could not load {nickname}:{item_name}")
        footprint.SetReference(reference)
        footprint.SetValue(spec["value"])
        footprint.SetPosition(pcbnew.VECTOR2I_MM(*spec["position"]))
        footprint.SetOrientationDegrees(spec["rotation"])
        for pad in footprint.Pads():
            net_name = spec["nets"].get(pad.GetNumber())
            if net_name:
                pad.SetNet(ensure_net(board, net_name))
        board.Add(footprint)
        print(f"{reference}: added {nickname}:{item_name}")

    # R2 pad 1 now receives the gate-driver output, not the host GPIO directly.
    r2 = next(fp for fp in board.GetFootprints() if fp.GetReference() == "R2")
    next(p for p in r2.Pads() if p.GetNumber() == "1").SetNet(
        ensure_net(board, "CUTDOWN_DRIVE")
    )


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
    if args.group in {"tht_existing", "add_driver"}:
        add_missing_footprints(board)
    pcbnew.SaveBoard(str(board_path), board)


if __name__ == "__main__":
    main()
