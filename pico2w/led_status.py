import machine
import time
import _thread

led = machine.Pin("LED", machine.Pin.OUT)

# --- LED state machine ---
# Modes: "on", "off", "blink"
_led_mode = "on"
_blink_hz = 4  # blinks per second when processing

def _led_thread():
    while True:
        if _led_mode == "on":
            led.on()
            time.sleep_ms(50)
        elif _led_mode == "off":
            led.off()
            time.sleep_ms(50)
        elif _led_mode == "blink":
            led.toggle()
            time.sleep_ms(int(500 / _blink_hz))

def set_led(mode):
    global _led_mode
    _led_mode = mode

# Start LED thread - runs independently of your main program
_thread.start_new_thread(_led_thread, ())

# --- Your actual program below ---
set_led("on")   # powered = LED solid on

# Simulate a processing task
while True:
    set_led("blink")     # processing = blink
    time.sleep(3)        # your work happens here
    set_led("on")        # done = back to solid
    time.sleep(2)
