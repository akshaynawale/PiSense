#!/usr/bin/env python
from sense_hat import SenseHat


sense_obj = SenseHat()
red = (255,0,0)
green = (0,255,9)
blue = (0,0,255)

while True:
    sense_obj.show_message("Life is Beautiful!", text_colour=red, back_colour=green)
