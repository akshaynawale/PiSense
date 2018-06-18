#!/usr/bin/env python3

from sense_hat import SenseHat
from display_lib import show_drop, correct_orientation, show_strip, play_music
from time import sleep
import threading
import random

def show_rain(sense)->None:
	'''
	shows rain like pattern on the display
	'''
	threads = []
	tc = threading.Thread(target=correct_orientation, args=(sense,))
	threads.append(tc)
	#tc.setDaemon(True)
	tc.start()
	ts = threading.Thread(target=play_music)
	threads.append(ts)
	ts.start()
	while True:	
		for i in range(8):
			drop_kwargs = {
				'end_position': 8,
				'sleep_before': random.uniform(0.7, 1),
				'sleep_between': random.uniform(0.05, 0.08),
				'stick_drop': True
			} 
			t = threading.Thread(target=show_drop, args=(sense, i), kwargs= drop_kwargs)
			threads.append(t)
			t.start()
		sleep(random.uniform(0.4,0.7))
def main():
	sense = SenseHat()
	sense.clear()
	show_rain(sense)

if __name__ == '__main__':
	main()
