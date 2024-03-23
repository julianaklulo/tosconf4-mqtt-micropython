"""
Exercício 1.2: Fade do MicroPython.
"""
from machine import Pin, PWM
from time import sleep


LED_PIN = PWM(Pin(4))
MIN = 0
MAX = 65535

while True:
    for i in range(MIN, MAX + 1):
        LED_PIN.duty_u16(i)
        sleep(0.1)

    for i in range(MAX, MIN - 1, -1):
        LED_PIN.duty_u16(i)
        sleep(0.1)
