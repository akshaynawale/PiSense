#!/usr/bin/env python3
from sense_hat import SenseHat
from time import sleep
from display_lib import set_image
sense = SenseHat()

# Define some colours

B = (102, 51, 0)

b = (0, 0, 255)

S = (205,133,63)

W = (255, 255, 255)




# Define some colours

g = (0, 255, 0) # Green

b = (0, 0, 0) # Black

# Set up where each colour will display

steve_pixels = [

    B, B, B, B, B, B, B, B,

    B, B, B, B, B, B, B, B,

    B, S, S, S, S, S, S, B,

    S, S, S, S, S, S, S, S,

    S, W, b, S, S, b, W, S,

    S, S, S, B, B, S, S, S,

    S, S, B, S, S, B, S, S,

    S, S, B, B, B, B, S, S

]

creeper_pixels = [

    g, g, g, g, g, g, g, g,

    g, g, g, g, g, g, g, g,

    g, b, b, g, g, b, b, g,

    g, b, b, g, g, b, b, g,

    g, g, g, b, b, g, g, g,

    g, g, b, b, b, b, g, g,

    g, g, b, b, b, b, g, g,

    g, g, b, g, g, b, g, g

]


# Display these colours on the LED matrix

set_image(sense, creeper_pixels)

sleep(2)
sense.set_rotation(90)
sleep(2)
sense.set_rotation(180)
sleep(2)
sense.clear()
