#! /usr/bin/env python3

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 24)

pixels.fill((0, 0, 0))
pixels.show()

