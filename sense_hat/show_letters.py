#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep
import random
from display_lib import get_rand_color

def display_letter(sense_obj, letter:str, color)->None:
    '''
    Display word on the sense hat
    '''
    sense_obj.show_letter(letter, color)

def clear_display(sense_obj)->None:
    """
    clear sense hat display
    """
    sense_obj.clear()

def main():
    sense_obj = SenseHat()
    Message = "Akshay Navale"
    for i in Message:
        display_letter(sense_obj, i, get_rand_color())
        sleep(0.5)
    clear_display(sense_obj)

if __name__ == '__main__':
    main()
