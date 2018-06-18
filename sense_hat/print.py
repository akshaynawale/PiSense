#!/usr/bin/env python3

import time

for i in range(10):
	print("update %d" %i, end='\r')
	time.sleep(1)
