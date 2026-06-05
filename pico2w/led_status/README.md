# led_status

Reusable LED state module for the Pico 2 W. Runs on a separate thread so it never blocks the main program. Supports solid on, solid off, and blink modes.

---

## Hardware

- Raspberry Pi Pico 2 W (uses onboard LED — no external components needed)

---

## Requirements

- MicroPython v1.28.0 or later
- Built-in modules: `machine`, `time`, `_thread`

---

## Usage

Copy the module to the Pico:

```bash
mpremote connect auto cp led_status.py :led_status.py
```

Import and use `set_led()` in your program:

```python
import led_status

led_status.set_led("on")     # solid on
led_status.set_led("blink")  # blink at 4 Hz
led_status.set_led("off")    # solid off
```

> **Note:** The LED thread starts automatically when you import the module. You do not need to call any init function.

---

## How It Works

The module starts a background thread (`_led_thread`) on import. That thread loops continuously, reading `_led_mode` and driving the LED accordingly. Your main program calls `set_led()` to update the mode — no blocking, no timing logic needed in your code.

Blink speed is controlled by `_blink_hz` (default: 4 blinks per second). Edit that value directly in the file if you want a different rate.

The bottom section of `led_status.py` is a usage demo — replace it with your actual program.

---

## Notes

- Only one LED mode is active at a time. Calling `set_led()` is an instant switch.
- The thread runs for the lifetime of the program. There is no stop mechanism.

---

## Related

- [init-new-pico2w.md](../init-new-pico2w.md) — First-time Pico 2 W setup
- [mpremote.md](../mpremote.md) — File transfer and REPL reference
