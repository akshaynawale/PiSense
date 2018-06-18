#!/usr/bin/env python3
import pygame
from sense_hat import SenseHat
from time import sleep
pygame.init()
pygame.mixer.music.load('/home/pi/Documents/sense_hat/Yu.mp3')
pygame.mixer.music.play()

e = (0,0,0)
p = (255,20,147)
g = (0,255,0)
y = (255,255,0)
w = (255,255,255)


cat1 = [
	e,e,e,e,e,e,e,e,
	p,e,e,e,e,e,e,e,
	e,p,e,e,p,e,p,e,
	e,p,g,g,p,y,y,e,
	e,g,g,g,y,w,y,g,
	e,g,g,g,g,y,y,e,
	e,g,e,g,e,g,e,e,
	e,e,e,e,e,e,e,e,
]

cat2 = [

	e,e,e,e,e,e,e,e,
	p,e,e,e,e,e,e,e,
	e,p,e,e,p,e,p,e,
	e,p,g,g,p,y,y,e,
	e,g,g,g,y,w,y,g,
	e,g,g,g,g,y,y,e,
	e,e,g,e,g,e,e,e,
	e,e,e,e,e,e,e,e
]


sense = SenseHat()

def set_position(sense)->None:
	a = sense.get_accelerometer_raw()
	x = round(a['x'], 0)
	y = round(a['y'], 0)
	z = round(a['z'], 0)
	
	if x == -1:
		sense.set_rotation(90)
	elif y == -1:
		sense.set_rotation(180)
	elif x == 1:
		sense.set_rotation(270)
	else:
		sense.set_rotation(0)

for i in range(360):
	set_position(sense)
	sense.set_pixels(cat1)
	sleep(0.5)
	set_position(sense)
	sense.set_pixels(cat2)
	sleep(0.5)
sense.clear()

