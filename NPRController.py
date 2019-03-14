#! /usr/bin/env python3

import neopixel

class NPRController:

    ORDER = neopixel.GRB
    NUM_PIXELS = 24

    LT = 'LT'
    LR = 'LR'
    LB = 'LB'
    LL = 'LL'
    LTL = 'LTL'
    LBL = 'LBL'
    LBR = 'LBR'
    LTR = 'LTR'
    RT = 'RT'
    RR = 'RR'
    RB = 'RB'
    RL = 'RL'
    RTL = 'RTL'
    RBL = 'RBL'
    RBR = 'RBR'
    RTR = 'RTR'
    TURR = 'TURR'
    TURL = 'TURL'
    TULR = 'TULR'
    TULL = 'TULL'

    LED_indexes ={ LT:( 0, 1, 2),
                   LR:( 3, 4, 5),
                   LB:( 6, 7, 8),
                   LL:( 9, 10, 11),
                   RT:( 12, 13, 14),
                   RR:( 15, 16, 17),
                   RB:( 18, 19, 20),
                   RL:( 21, 22, 23),
                   RTL:(2,3),
                   RBL:(5,6),
                   RBR:(8,9),
                   RTR:(11,0),
                   LTL:(14,15),                   
                   LBL:(17,18),
                   LBR:(20,21),                 
                   LTR:(23,12),
                   TURR:(2,3,4,5,6),
                   TURL:(14,15,16,17,18),
                   TULR:(8,9,10,11,0),
                   TULL:(20,21,22,23,12)
                  }

    def __init__(self, pixel_pin, brightness_value):
        self.pixel_pin = pixel_pin
        self.num_pixels = NPRController.NUM_PIXELS

        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels, brightness=brightness_value, auto_write=False, pixel_order=NPRController.ORDER)

    def set(self, key, color):
        #print("set()")
        if (key in NPRController.LED_indexes):
            for index in NPRController.LED_indexes[key]:
                #print(index)
                self.pixels[index] = color

    def clear(self):
        #print("clear()")
        self.pixels.fill((0, 0, 0))

    def show(self):
        #print("show()")
        self.pixels.show()

    def stop(self):
        #print("stop()")
        self.pixels.fill((0, 0, 0))
        self.pixels.show()


