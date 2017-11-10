import pygame, sys
from pygame.locals import *

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

    # Draw the window to the screen
    pygame.display.update()

    # Regulate the framerate
    fps.tick( 30 )
