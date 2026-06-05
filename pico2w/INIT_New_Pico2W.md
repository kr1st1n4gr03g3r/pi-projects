# Raspberry Pi Pico 2 W MicroPython Bring-Up Guide for macOS

*This guide uses macOS and Bash. It is written for beginners.*

> **Note:** The Pico 2 W does not behave like a Raspberry Pi 4 or 5. The onboard LED does not automatically turn on when the board is plugged in, turn off when unplugged, or blink while the board is "thinking."

---

## Initialize

1. Plug the Pico 2 W into your computer using a USB cable.

2. Open Terminal using Bash, then run:

    ```bash
    ls /Volumes
    ```

3. If you see `RP2350` or `RPI-RP2`, your computer can see the device. If you do not see anything new under `/Volumes`, scroll down to the Troubleshooting section below.

4. Download the latest dedicated [Pico 2 W MicroPython UF2](https://micropython.org/download/RPI_PICO2_W/). Do **not** use the Pico W or Pico 2 UF2. It must be the Pico 2 W version.

5. Copy the UF2 file to the Pico:

    ```bash
    cp path/to/file/RPI_PICO2_W-*.uf2 /Volumes/RP2350/
    ```

    Replace `*` with the actual release number in the downloaded filename.

6. After copying, the Pico should automatically reboot and the `RP2350` drive will disappear. This is expected.

7. Check for the MicroPython serial connection:

    ```bash
    ls /dev/tty.usbmodem*
    ```

    You should see something like:

    ```
    /dev/tty.usbmodem1101
    ```

    If you see:

    ```
    ls: /dev/tty.usbmodem*: No such file or directory
    ```

    then your Mac does not currently see the Pico as a MicroPython serial device. See Troubleshooting below.

8. Open the MicroPython REPL using `screen`. Use the exact device path from Step 7:

    ```bash
    screen /dev/tty.usbmodem1101 115200
    ```

    Replace `/dev/tty.usbmodem1101` with whatever your terminal actually showed.

    If it opens successfully, you may see a blank screen. Press `Enter` once or twice. You should see:

    ```
    >>>
    ```

    That `>>>` prompt means you are now inside MicroPython on the Pico 2 W.

9. Test the onboard LED. At the `>>>` prompt, enter each line one at a time:

    ```python
    from machine import Pin
    led = Pin("LED", Pin.OUT)
    led.on()
    ```

    The onboard LED should turn on. Then:

    ```python
    led.off()
    ```

    The onboard LED should turn off.

10. Exit the `screen` session by pressing these keys in order:

    - Hold `Ctrl` and press `A`, then release both keys
    - Press `K`
    - Press `Y`

    You should return to your normal terminal prompt, for example:

    ```
    bash-3.2$
    ```

---

## Troubleshooting

### Problem: `ls /dev/tty.usbmodem*` says no such file or directory

Example:

```bash
bash-3.2$ ls /dev/tty.usbmodem*
ls: /dev/tty.usbmodem*: No such file or directory
```

This means macOS does not currently see the Pico as a MicroPython serial device. Check whether the Pico appears as a USB drive instead:

- Unplug the Pico.
- Hold the `BOOTSEL` button on the Pico.
- While holding `BOOTSEL`, plug the Pico into USB.
- Release `BOOTSEL`.
- Run:

    ```bash
    ls /Volumes
    ```

    If you see `RP2350`, the Pico is alive and in bootloader mode.

For a Pico 2 W, download the dedicated Pico 2 W MicroPython UF2 from:

```
https://micropython.org/download/RPI_PICO2_W/
```

Then copy the `.uf2` file to the Pico:

```bash
cp path/to/file/RPI_PICO2_W-*.uf2 /Volumes/RP2350/
```

After copying, the Pico should automatically reboot and the `RP2350` drive will disappear. macOS may show a "Disk Not Ejected Properly" warning. That is expected - the Pico rebooted itself after receiving the UF2 file.

After that, unplug and replug the Pico normally, without holding `BOOTSEL`, then run:

```bash
ls /dev/tty.usbmodem*
```

---

### Problem: `screen` immediately exits

Example:

```bash
bash-3.2$ screen /dev/tty.usbmodem1101 115200
[screen is terminating]
bash-3.2$
```

This usually means the device path is wrong, stale, or no longer available. Run this again:

```bash
ls /dev/tty.usbmodem*
```

Use the exact current value it prints. For example, if it prints:

```
/dev/tty.usbmodem14201
```

then connect using:

```bash
screen /dev/tty.usbmodem14201 115200
```

Do not assume it will always be `/dev/tty.usbmodem1101`. The number can change.

You can also check the `cu` device path:

```bash
ls /dev/cu.usbmodem*
```

If that prints something like `/dev/cu.usbmodem14201`, you can try:

```bash
screen /dev/cu.usbmodem14201 115200
```

---

### Problem: `screen` opens but the screen is blank

- Press `Enter` once or twice.
- If MicroPython is running, you should see `>>>`.
- If you still see nothing, exit `screen` with `Ctrl + A`, then `K`, then `Y`.
- Unplug and replug the Pico normally, without holding `BOOTSEL`, and try again:

    ```bash
    ls /dev/tty.usbmodem*
    ```

    Then:

    ```bash
    screen /dev/tty.usbmodemXXXX 115200
    ```

    Replace `usbmodemXXXX` with the actual value from your terminal.

---

### Problem: I am stuck inside `screen`

To exit, press `Ctrl + A`, then `K`, then `Y`.

If that does not work, try `Ctrl + A`, then `\`, then `Y`.

If you are running code in MicroPython and it will not stop, press `Ctrl + C`. That interrupts the running program and returns you to:

```
>>>
```

Then exit `screen` with `Ctrl + A`, then `K`, then `Y`.

---

### Problem: The Pico shows `RP2350` but not `/dev/tty.usbmodem*`

If the Pico shows up as `RP2350`, it is in bootloader mode, not normal MicroPython mode. This can happen when:

- You are holding `BOOTSEL` while plugging it in
- MicroPython has not been installed yet
- The UF2 copy did not complete correctly
- The wrong UF2 file was copied

For Pico 2 W, make sure the UF2 is specifically for `RPI_PICO2_W`, not `RPI_PICO_W`, `RPI_PICO2`, or `RPI_PICO`.

After copying the correct UF2, unplug and replug the Pico normally, without holding `BOOTSEL`, then check again:

```bash
ls /dev/tty.usbmodem*
```

---

### Problem: The computer does not see the Pico at all

If the Pico does not appear under `/Volumes` and does not appear under `/dev/tty.usbmodem*`, check the following:

- Try another USB cable. Some cables are power-only and do not carry data.
- Try another USB port.
- Avoid USB hubs while testing. Plug directly into the computer.
- Confirm the Pico is seated normally and not shorting against anything on a breadboard.
- Less likely but possible: the Pico 2 W itself could be faulty.
