import pygame, sys
from pygame.locals import *
import functions

class Character:
    # Constructor
    def __init__( self ):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.image = None

    # Constructor
    def __init__( self, image, x, y, width, height ):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Member function/methods
    def Draw( self, window ):
        window.blit( self.image, ( self.x, self.y ) )

    def SetPosition( self, x, y ):
        self.x = x
        self.y = y

    def GetX( self ):
        return self.x

    def GetY( self ):
        return self.y

    def GetWidth( self ):
        return self.width

    def GetHeight( self ):
        return self.height

    def GetCenterX( self ):
        return self.x + self.width / 2

    def GetCenterY( self ):
        return self.y + self.height / 2

    def PlaceRandomly( self, maxX, maxY ):
        self.x, self.y = functions.GetRandomCoordinates( maxX, maxY )

    def Move( self, amountX, amountY ):
        self.x = self.x + amountX
        self.y = self.y + amountY
