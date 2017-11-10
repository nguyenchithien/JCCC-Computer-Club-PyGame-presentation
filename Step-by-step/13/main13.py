import pygame, sys
from pygame.locals import *
import random
import math

from character import Character, Player, NPC
import functions

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
girlImage = pygame.image.load( "../girl-animated.png" )
stickImage = pygame.image.load( "../stick.png" )
bunnyImage = pygame.image.load( "../bunny-animated.png" )

# Load audio
pickupSound = pygame.mixer.Sound( "../pickup.wav" )
pickup2Sound = pygame.mixer.Sound( "../pickup2.wav" )
pygame.mixer.music.load( "../dancingbunnies.ogg" )

# Create objects
objects = {}
objects[ "stick" ] = Character( stickImage, 0, 0, 32, 32 )
objects[ "stick" ].PlaceRandomly( windowWidth, windowHeight )
objects[ "girl" ] = Player( girlImage, 0, 0, 32, 48, 5 )
objects[ "girl" ].PlaceRandomly( windowWidth, windowHeight )
objects[ "girl" ].SetupAnimation( 4, 0.1 )
objects[ "bunny" ] = NPC( bunnyImage, 0, 0, 32, 32, 3 )
objects[ "bunny" ].PlaceRandomly( windowWidth, windowHeight )
objects[ "bunny" ].SetupAnimation( 4, 0.1 )
objects["bunny"].SetGoal( objects["stick"].GetX(), objects["stick"].GetY() )

pygame.mixer.music.play( -1 )

gameOver = False
winner = ""

# Begin Game Loop
while True:
    for event in pygame.event.get():
        # Detect a "window X" event
        if ( event.type == QUIT ):
            pygame.quit()
            sys.exit()

    if ( gameOver ):
        textSurface = font.render( winner + " wins!", False, textColor )
        window.blit( textSurface, ( windowWidth / 2, windowHeight / 2 ) )

    else:
        # Get keyboard input
        keys = pygame.key.get_pressed()
        objects["girl"].HandleKeys( keys )

        # Check to see if girl hit the stick (passing in the center point, not top-left corner)
        if ( functions.Distance( objects["girl"].GetCenterX(), objects["girl"].GetCenterY(), objects["stick"].GetCenterX(), objects["stick"].GetCenterY() ) < 10 ):
            # Add to points
            objects["girl"].IncreaseScore( 1 )
            # Generate new coordinates
            objects["stick"].PlaceRandomly( windowWidth, windowHeight )
            # Play sound effect
            pickupSound.play()

            objects["bunny"].SetGoal( objects["stick"].GetX(), objects["stick"].GetY() )

            if ( objects["girl"].GetScore() == 5 ):
                gameOver = True
                winner = "Player"

        if ( functions.Distance( objects["bunny"].GetCenterX(), objects["bunny"].GetCenterY(), objects["stick"].GetCenterX(), objects["stick"].GetCenterY() ) < 10 ):
            objects["bunny"].IncreaseScore( 1 )
            objects["stick"].PlaceRandomly( windowWidth, windowHeight )
            objects["bunny"].SetGoal( objects["stick"].GetX(), objects["stick"].GetY() )
            pickup2Sound.play()
            
            if ( objects["bunny"].GetScore() == 5 ):
                gameOver = True
                winner = "Computer"
            

        # Fill the window with the color given
        window.fill( backgroundColor )

        # Draw grass
        functions.DrawGrass( grassImage, window, windowWidth, windowHeight )

        # Draw objects
        for key, obj in objects.iteritems():
            obj.Update()
            obj.Draw( window )

    # Draw text to the screen
    textSurface = font.render( "Player: " + str( objects["girl"].GetScore() ), False, textColor )
    window.blit( textSurface, ( 10, 10 ) )
    textSurface = font.render( "Computer: " + str( objects["bunny"].GetScore() ), False, textColor )
    window.blit( textSurface, ( 200, 10 ) )

    # Draw the window to the screen
    pygame.display.update()

    # Regulate the framerate
    fps.tick( 30 )
