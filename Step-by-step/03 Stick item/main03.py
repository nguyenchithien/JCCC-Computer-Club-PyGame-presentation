import pygame, sys
from pygame.locals import *
import random

# Function to get random coordinates
def GetRandomCoordinates( maxX, maxY ):
    x = random.randint( 0, maxX )
    y = random.randint( 0, maxY )

    # In Python you can return multiple items with one return
    return x, y

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

# Load images

grassImage = pygame.image.load( "../grass.png" )
girlImage = pygame.image.load( "../girl.png" )
stickImage = pygame.image.load( "../stick.png" )

# Generate random coordinates for the stick
stickX, stickY = GetRandomCoordinates( windowWidth, windowHeight )

# Begin Game Loop
while True:
    for event in pygame.event.get():
        # Detect a "window X" event
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()

    # Fill the window with the color given
    window.fill( backgroundColor )

    # Draw grass
    for y in range( windowHeight / 32 + 1):
        for x in range( windowWidth / 32 ):
            window.blit( grassImage, ( x * 32, y * 32 ) )

    # Draw girl in center of the screen (almost)
    window.blit( girlImage, ( windowWidth / 2, windowHeight / 2 ) )

    # Draw the stick at its coordinates
    window.blit( stickImage, ( stickX, stickY ) )

    # Draw the window to the screen
    pygame.display.update()

    # Regulate the framerate
    fps.tick( 30 )
