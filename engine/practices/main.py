# This is script is made to show suggested practice example for the engine
# Files in the practices folder are not required for the engine to work
# Yet they need to be accessing the engine to work so they are commented out and presented here
"""
import pygame
from game import *
import defaults, time
# First/starter scene
from menu_scene import MenuScene


pygame.init()

pygame.mouse.set_cursor(*defaults.CURSOR)

size = rootX, rootY = defaults.SIZE

root = pygame.display.set_mode(size)
pygame.display.set_caption(defaults.WINDOW_NAME)

game = Game(MenuScene(root), defaults.FRAME_RATE)
game.run()
"""