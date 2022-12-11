import plasma
from plasma import plasma_stick
import time

"""
Make some rainbows!
"""

# list of leds to switch on
onLeds = [251,244,235,228,216,217,218,219,220,221,222,212,203,196,187,40,41,42,43,44,45,46,39,38,37,36,35,34,33,24,25,26,27,28,29,30,23,22,21,20,19,18,17,8,9,10,11,12,13,14,7,6,5,4,3,2,1,71,70,69,68,67,66,65,56,57,58,59,60,61,62,55,54,53,52,51,50,49,105,106,107,108,109,103,97,88,94,86,85,84,83,82,169,170,171,172,173,167,161,152,158,150,149,148,147,146,133,131]
# [9,10,11,50,51,52,53,61,66,67,68,69,77,82,83,84,85,93,95,98,99,100,101,103,109,111,113,114,115,116,117,118,119,125,127,130,131,132,133,135,141,143,146,147,148,149,157,162,163,164,165,173,178,179,180,181]
enFlagWhite = [248,249,250,252,253,254,247,246,245,243,242,241,232,233,234,236,237,238,231,230,229,227,226,225,215,214,213,211,210,209,200,201,202,204,205,206,199,198,197,195,194,193,184,185,186,188,189,190]
enFlagRed = [251,244,235,228,216,217,218,219,220,221,222,212,203,196,187]
frFlagWhite = [40,41,42,43,44,45,46,39,38,37,36,35,34,33,24,25,26,27,28,29,30]
frFlagRed = [23,22,21,20,19,18,17,8,9,10,11,12,13,14,7,6,5,4,3,2,1]
frFlagBlue = [71,70,69,68,67,66,65,56,57,58,59,60,61,62,55,54,53,52,51,50,49]
maFlagRed = [248,249,250,251,252,253,254,247,246,245,244,243,242,241,232,233,235,236,237,238,231,230,228,226,225,216,220,221,222,215,214,212,210,209,200,201,203,204,205,206,199,198,197,196,195,194,193,184,185,186,187,188,189,190]
maFlagGreen = [234,229,227,217,218,219,213,211,202]
colon = [133,131]

zeroen = [169,170,171,172,173,167,161,152,158,150,149,148,147,146]
oneen = [170,166,152,153,154,155,156,157,158]
zerofr = [105,106,107,108,109,103,97,88,94,86,85,84,83,82]
onefr = [101,89,87,86,85,84,83,82,81]
twofr = [105,108,109,110,103,100,97,88,90,94,86,81]
twoen = [166,163,162,161,152,155,158,151,149,145,137,142]
threeen = [166,162,152,155,158,151,148,145,137,138,140,141]
threefr = [105,109,103,100,97,88,91,94,86,85,83,82]

frScore = zerofr
enScore = zeroen

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


def colour(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((R&0b11111000)>>3)<<8) + (B&0b11111000)+((G&0b11100000)>>5)

#  colours from https://thepihut.com/blogs/raspberry-pi-tutorials/coding-colour-with-micropython-on-raspberry-pi-pico-displays
red = 0.3#colour(255, 0, 0)# is bright red
green = 0.1#colour(0, 255, 0)# is bright green
blue = 0.6#colour(0, 0, 127)# is half-power blue
yellow = 0.15#colour(255, 255, 0)# Red + Green
# cyan = 0.8#colour(0, 255, 255)# Green + Blue
# magenta = 0.9#colour(255, 0, 255)# Red + Blue
white = 0.0#colour(255, 255 ,255)# Red + Green + Blue
midgrey = 0.1#(127, 127, 127)# Half brightness of white


def lightUp(ledArray, color, offset):
    # function body 

    for i in range(len(ledArray)):
        hue = float(i) / len(ledArray)
        led_strip.set_hsv(ledArray[i], color, offset, 0.9)
        
    return

# Make rainbows
while True:

    SPEED = min(255, max(1, SPEED))
    offset += float(SPEED) / 2000.0

    lightUp(maFlagGreen, green, 1.0)
    lightUp(maFlagRed, red, 1.0)
    lightUp(frFlagWhite, yellow, 0.0)
    lightUp(frFlagRed, red, 1.0)
    lightUp(frFlagBlue, blue, 1.0)
    lightUp(frScore, green, 1.0)
    lightUp(enScore, green, 1.0)
    lightUp(colon, green, 1.0)

    time.sleep(1.0 / UPDATES)
