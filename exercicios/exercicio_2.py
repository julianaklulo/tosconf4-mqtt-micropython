"""
Exercício 2: Potenciômetro.
"""
from machine import Pin, ADC
from time import sleep

POT_PIN = ADC(Pin(34))

while True:
    value = POT_PIN.read_u16()
    print(f"Valor: {value}")
    sleep(0.5)
