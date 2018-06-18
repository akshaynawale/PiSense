#!/usr/bin/env python3

from sense_hat import SenseHat
from display_lib import show_message 
from time import sleep
from typing import Dict


back_color = (0,0,0)
text_color = (255,255,255)

data = {}
sense_obj = SenseHat()
data['pres:'] = str(round(sense_obj.get_pressure(), 2))
data['temp:'] = str(round(sense_obj.get_temperature(),2))
data['humi:'] = str(round(sense_obj.get_humidity(), 2))
sense_obj.set_rotation(180)
for k, v in data.items():
    show_message(sense_obj, k, text_color, back_color)
    show_message(sense_obj, v, text_color, back_color)
sense_obj.clear()
print(data)
