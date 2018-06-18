#!/usr/bin/env python3
import sys
import time


output_stream = sys.stdout

for i in range(10):
	output_stream.write("update {0}\r".format(i))
	output_stream.flush() 
	time.sleep(1)
output_stream.write('\n')   
