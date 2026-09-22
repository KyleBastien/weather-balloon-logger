"""Deterministically rebuild the provisional LightHAB carrier PCB.

Run with KiCad's bundled Python.  LightHAB mechanical coordinates in this
draft are deliberately provisional and the board is marked not for fab.
"""

from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[1]
BOARD_PATH = ROOT / "weather-balloon-logger.kicad_pcb"
KICAD_FP = Path(r"C:\Program Files\KiCad\10.0\share\kicad\footprints")
PROJECT_FP = ROOT / "library" / "WeatherBalloon.pretty"


NETS = {
    "VBATT": {"J1.1", "A2.1", "A2.2"},
    "GND": {"J1.2", "J2.4", "A2.3", "A1.2", "C1.2", "C2.2", "J3.2", "J5.2"},
    "LOGGER_5V": {"A2.4", "A1.3", "C1.1", "C2.1"},
    "3V3": {"J2.3", "R1.1", "R2.1"},
    "UART_TX": {"J2.1", "R4.1"},
    "OPENLOG_RXI": {"R4.2", "A1.5"},
    "LED_A": {"R1.2", "D1.2"},
    "LED_N": {"J2.2", "D1.1", "R2.2"},
    "OUT1": {"J3.1", "J5.1"},
}


# Reference: (library, footprint, value, x, y, rotation)
PARTS = {
    "A1": ("WeatherBalloon", "SparkFun_OpenLog_DEV-13712_Carrier", "OpenLog", 116.5, 110.0, 0),
    "R4": ("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal", "1k", 128.0, 106.0, 180),
    "A2": ("WeatherBalloon", "Pololu_S7V8F5_Carrier", "Pololu S7V8F5", 103.0, 140.0, 0),
    "C1": ("WeatherBalloon", "KEMET_C322C475K5R5TA", "4.7uF", 116.0, 132.0, 0),
    "C2": ("WeatherBalloon", "KEMET_C315C104K5R5TA", "100nF", 116.0, 138.0, 0),
    "R1": ("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal", "1k", 110.0, 116.0, 0),
    "D1": ("LED_THT", "LED_D3.0mm", "WP710A10SGC", 122.7, 116.0, 180),
    "R2": ("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal", "100k", 110.0, 120.0, 0),
    "J5": ("Connector_JST", "JST_XH_S2B-XH-A_1x02_P2.50mm_Horizontal", "Cutdown output", 108.5, 158.0, 180),
    # Photo-derived LightHAB mating locations: intentionally provisional.
    "J2": ("Connector_PinHeader_2.54mm", "PinHeader_1x09_P2.54mm_Vertical", "LightHABTracker 1.0", 136.5, 109.0, 0),
    "J1": ("Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical", "LightHAB VBATT/GND", 144.0, 142.0, 0),
    "J3": ("Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical", "LightHAB OUT1/GND", 144.0, 155.0, 0),
}

POWER_NETS = {"VBATT", "GND", "LOGGER_5V", "OUT1"}


def fp_dir(nickname: str) -> Path:
    return PROJECT_FP if nickname == "WeatherBalloon" else KICAD_FP / f"{nickname}.pretty"


def add_net(board: pcbnew.BOARD, name: str) -> pcbnew.NETINFO_ITEM:
    net = pcbnew.NETINFO_ITEM(board, name)
    board.Add(net)
    return net


def add_part(board: pcbnew.BOARD, ref: str, spec, nets_by_name) -> pcbnew.FOOTPRINT:
    nickname, item, value, x, y, rotation = spec
    fp = pcbnew.FootprintLoad(str(fp_dir(nickname)), item)
    if fp is None:
        raise RuntimeError(f"cannot load {nickname}:{item}")
    fp.SetReference(ref)
    fp.SetValue(value)
    fp.SetPosition(pcbnew.VECTOR2I_MM(x, y))
    fp.SetOrientationDegrees(rotation)
    fp.Reference().SetVisible(False)
    fp.Value().SetVisible(False)
    for pad in fp.Pads():
        key = f"{ref}.{pad.GetNumber()}"
        for net_name, members in NETS.items():
            if key in members:
                pad.SetNet(nets_by_name[net_name])
                break
    board.Add(fp)
    return fp


def add_shape(board, start, end, layer, width=0.25, dashed=False):
    shape = pcbnew.PCB_SHAPE(board)
    shape.SetShape(pcbnew.SHAPE_T_SEGMENT)
    shape.SetStart(pcbnew.VECTOR2I_MM(*start))
    shape.SetEnd(pcbnew.VECTOR2I_MM(*end))
    shape.SetLayer(layer)
    shape.SetWidth(pcbnew.FromMM(width))
    # KiCad's Python enum name for dashed styles is not stable across builds;
    # the surrounding warning text carries the provisional status.
    board.Add(shape)


