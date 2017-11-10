import pygame, sys
from pygame.locals import *

# Initialize PyGame

pygame.init()
pygame.font.init()

fps = pygame.time.Clock()

window = pygame.display.set_mode( ( 1280, 720 ) )
pygame.display.set_caption( "JCCC Game" )

backgroundColor = pygame.Color( 100, 200, 255 )

# Begin Game Loop
while True:
    for event in pygame.event.get():
        # Detect a "window X" event
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()

    # Fill the window with the color given
    window.fill( backgroundColor )

    # Draw the window to the screen
    pygame.display.update()

    # Regulate the framerate
    fps.tick( 30 )
