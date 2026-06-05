# pi-projects

```
        )   (
       (     )
    __..---..__
,-='  /  |  \  `=-.
:--..___________..--;
 \.,_____________,./
```

Personal monorepo for hardware tinkering and invention. Projects are organized by device and written in MicroPython or Python.

## Projects

### Pico 2 W

| Project | Description |
|---|---|
| [lcd_scrolling_poem](./pico2w/lcd_scrolling_poem/) | 1602A LCD display scrolling a Hávamál stanza. Raw 4-bit HD44780 driver, no external library. |
| [led_status](./pico2w/led_status/) | Reusable onboard LED state module. Runs on a separate thread so it never blocks the main program. Supports solid on, solid off, and blink modes. |
| [hardware_checks](./pico2w/hardware_checks/) | Component go/no-go tests. Run before building a project to confirm hardware is alive. |
| [init-new-pico2w](./pico2w/init-new-pico2w.md) | First-time setup guide for the Pico 2 W on macOS. Covers MicroPython firmware install, serial connection, and onboard LED verification. |
| [mpremote](./pico2w/mpremote.md) | Command reference for `mpremote` on macOS. Covers install, REPL, file management, and common troubleshooting. |
 

## Repo Structure

```
pi-projects/
|- pico2w/                   # Raspberry Pi Pico 2 W
|  |- hardware_checks/       # Component go/no-go tests
|  |- lcd_scrolling_poem/    # 1602A LCD scrolling display
|  |- led_status/            # Onboard LED state module
|  |- init-new-pico2w.md
|  |- main.py                # Boot script: onboard LED on at power-up
|  |- mpremote.md
|- README.md
|- DOCS_STYLE_GUIDE.md
|- TEMPLATE.md
|- .gitignore
|- LICENSE
```


## Documentation

See [DOCS_STYLE_GUIDE.md](./DOCS_STYLE_GUIDE.md) for formatting and writing conventions used across this repo. Use [TEMPLATE.md](./TEMPLATE.md) for new projects or instructions.


## Environment

- **Primary device:** Raspberry Pi Pico 2 W (RP2350)
- **Language:** MicroPython v1.28.0
- **OS:** macOS
- **Tool:** `mpremote`
