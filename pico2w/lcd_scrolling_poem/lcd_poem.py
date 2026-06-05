import time

from machine import Pin

RS = Pin(2, Pin.OUT)
E = Pin(3, Pin.OUT)
D4 = Pin(4, Pin.OUT)
D5 = Pin(5, Pin.OUT)
D6 = Pin(6, Pin.OUT)
D7 = Pin(7, Pin.OUT)


def pulse():
    E.value(1)
    time.sleep_us(1)
    E.value(0)
    time.sleep_us(50)


def write4(nibble):
    D4.value((nibble >> 0) & 1)
    D5.value((nibble >> 1) & 1)
    D6.value((nibble >> 2) & 1)
    D7.value((nibble >> 3) & 1)
    pulse()


def send(val, mode):
    RS.value(mode)
    write4(val >> 4)
    write4(val & 0x0F)
    time.sleep_us(50)


def cmd(c):
    send(c, 0)


def char(c):
    send(ord(c), 1)


def init():
    time.sleep_ms(50)
    RS.value(0)
    write4(0x03)
    time.sleep_ms(5)
    write4(0x03)
    time.sleep_us(150)
    write4(0x03)
    time.sleep_us(150)
    write4(0x02)
    cmd(0x28)
    cmd(0x0C)
    cmd(0x06)
    cmd(0x01)
    time.sleep_ms(2)


def cursor(col, row):
    cmd(0x80 | ([0x00, 0x40][row] + col))


def print_at(text, col, row):
    cursor(col, row)
    for c in text:
        char(c)


init()

print_at("   - Havamal    ", 0, 1)

poem = "Cattle die, kinsmen die, the self must also die; but glory never dies."
padded = " " * 16 + poem + " " * 16

while True:
    for i in range(len(padded) - 15):
        print_at(padded[i : i + 16], 0, 0)
        time.sleep_ms(300)
