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


# Player class inherits from Character
class Player( Character ):
    # Pass info to parent constructor
    def __init__( self ):
        Character.__init__( self )
        self.speed = 0
        self.points = 0
        self.isRunning = False

    def __init__( self, image, x, y, width, height ):
        Character.__init__( self, image, x, y, width, height )
        self.speed = 0
        self.points = 0
        self.isRunning = False

    # Special constructor
    def __init__( self, image, x, y, width, height, speed ):
        Character.__init__( self, image, x, y, width, height )
        self.speed = speed
        self.points = 0
        self.isRunning = False

    def IncreaseScore( self, amount ):
        self.points = self.points + amount

    def GetScore( self ):
        return self.points

    def HandleKeys( self, keys ):

        if ( keys[ K_LSHIFT] ):            
            self.isRunning = True
        else:
            self.isRunning = False

        speed = self.speed
        if ( self.isRunning ):
            speed = speed * 2
        
        if ( keys[ K_UP ] ):
            self.Move( 0, -speed )
            
        elif ( keys[ K_DOWN ] ):
            self.Move( 0, speed )
            
        elif ( keys[ K_LEFT ] ):
            self.Move( -speed, 0 )
            
        elif ( keys[ K_RIGHT ] ):
            self.Move( speed, 0 )









    
