from machine import Pin
import time

BUTTON_PIN = 4

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("занято")
    else:
        print("свободно")

    time.sleep_ms(200)
