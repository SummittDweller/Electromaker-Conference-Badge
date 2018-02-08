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

def container():
    inkyphat.rectangle((0,0,212,104),inkyphat.RED)
    inkyphat.rectangle((4,4,208,100),inkyphat.BLACK)
    inkyphat.show()

def cleaner():
    colours = (inkyphat.RED, inkyphat.BLACK, inkyphat.WHITE)
    for j, c in enumerate(colours):
        inkyphat.set_border(c)
        for x in range(inkyphat.WIDTH):
            for y in range(inkyphat.HEIGHT):
                inkyphat.putpixel((x, y), c)
    inkyphat.show()


while True:
    image("electromaker-edit.png")
    #container()
    inkyphat.clear()
    text("@biglesp",inkyphat.BLACK)
    sleep(5)
    #container()
    inkyphat.clear()
    text("http://bigl.es", inkyphat.BLACK)
    sleep(5)
    cleaner()
    sleep(5)

