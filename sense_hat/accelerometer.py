#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
	a = sense.get_accelerometer_raw()
	a = {
			'x': round(a['x'],0), 
			'y': round(a['y'],0),
			'z': round(a['z'],0)
		}
	print(a, end = '\r')
	sleep(0.01)
