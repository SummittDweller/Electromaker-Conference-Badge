#!/usr/bin/env python3

import inkyphat
from PIL import ImageFont, Image
from time import sleep
font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)

def text(text, colour):
    w, h = font.getsize(text)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = (inkyphat.HEIGHT / 2) - (h / 2)
    inkyphat.text((x, y), text, colour, font)
    inkyphat.show()

def image(file):
    inkyphat.clear()
    inkyphat.set_image(Image.open(file))
    inkyphat.show()

def cleaner():
    colours = (inkyphat.RED, inkyphat.BLACK, inkyphat.WHITE)
    for c in enumerate(colours):
        inkyphat.set_border(c)
        for x in range(inkyphat.WIDTH):
            for y in range(inkyphat.HEIGHT):
                inkyphat.putpixel((x, y), c)
    inkyphat.show()


while True:
    image("/home/pi/Electromaker-Conference-Badge/dweller4.png")
    inkyphat.clear()
    text("Summitt Dweller",inkyphat.BLACK)
    sleep(5)
    image("/home/pi/Electromaker-Conference-Badge/gothic.png")
    inkyphat.clear()
    text("Iowa.Landmark", inkyphat.BLACK)
    sleep(5)
    cleaner()
    sleep(5)
