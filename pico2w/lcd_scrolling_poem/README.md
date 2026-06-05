# lcd_scrolling_poem

1602A LCD display connected to the Pico 2 W. Scrolls a stanza from Hávamál across line 1. Line 2 shows a static attribution. Written with a raw 4-bit HD44780 driver — no external library.

---

## Hardware

- Raspberry Pi Pico 2 W
- 1602A LCD display (HD44780 controller)
- 100Ω resistor (backlight current limiting)
- Breadboard and jumper wires

---

## Requirements

- MicroPython v1.28.0 or later
- Built-in modules: `machine`, `time`

---

## Pin Wiring

| LCD Pin | Connects to | Notes |
|---|---|---|
| VSS | GND | |
| VDD | VBUS (5V) | |
| VO | GND | Max contrast. A potentiometer here gives adjustable contrast. |
| RS | GP2 | |
| RW | GND | Write-only — never reads from display. |
| E | GP3 | |
| D0–D3 | not connected | 4-bit mode only uses D4–D7. |
| D4 | GP4 | |
| D5 | GP5 | |
| D6 | GP6 | |
| D7 | GP7 | |
| A | VBUS via 100Ω | Backlight anode. Higher resistance = dimmer. |
| K | GND | Backlight cathode. |

See `lcd_scrolling_poem.json` for the full Wokwi diagram and `lcd_scrolling_poem.png` for a reference screenshot.

---

## Usage

Copy `lcd_poem.py` to the Pico:

```bash
mpremote connect auto cp lcd_poem.py :lcd_poem.py
```

The display starts scrolling on power-up.

> **Note:** This overwrites `lcd_poem.py` on the Pico. If you have another boot script running, back it up first.

---

## How It Works

The HD44780 is driven in 4-bit mode using six GPIO pins (RS, E, D4–D7). RW is tied permanently to GND. The init sequence follows the HD44780 datasheet power-on procedure.

The poem text is padded with spaces on both ends, then a 16-character window slides through it one position at a time, updating every 300ms.

---

## Notes

- Scroll speed is set by `time.sleep_ms(300)` at the bottom of `lcd_poem.py`. Increase the value to slow it down.
- VO tied to GND gives maximum contrast. If the display looks washed out or too dark, a 10kΩ potentiometer on VO lets you tune it.
- Backlight brightness is fixed by the 100Ω resistor. Swap for a higher value to dim it.

---

## Related

- [hardware_checks](../hardware_checks/) — LCD power verification test
- [init-new-pico2w.md](../init-new-pico2w.md) — First-time Pico 2 W setup
- [mpremote.md](../mpremote.md) — File transfer reference
