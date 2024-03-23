"""
Exercício 1.1: Blink do MicroPython.
"""
from machine import Pin
from time import sleep


LED_PIN = Pin(4, Pin.OUT)

while True:
    LED_PIN.value(1)
    sleep(0.5)
    LED_PIN.value(0)
    sleep(0.5)
