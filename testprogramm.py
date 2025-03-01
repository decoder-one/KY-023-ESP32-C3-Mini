'''
Verkabelung KY-023 mit ESP32-C3 Mini
Das KY-023 Modul hat 5 Pins:

KY-023 Pin ESP32-C3 Mini Pin Funktion
VCC 3.3V Stromversorgung
GND GND Masse
VRX GPIO 2 (ADC) X-Achse (Analog)
VRY GPIO 3 (ADC) Y-Achse (Analog)
SW GPIO 4 (Digital) Joystick-Knopf (Taster)
'''

from machine import Pin, ADC
import time

# Definiere die Pins für X, Y und den Button
x_achse = ADC(Pin(2))  # VRX -> GPIO 2 (ADC)
y_achse = ADC(Pin(3))  # VRY -> GPIO 3 (ADC)
taster = Pin(4, Pin.IN, Pin.PULL_UP)  # SW -> GPIO 4 (Taster mit Pull-Up)

# Setze die ADC-Konfiguration für eine höhere Spannung (0-3.3V)
x_achse.atten(ADC.ATTN_11DB)
y_achse.atten(ADC.ATTN_11DB)

while True:
    x_wert = x_achse.read()  # Wert von X-Achse (0-4095)
    y_wert = y_achse.read()  # Wert von Y-Achse (0-4095)
    taster_status = not taster.value()  # Umkehren (0=gedrückt, 1=nicht gedrückt)

    print(f"X: {x_wert}, Y: {y_wert}, Button: {taster_status}")

    time.sleep(0.1)  # Kleines Delay



