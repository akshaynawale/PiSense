#!/usr/bin/env python3
from sense_hat import SenseHat
from display_lib import set_color, get_rand_color
import random
import time


def main():
    sense_obj = SenseHat()
    for i in range(100):
        print("{0}th iteration")
        set_color(sense_obj, get_rand_color(), 0.2)
    print("Thanks for watching")
    #sense.show_message("Akshay the Great :)")

if __name__ == "__main__":
    main()