def add_rect(board, x1, y1, x2, y2, layer, width=0.25, dashed=False):
    add_shape(board, (x1, y1), (x2, y1), layer, width, dashed)
    add_shape(board, (x2, y1), (x2, y2), layer, width, dashed)
    add_shape(board, (x2, y2), (x1, y2), layer, width, dashed)
    add_shape(board, (x1, y2), (x1, y1), layer, width, dashed)


def add_text(board, value, x, y, layer=pcbnew.F_SilkS, size=1.1, thickness=0.18, angle=0, justify=None):
    text = pcbnew.PCB_TEXT(board)
    text.SetText(value)
    text.SetPosition(pcbnew.VECTOR2I_MM(x, y))
    text.SetLayer(layer)
    text.SetTextSize(pcbnew.VECTOR2I_MM(size, size))
    text.SetTextThickness(pcbnew.FromMM(thickness))
    text.SetTextAngle(pcbnew.EDA_ANGLE(angle, pcbnew.DEGREES_T))
    if justify:
        text.SetHorizJustify(justify)
    board.Add(text)


def add_hole(board, ref, x, y):
    fp = pcbnew.FootprintLoad(str(fp_dir("MountingHole")), "MountingHole_3.2mm_M3")
    if fp is None:
        raise RuntimeError("cannot load 3.2 mm mounting hole")
    fp.SetReference(ref)
    fp.SetValue("LIGHTHAB HOLE - UNVERIFIED")
    fp.SetPosition(pcbnew.VECTOR2I_MM(x, y))
    fp.Reference().SetVisible(False)
    fp.Value().SetVisible(False)
    board.Add(fp)


def add_track(board, net, start, end, layer, width):
    if start == end:
        return
    track = pcbnew.PCB_TRACK(board)
    track.SetNet(net)
    track.SetLayer(layer)
    track.SetWidth(pcbnew.FromMM(width))
    track.SetStart(start)
    track.SetEnd(end)
    board.Add(track)


def route_path(board, net, layer, points, width):
    def vector(point):
        return point if isinstance(point, pcbnew.VECTOR2I) else pcbnew.VECTOR2I_MM(*point)

    for start, end in zip(points, points[1:]):
        add_track(board, net, vector(start), vector(end), layer, width)


