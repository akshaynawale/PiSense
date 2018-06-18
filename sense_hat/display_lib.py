#!/usr/bin/env python3

import pygame
import random
import time
import threading
from typing import List, Tuple


#Default colors
def_text_color = (255,0,0)
def_back_color = (0,255,0)


def get_color(sense, color_tuple: (int, int, int), sec)->None:
    '''
    Display color for the specified time 
    takes 1. sense hat object
    2. color tuple
    3. time in seconds
    '''
    sense.clear((color_tuple))
    print('waiting for {0} seconds'.format(sec))
    time.sleep(sec)
    sense.clear((0,0,0))


def get_rand_color()->(int, int, int):
    '''
    Generate random colors
    ''' 
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return red, green, blue

def set_color(sense, color_tuple: (int, int, int), sec)->None:
    '''
    Display color for the specified time 
    takes 1. sense hat object
    2. color tuple
    3. time in seconds
    '''
    sense.clear((color_tuple))
    print('waiting for {0} seconds'.format(sec))
    time.sleep(sec)
    sense.clear((0,0,0))


def get_rand_color()->(int, int, int):
    '''
    Generate random colors
    ''' 
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return red, green, blue

def set_image(sense_obj, matrix: List[Tuple[int, int, int]])->None:
    '''
    Sets the image on the display
    '''
    sense_obj.set_pixels(matrix)

def show_message(sense_obj, msg:str, text_color=def_text_color, back_color=def_back_color)->None:
    '''
    shows messages on the display
    '''
    sense_obj.show_message(msg, text_colour=text_color, back_colour=back_color)

def show_drop(
	sense_obj, 
	row:int, 
	color:Tuple[int,int,int]=None, 
	sleep_before:float=None, 
	sleep_between:float=None,
	start_position:int = 0,
	end_position:int = 8,
	stick_drop: bool = False,
)->None:
	'''
	Display a rain drop on sense hat display
	'''
	if not sleep_before:
		sleep_before = random.uniform(0.1,0.9)
	if not sleep_between:
		sleep_between = random.uniform(0.05, 0.15)
	if not color:
		color = (get_rand_color())
	time.sleep(sleep_before)
	stick_position = end_position -1
	for i in range(start_position, end_position):
		sense_obj.set_pixel(row, i, color)
		time.sleep(sleep_between)
		if stick_drop and (i == stick_position):
			continue
		else:	
			sense_obj.set_pixel(row, i, (0,0,0))

def correct_orientation(sense_obj)->None:
	'''
	Change the display orientation on basis of how the pi is held
	'''
	while True:	
		a = sense_obj.get_accelerometer_raw()
		x = round(a['x'], 0)
		y = round(a['y'], 0)
		if x == -1:
			sense_obj.set_rotation(90)
		elif y == -1:
			sense_obj.set_rotation(180)
		elif x == 1:
			sense_obj.set_rotation(270)
		else:
			sense_obj.set_rotation(0)
		time.sleep(0.2)


def show_strip(sense_obj, row: int=0, vertical: bool=False)->None:
	'''
	shows a line with sparkling color strip
	'''
	while True:
		position = random.randint(0,7)
		if not vertical:
			sense_obj.set_pixel(row, position, (get_rand_color()))
		else:
			sense_obj.set_pixel(position, row, (get_rand_color()))
		time.sleep(0.2)
		
def play_music(file_path:str=None)->None:
	'''
	Plays music if path nor given then plays one track from list randomly.
	'''
	pygame.init()
	pygame.mixer.music.load('/home/pi/Documents/sense_hat/rain.mp3')
	pygame.mixer.music.play(loops=-1)

if __name__ == "__main__":
    main()
