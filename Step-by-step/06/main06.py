import pygame, sys
from pygame.locals import *
import random

# Function to get random coordinates
def GetRandomCoordinates( maxX, maxY ):
    x = random.randint( 0, maxX )
    y = random.randint( 0, maxY )

    # In Python you can return multiple items with one return
    return x, y

def IsClicking( objectX, objectY, objectWidth, objectHeight, mouseX, mouseY ):
    return ( mouseX >= objectX and mouseX <= objectX + objectWidth
            and mouseY >= objectY and mouseY <= objectY + objectHeight )

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

# Generate random coordinates for the stick
stickX, stickY = GetRandomCoordinates( windowWidth, windowHeight )

# Generate random coordinates for the girl
girlX, girlY = GetRandomCoordinates( windowWidth, windowHeight )
girlSpeed = 5

points = 0

# Begin Game Loop
while True:
    for event in pygame.event.get():
        # Detect a "window X" event
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()

        # Check for mouse click
        elif ( event.type == MOUSEBUTTONDOWN ):
            mouseX, mouseY = event.pos

            # Are we clicking the stick?
            if ( IsClicking( stickX, stickY, 32, 32, mouseX, mouseY ) ):
                # Add to points
                points = points + 1
                # Generate new coordinates
                stickX, stickY = GetRandomCoordinates( windowWidth, windowHeight )
                # Play sound effect
                pickupSound.play()

    # Get keyboard input
    keys = pygame.key.get_pressed()
    # Which keys were pressed?
    if ( keys[ K_UP ] ):
        girlY = girlY - girlSpeed
    elif ( keys[ K_DOWN ] ):
        girlY = girlY + girlSpeed
    elif ( keys[ K_LEFT ] ):
        girlX = girlX - girlSpeed
    elif ( keys[ K_RIGHT ] ):
        girlX = girlX + girlSpeed

    # Fill the window with the color given
    window.fill( backgroundColor )

    # Draw grass
    for y in range( windowHeight / 32 + 1):
        for x in range( windowWidth / 32 ):
            window.blit( grassImage, ( x * 32, y * 32 ) )

    # Draw girl in center of the screen (almost)
    window.blit( girlImage, ( girlX, girlY ) )

    # Draw the stick at its coordinates
    window.blit( stickImage, ( stickX, stickY ) )

    # Draw text to the screen
    textSurface = font.render( str( points ), False, textColor )
    window.blit( textSurface, ( 10, 10 ) )

    # Draw the window to the screen
    pygame.display.update()

    # Regulate the framerate
    fps.tick( 30 )
