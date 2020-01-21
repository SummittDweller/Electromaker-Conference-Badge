#!/usr/bin/env python3

import inkyphat
from PIL import ImageFont, Image
from time import sleep
font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)
margin = 5.

def ctext(text, colour, line):
    w, h = font.getsize(text)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = h * (line - 1) + margin
    inkyphat.text((x, y), text, colour, font)
    # inkyphat.show()

def ltext(text, colour, line):
    w, h = font.getsize(text)
    x = margin
    y = h * (line - 1) + margin
    inkyphat.text((x, y), text, colour, font)
    # inkyphat.show()

def rtext(text, colour, line):
    w, h = font.getsize(text)
    x = inkyphat.WIDTH - w - margin
    y = h * (line - 1) + margin
    inkyphat.text((x, y), text, colour, font)
    # inkyphat.show()

def image(file):
    inkyphat.clear()
    inkyphat.set_image(Image.open(file))
    # inkyphat.show()

def cleaner():
    colours = (inkyphat.RED, inkyphat.BLACK, inkyphat.WHITE)
    for c in enumerate(colours):
        inkyphat.set_border(c)
        for x in range(inkyphat.WIDTH):
            for y in range(inkyphat.HEIGHT):
                inkyphat.putpixel((x, y), c)
    inkyphat.show()


while True:
    inkyphat.set_colour("red")  # required to describe the inkyPHAT unit color
    inkyphat.clear()
 
    image("/home/pi/Electromaker-Conference-Badge/dweller4.png")
    rtext("Summitt", inkyphat.BLACK, 1)
    rtext("Dweller", inkyphat.BLACK, 2)
    inkyphat.show()
    sleep(5)
 
    # inkyphat.clear()
    image("/home/pi/Electromaker-Conference-Badge/gothic.png")
    rtext("Iowa.", inkyphat.BLACK, 3)
    rtext("Landmark", inkyphat.BLACK, 4)
    inkyphat.show()    
    sleep(5)
    # cleaner()
    # sleep(5)
 
    inkyphat.clear()
    ltext("Iowa.", inkyphat.RED, 1)
    ltext("Landmark", inkyphat.RED, 2)
    rtext("Iowa Reviewer", inkyphat.BLACK, 3)
    rtext("Since 4-Oct-2014", inkyphat.BLACK, 4)
    inkyphat.show()
    sleep(5)
 
    inkyphat.clear()
    rtext("Summitt", inkyphat.BLACK, 1)
    rtext("Dweller", inkyphat.BLACK, 2)
    ltext("Charter Member", inkyphat.RED, 3)
    ltext("Since 20-02-2002", inkyphat.RED, 4)
    inkyphat.show()
    sleep(5)
 
