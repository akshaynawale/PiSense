#!/usr/bin/env python3 

from sense_hat import SenseHat
from time import sleep
from display_lib import get_rand_color

sense = SenseHat()

#sense.show_letter('A')
sense.clear()
while True:
	sense.show_letter('A', (get_rand_color()))
	for i in range(10):
		a = sense.get_accelerometer_raw()
		x = round(a['x'],0)
		y = round(a['y'],0)
		z = round(a['z'],0)

		if x == -1:
			sense.set_rotation(90)
		elif y == -1:
			sense.set_rotation(180)
		elif x == 1:
			sense.set_rotation(270)
		else:
			sense.set_rotation(0)
		sleep(0.01)
	
