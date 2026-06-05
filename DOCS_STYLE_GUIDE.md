# Documentation Style Guide

This guide defines how documentation is written across this repo. Following it consistently makes the repo easier to navigate, easier to read, and portfolio-ready.

---

## General Principles

- Write for your future self first. Assume you will not remember why you made a decision.
- Write in plain English. No jargon unless it is defined or linked.
- Shorter is better. If a sentence can be cut without losing meaning, cut it.
- Every folder that contains a project gets a `README.md`. No exceptions.

---

## File Naming

| File | Purpose |
|---|---|
| `README.md` | Required in every project folder. Describes what the project does. |
| `SETUP.md` | Optional. Step-by-step bring-up or install instructions, if too long for the README. |
| `NOTES.md` | Optional. Informal scratchpad for observations, gotchas, or things to revisit. |
| `DOCS_STYLE_GUIDE.md` | This file. Lives at repo root. |

Rules:

- Filenames use lowercase with hyphens, except for conventional all-caps files like `README.md`, `LICENSE`, and `DOCS_STYLE_GUIDE.md`.
- No spaces in filenames.
- MicroPython module files use lowercase with underscores: `led_status.py`, `main.py`.

---

## Folder Structure

```
pi-projects/
|- pico2w/
|  |- led_status/
|  |  |- led_status.py
|  |  |- README.md
|  |- some-other-project/
|  |  |- main.py
|  |  |- README.md
|- shared/
|  |- README.md
|- README.md
|- DOCS_STYLE_GUIDE.md
|- .gitignore
|- LICENSE
```

- Device folders at root level: `pico2w/`, `pi4/`, `pi-zero/`, etc.
- Each project lives in its own subfolder under the device folder.
- `shared/` is for code that works across multiple device types without modification.

---

## Markdown Formatting

### Headings

- Use `#` for the document title. One per file.
- Use `##` for major sections.
- Use `###` for subsections.
- Do not skip levels. Do not use `####` unless there is a clear reason.
- No period at the end of a heading.

### Lists

- Use `-` for all unordered lists. Never `*`.
- Use numbered lists only for sequential steps where order matters.
- Keep list items parallel in structure. If one item starts with a verb, they all should.
- Nested lists are fine up to two levels. Beyond that, break it into sections.

### Code

- Always use fenced code blocks. Never inline backticks for multi-line content.
- Always specify the language for syntax highlighting:

    ````
    ```bash
    mpremote connect auto run main.py
    ```
    ````

    ````
    ```python
    led.on()
    ```
    ````

- Use plain fenced blocks with no language tag for terminal output, file paths, and prompts:

    ````
    ```
    /dev/tty.usbmodem1101
    ```
    ````

- Use inline backticks for: file names, folder names, commands, key names, and short values mentioned in a sentence.

    Examples:
    - Copy the file to `led_status.py`.
    - Run `mpremote` to connect.
    - Press `Ctrl + C` to interrupt.

### Key Combinations

Write keyboard shortcuts in inline backticks with `+` between keys:

- `Ctrl + C`
- `Ctrl + A`, then `K`, then `Y`

Do not write: `^C`, `Ctrl+C` (no spaces), or `CTRL + C` (all caps).

### Bold and Italic

- Use **bold** for warnings, important terms on first use, or UI labels.
- Use *italic* for light emphasis or document subtitles.
- Do not use bold for decoration. If everything is bold, nothing is.

### Horizontal Rules

Use `---` to separate major sections in longer documents. Do not overuse them in short files.

### Tables

Use tables for structured comparisons or reference data. Always include a header row. Align the pipes for readability in source:

```markdown
| Column A | Column B |
|---|---|
| Value    | Value    |
```

### Notes and Warnings

Use a blockquote with a bold label for callouts:

```markdown
> **Note:** The Pico 2 W does not behave like a Raspberry Pi 4 or 5.
```

```markdown
> **Warning:** Do not use the Pico W UF2. It must be the Pico 2 W version.
```

---

## Voice and Tone

- Write in second person: "Run this command", not "The user should run this command."
- Use active voice. "Copy the file" not "The file should be copied."
- Use present tense. "The LED turns on" not "The LED will turn on."
- Contractions are fine. "You'll see" is more readable than "You will see."
- Do not use filler phrases: "simply", "just", "easily", "straightforward", "basically."

---

## README Structure

Every project README should follow this structure. Omit sections that genuinely do not apply.

```markdown
# Project Name

One or two sentences describing what this does and why it exists.

## Hardware

- Raspberry Pi Pico 2 W
- [Any other components]

## Requirements

- MicroPython v1.x or later
- [Any libraries or tools]

## Usage

How to run or deploy it. Keep this short.

## Notes

Anything worth knowing that did not fit above. Gotchas, known issues, future ideas.
```

---

## Device Name Conventions

| Device | Write it as |
|---|---|
| Raspberry Pi Pico 2 W | Pico 2 W |
| Raspberry Pi Pico W | Pico W |
| Raspberry Pi Pico 2 | Pico 2 |
| Raspberry Pi Pico | Pico |
| Raspberry Pi 4 | Pi 4 |
| Raspberry Pi 5 | Pi 5 |
| Raspberry Pi Zero 2 W | Pi Zero 2 W |

- Match product names exactly on first mention in a document.
- Shortened forms are fine after first use.
- Never write `PicoW`, `Pico2W`, or `RPI` in prose. Those are for folder names and file paths only.

---

## What Not to Commit

The `.gitignore` covers these, but as a rule:

- No compiled MicroPython bytecode: `*.mpy`
- No `boot_out.txt`
- No `__pycache__/`
- No `.env` files or files containing credentials or tokens
- No OS junk: `.DS_Store`

---

## Tagging

Tag a project folder when it reaches a known-good state:

```bash
git tag pico2w-led-status-v1
git push origin --tags
```

Tag names follow the pattern: `<device>-<project>-v<number>`.

---

## A Note on This Repo

This is a personal monorepo for tinkering and invention. The documentation standard here is not corporate - it is consistent, honest, and clear. The goal is that any project in this repo could be picked up and understood by someone with basic technical knowledge, including future you.
