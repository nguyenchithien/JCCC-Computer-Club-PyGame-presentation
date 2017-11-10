import pygame, sys
from pygame.locals import *
import random
import math

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
        self.x, self.y = GetRandomCoordinates( maxX, maxY )

    def Move( self, amountX, amountY ):
        self.x = self.x + amountX
        self.y = self.y + amountY

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

# Initialize PyGame
pygame.init()
pygame.font.init()

fps = pygame.time.Clock()

# Use variables to store window width/height
windowWidth = 1280
windowHeight = 720

window = pygame.display.set_mode( ( windowWidth, windowHeight ) )
pygame.display.set_caption( "JCCC Game" )

backgroundColor = pygame.Color( 100, 200, 255 )

# Create text color
textColor = pygame.Color( 255, 255, 255 )

# Load font
font = pygame.font.Font( "../Redkost Comic.otf", 20 )

# Load images
grassImage = pygame.image.load( "../grass.png" )
girlImage = pygame.image.load( "../girl.png" )
stickImage = pygame.image.load( "../stick.png" )

# Load audio
pickupSound = pygame.mixer.Sound( "../pickup.wav" )

# Create objects
objects = {}
objects[ "stick" ] = Character( stickImage, 0, 0, 32, 32 )
objects[ "stick" ].PlaceRandomly( windowWidth, windowHeight )
objects[ "girl" ] = Character( girlImage, 0, 0, 32, 48 )
objects[ "girl" ].PlaceRandomly( windowWidth, windowHeight )

# To move next...
girlSpeed = 5
points = 0

# Begin Game Loop
while True:
    for event in pygame.event.get():
        # Detect a "window X" event
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()

    # Get keyboard input
    keys = pygame.key.get_pressed()
    # Which keys were pressed?
    if ( keys[ K_UP ] ):
        objects["girl"].Move( 0, -girlSpeed )
    elif ( keys[ K_DOWN ] ):
        objects["girl"].Move( 0, girlSpeed )
    elif ( keys[ K_LEFT ] ):
        objects["girl"].Move( -girlSpeed, 0 )
    elif ( keys[ K_RIGHT ] ):
        objects["girl"].Move( girlSpeed, 0 )

    # Check to see if girl hit the stick (passing in the center point, not top-left corner)
    if ( Distance( objects["girl"].GetCenterX(), objects["girl"].GetCenterY(), objects["stick"].GetCenterX(), objects["stick"].GetCenterY() ) < 10 ):
        # Add to points
        points = points + 1
        # Generate new coordinates
        objects["stick"].PlaceRandomly( windowWidth, windowHeight )
        # Play sound effect
        pickupSound.play()
        

    # Fill the window with the color given
    window.fill( backgroundColor )

    # Draw grass
    DrawGrass( grassImage, window, windowWidth, windowHeight )

    # Draw objects
    for key, obj in objects.iteritems():
        obj.Draw( window )

    # Draw text to the screen
    textSurface = font.render( str( points ), False, textColor )
    window.blit( textSurface, ( 10, 10 ) )

    # Draw the window to the screen
    pygame.display.update()

    # Regulate the framerate
    fps.tick( 30 )
