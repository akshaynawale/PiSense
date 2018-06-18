#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()

while True:
	temp = round(sense.get_temperature(),4)
	print('{0}'.format(temp), end='\r')
