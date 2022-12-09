import plasma
from plasma import plasma_stick
import time

"""
Make some rainbows!
"""

# list of leds to switch on
onLeds = [170,171,172,173,162,154,155,156,157,146,138,139,140,141,130,128,122,123,124,125,127,114,112,105,106,107,108,109,110,111,98,96,90,91,92,93,95,82,80,74,75,76,77,66,58,59,60,61,50,42,43,44,45];

# Set how many LEDs you have
NUM_LEDS = len(onLeds)
NUM_LEDS2 = 32*8

# The SPEED that the LEDs cycle at (1 - 255)
SPEED = 20

# How many times the LEDs will be updated per second
UPDATES = 60

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS2, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# Start updating the LED strip
led_strip.start()

offset = 0.0

# Make rainbows
while True:

    SPEED = min(255, max(1, SPEED))
    offset += float(SPEED) / 2000.0

    for i in range(NUM_LEDS):
        hue = float(i) / NUM_LEDS
        led_strip.set_hsv(onLeds[i], hue + offset, 1.0, 1.0)

    time.sleep(1.0 / UPDATES)


