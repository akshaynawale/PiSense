#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep
import sys

#output_stream = sys.stdout
sense = SenseHat()
while True:
	o = sense.get_orientation()
	print('pitch {0} roll {1} yaw {2}'.format(round(o['pitch'],2), round(o['roll'],2), round(o['yaw'],2)), end='\r')
	#output_stream.write("pitch {0}\r roll {1}\r yaw {2}\r".format(o["pitch"], o['roll'], o['yaw']))
	#output_stream.flush()
	sleep(0.5)
#output_stream.write('\n')
