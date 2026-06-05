# Simple Test for New Pico

*This test uses Mac / BASH*

1. Plug USB into Pico 2W from your computer
2. Open BASH, `ls /Volumes`
3. If you see `RP2350` or `RPI-RP2`, your computer can see the device. If you do **not** see anything new under `/Volumes`, check:
  - USB cable - try another one
  - USB cable - make sure it's a data cable. The device often comes with a data cable, but if not it could be a power-only USB cable
  - USB adapter or hub issue - try plugging it into a different usb port on your computer
  - Less likely, but possible Pico2W is a dud
4. 

>>> from machine import Pin
>>> led = Pin("LED", Pin.OUT)
>>> led.on()
>>> led.off()
