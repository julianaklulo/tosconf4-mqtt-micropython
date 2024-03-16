"""
Exercício 2: Fade do MicroPython.
"""
from machine import Pin, PWM
from time import sleep

LED_PIN = PWM(Pin(16))

min = 0
max = 65535

while True:
    for i in range(min, max + 1):
        LED_PIN.dutu_u16(i)
        sleep(0.1)

    for i in range(max, min - 1, -1):
        LED_PIN.dutu_u16(i)
        sleep(0.1)
