# Using mpremote with the Pico 2 W on macOS

`mpremote` is a command-line tool from the MicroPython project. It replaces `screen` with something purpose-built for MicroPython development - you can open a REPL, run files, copy files to the Pico, and manage the Pico filesystem, all from your terminal.

---

## Install

```bash
pipx install mpremote
```

Verify it installed correctly:

```bash
mpremote --version
```

---

## Connect to the REPL

Plug in your Pico 2 W, then run:

```bash
mpremote connect auto repl
```

`connect auto` finds your Pico automatically - you do not need to look up the device path like you did with `screen`.

You should see:

```
MicroPython v1.28.0 on 2026-04-06; Raspberry Pi Pico 2 W with RP2350
Type "help()" for more information.
>>>
```

You are now in the MicroPython REPL. Type any MicroPython code and press `Enter` to run it.

**To exit the REPL:** press `Ctrl + X`.

---

## Run a File Without Copying It

This is useful for testing. The file runs on the Pico but is not saved there - when the Pico restarts, it is gone.

```bash
mpremote connect auto run main.py
```

Replace `main.py` with the path to your file.

---

## Copy a File to the Pico

This saves the file to the Pico's filesystem permanently.

```bash
mpremote connect auto cp main.py :main.py
```

The `:` before the filename means "on the Pico". Without it, the path refers to your Mac.

To copy multiple files:

```bash
mpremote connect auto cp led_status.py :led_status.py + cp main.py :main.py
```

---

## Make a File Run Automatically on Boot

The Pico looks for a file called `main.py` on startup and runs it automatically. Copy your file with that name:

```bash
mpremote connect auto cp my_script.py :main.py
```

From now on, that script runs every time the Pico is powered on, with no computer needed.

---

## List Files on the Pico

```bash
mpremote connect auto fs ls
```

Open the file:

```bash
mpremote connect auto fs cat :main.py
```

---

## Delete a File from the Pico

```bash
mpremote connect auto fs rm :main.py
```

---

## Common Workflow

A typical session looks like this:

1. Write or edit your code in your editor on your Mac.
2. Test it without committing:

    ```bash
    mpremote connect auto run main.py
    ```

3. When it works, copy it to the Pico:

    ```bash
    mpremote connect auto cp main.py :main.py
    ```

4. Verify it runs on boot by unplugging and replugging the Pico.

---

## Troubleshooting

### `mpremote` says device not found

- Make sure the Pico is plugged in.
- Try unplugging and replugging.
- Run `ls /dev/tty.usbmodem*` to confirm macOS can see it.
- Avoid USB hubs. Plug directly into your Mac.

### `mpremote` hangs after connecting

The Pico may be running a program that is blocking. Press `Ctrl + C` to interrupt it, then try again.

### Permission error on install

Try:

```bash
pip install mpremote --user
```

---

## Related

- [init-new-pico2w.md](./init-new-pico2w.md) - First-time Pico 2 W setup
- [MicroPython mpremote docs](https://docs.micropython.org/en/latest/reference/mpremote.html)
