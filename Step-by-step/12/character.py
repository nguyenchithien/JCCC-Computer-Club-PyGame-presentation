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

        # Frames
        self.frame = 0
        self.maxFrame = 0
        self.animateSpeed = 0
        self.animated = False

        # Direction
        self.direction = 0

    # Constructor
    def __init__( self, image, x, y, width, height ):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Frames
        self.frame = 0
        self.maxFrame = 0
        self.animateSpeed = 0
        self.animated = False
        
        # Direction
        self.direction = 0

    # Member function/methods
    def Draw( self, window ):
        if ( self.animated ):
            cropRectangle = ( int( self.frame ) * self.width, int( self.direction ) * self.height, self.width, self.height )
            window.blit( self.image, ( self.x, self.y ), cropRectangle )
            
        else:
            window.blit( self.image, ( self.x, self.y ) )

    def Update( self ):
        if ( self.animated ):
            self.frame = self.frame + self.animateSpeed
            if ( self.frame >= self.maxFrame ):
                self.frame = 0

    def SetupAnimation( self, maxFrame, animateSpeed ):
        self.animated = True
        self.maxFrame = maxFrame
        self.animateSpeed = animateSpeed

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

    # Override this function
    def Update( self ):
        if ( self.animated ):
            speed = self.animateSpeed

            if ( self.isRunning ):
                speed = speed * 2
            
            self.frame = self.frame + speed
            if ( self.frame >= self.maxFrame ):
                self.frame = 0

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
            self.direction = 1
            
        elif ( keys[ K_DOWN ] ):
            self.Move( 0, speed )
            self.direction = 0
            
        elif ( keys[ K_LEFT ] ):
            self.Move( -speed, 0 )
            self.direction = 2
            
        elif ( keys[ K_RIGHT ] ):
            self.Move( speed, 0 )
            self.direction = 3









    
