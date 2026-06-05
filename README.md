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
| [led_status](./pico2w/led_status/) | Reusable LED state module. Runs on a separate thread so it never blocks the main program. Supports solid on, solid off, and blink modes. |


## Repo Structure

```
pi-projects/
|- pico2w/          # Raspberry Pi Pico 2 W projects
|- shared/          # Code that works across multiple devices
|- README.md
|- DOCS_STYLE_GUIDE.md
|- .gitignore
|- LICENSE
```


## Documentation

See [DOCS_STYLE_GUIDE.md](./DOCS_STYLE_GUIDE.md) for formatting and writing conventions used across this repo.


## Environment

- **Primary device:** Raspberry Pi Pico 2 W (RP2350)
- **Language:** MicroPython v1.28.0
- **OS:** macOS
- **Tool:** `mpremote`
