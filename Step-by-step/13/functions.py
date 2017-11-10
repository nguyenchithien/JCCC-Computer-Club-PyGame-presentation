import pygame, sys
from pygame.locals import *
import random
import math

# Function to get random coordinates
def GetRandomCoordinates( maxX, maxY ):
    x = random.randint( 0, maxX )
    y = random.randint( 0, maxY )

    # In Python you can return multiple items with one return
    return x, y

def IsClicking( objectX, objectY, objectWidth, objectHeight, mouseX, mouseY ):
    return ( mouseX >= objectX and mouseX <= objectX + objectWidth
            and mouseY >= objectY and mouseY <= objectY + objectHeight )

# Get distance between two objects (from cnter point)
def Distance( x1, y1, x2, y2 ):
    return math.sqrt( (x2-x1) ** 2 + (y2-y1) ** 2 )

def DrawGrass( grassImage, window, windowWidth, windowHeight ):
    for y in range( windowHeight / 32 + 1):
        for x in range( windowWidth / 32 ):
            window.blit( grassImage, ( x * 32, y * 32 ) )
