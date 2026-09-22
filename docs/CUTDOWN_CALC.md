# Cutdown interface status

The earlier carrier MOSFET/driver calculation is obsolete. LightHABTracker 1.0 now owns cutdown switching and timing. The carrier only routes LightHAB OUT1/GND from J3 to the soldered JST-XH J5 connector.

No safe nichrome current, resistance, gauge, length, or pulse duration can be released from the present public information. Before connecting a burn wire:

1. obtain an authoritative LightHAB OUT1 voltage/current/duty rating or characterize it with a fuse, current-limited source, oscilloscope, and inert loads;
2. confirm which battery rail feeds OUT1 and its worst-case cold/end-of-discharge voltage;
3. measure connector, harness, and contact drop and temperature;
4. select nichrome resistance and pulse time within the verified envelope with margin;
5. use a mechanical crimp sleeve for nichrome-to-copper joining rather than relying on ordinary solder;
6. test reset, brownout, bootloader, and firmware failure cases before any live burn test.

Until those measurements exist, J5 is a provisional pass-through and not a qualified cutdown source.