def main():
    board = pcbnew.BOARD()
    board.SetCopperLayerCount(2)
    board.GetTitleBlock().SetTitle("Weather Balloon Logger — provisional LightHAB carrier")
    board.GetTitleBlock().SetComment(0, "UNVERIFIED LIGHTHAB FIT — DO NOT FABRICATE")

    nets = {name: add_net(board, name) for name in NETS}
    footprints = {ref: add_part(board, ref, spec, nets) for ref, spec in PARTS.items()}

    # Four photo-derived placeholder holes, not claimed as module dimensions.
    for ref, x, y in (
        ("H1", 138.0, 99.0),
        ("H2", 186.0, 99.0),
        ("H3", 138.0, 166.0),
        ("H4", 186.0, 166.0),
    ):
        add_hole(board, ref, x, y)

    logo = pcbnew.FootprintLoad(str(PROJECT_FP), "CoffeeBalloon_7.5x11.25mm")
    if logo:
        logo.SetReference("G1")
        logo.SetValue("Coffee Balloon")
        logo.SetPosition(pcbnew.VECTOR2I_MM(126.0, 163.0))
        board.Add(logo)

    # Exact carrier outline.
    add_rect(board, 100.0, 90.0, 190.0, 170.0, pcbnew.Edge_Cuts, 0.2)

    # Module and connector clearance annotations.  These are drawings, not
    # electrical footprints or RF pads.
    add_rect(board, 134.0, 95.0, 190.0, 170.0, pcbnew.Cmts_User, 0.35, True)
    add_rect(board, 146.0, 158.0, 160.0, 170.0, pcbnew.Cmts_User, 0.3, True)
    add_rect(board, 170.0, 158.0, 184.0, 170.0, pcbnew.Cmts_User, 0.3, True)
    add_rect(board, 181.0, 111.0, 190.0, 129.0, pcbnew.Cmts_User, 0.3, True)

    add_text(board, "UNVERIFIED LIGHTHAB FIT - DO NOT FABRICATE", 161.8, 92.5, size=1.25, thickness=0.22)
    add_text(board, "LIGHTHAB 56x75 PHOTO-DERIVED ZONE", 162.0, 97.0, pcbnew.Cmts_User, 1.25, 0.2)
    add_text(board, "COMPONENTS OUT / 18-20mm STACK", 162.0, 101.0, pcbnew.Cmts_User, 1.1, 0.18)
    add_text(board, "SMA KEEP-OUT", 153.0, 164.0, pcbnew.Cmts_User, 0.9, 0.15)
    add_text(board, "SMA KEEP-OUT", 177.0, 164.0, pcbnew.Cmts_User, 0.9, 0.15)
    add_text(board, "USB KEEP-OUT", 185.5, 120.0, pcbnew.Cmts_User, 0.9, 0.15, 90)

    # Readable functional front-silkscreen labels, outside the module body.
    add_text(board, "OPENLOG", 123.0, 94.0, size=1.25)
    add_text(board, "microSD ACCESS", 124.0, 99.0, size=0.9)
    add_text(board, "LOGGER 5V", 126.0, 129.0, size=1.0)
    add_text(board, "ACTIVITY", 125.0, 123.5, size=0.95)
    add_text(board, "CUTDOWN", 118.0, 155.0, size=1.05)
    add_text(board, "1 OUT1   2 GND", 117.0, 168.0, size=0.8)
    add_text(board, "LIGHTHAB EXTENDED PINS 1=A1", 132.5, 119.0, size=0.8, angle=90)
    add_text(board, "VBATT / GND", 132.5, 143.0, size=0.8, angle=90)
    add_text(board, "OUT1 / GND", 132.5, 156.0, size=0.8, angle=90)

    def pad(ref, number):
        return next(p for p in footprints[ref].Pads() if p.GetNumber() == str(number)).GetPosition()

    # Controlled front-layer signal and power corridors.
    route_path(board, nets["UART_TX"], pcbnew.F_Cu,
               [pad("J2", 1), (132, 109), (132, 106), pad("R4", 1)], 0.35)
    route_path(board, nets["OPENLOG_RXI"], pcbnew.F_Cu,
               [pad("R4", 2), (106.34, 106), pad("A1", 5)], 0.35)

    route_path(board, nets["3V3"], pcbnew.F_Cu,
               [pad("J2", 3), (132, 114.08), (132, 122), (108, 122), (108, 116), pad("R1", 1)], 0.35)
    route_path(board, nets["3V3"], pcbnew.F_Cu,
               [(108, 120), pad("R2", 1)], 0.35)
    route_path(board, nets["LED_A"], pcbnew.F_Cu,
               [pad("R1", 2), pad("D1", 2)], 0.35)
    route_path(board, nets["LED_N"], pcbnew.F_Cu,
               [pad("J2", 2), (130, 111.54), (130, 118), (124.5, 118), pad("D1", 1)], 0.35)
    route_path(board, nets["LED_N"], pcbnew.F_Cu,
               [(124.5, 118), (124.5, 120), pad("R2", 2)], 0.35)

    route_path(board, nets["LOGGER_5V"], pcbnew.F_Cu,
               [pad("A1", 3), (111.42, 112.5), (101.5, 112.5), (101.5, 140), pad("A2", 4)], 0.5)
    route_path(board, nets["LOGGER_5V"], pcbnew.F_Cu,
               [(101.5, 132), pad("C1", 1)], 0.5)
    route_path(board, nets["LOGGER_5V"], pcbnew.F_Cu,
               [(101.5, 138), pad("C2", 1)], 0.5)

    route_path(board, nets["VBATT"], pcbnew.F_Cu,
               [pad("J1", 1), (134, 142), (134, 145), (110.62, 145), pad("A2", 1), pad("A2", 2)], 0.8)
    route_path(board, nets["OUT1"], pcbnew.F_Cu,
               [pad("J3", 1), (140, 155), (140, 158), pad("J5", 1)], 0.8)

    # Ground owns the rear layer, so its branches may cross each other safely.
    route_path(board, nets["GND"], pcbnew.B_Cu,
               [pad("A1", 2), (113.96, 112.5), (133, 112.5), (133, 157.54), pad("J3", 2)], 0.8)
    route_path(board, nets["GND"], pcbnew.B_Cu, [pad("J2", 4), (133, 116.62)], 0.8)
    route_path(board, nets["GND"], pcbnew.B_Cu, [pad("J1", 2), (133, 144.54)], 0.8)
    route_path(board, nets["GND"], pcbnew.B_Cu, [pad("C1", 2), (133, 132)], 0.8)
    route_path(board, nets["GND"], pcbnew.B_Cu, [pad("C2", 2), (133, 138)], 0.8)
    route_path(board, nets["GND"], pcbnew.B_Cu, [pad("A2", 3), (105.54, 143), (133, 143)], 0.8)
    route_path(board, nets["GND"], pcbnew.B_Cu,
               [pad("J5", 2), (106, 161), (133, 161), (133, 157.54)], 0.8)

    pcbnew.SaveBoard(str(BOARD_PATH), board)
    print(f"wrote {BOARD_PATH}")
    print(f"parts={len(PARTS)} holes=4 nets={len(NETS)}")


if __name__ == "__main__":
    main()
