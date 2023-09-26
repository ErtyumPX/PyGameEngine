# This is script is made to show suggested practice example for the engine
# Files in the practices folder are not required for the engine to work
# Yet they need to be accessing the engine to work so they are commented out and presented here
"""
from game import FadeIn
from scene import Scene
from renderer import RenderManager
from ui_elements import Button, ProcessElements
import pygame, defaults

class MenuScene(Scene):
    def __init__(self, main_surface):
        super().__init__(main_surface)
        self.surface = main_surface
        self.render_manager = RenderManager(main_surface, background_color=(80, 80, 80))
        self.BUTTONS = []
        FadeIn(self, 40)

    def process_input(self, events, pressed_keys, mouse_pos):
        ProcessElements(events, pressed_keys, mouse_pos, self.BUTTONS)

    def update(self):
        pass
    
    def render(self):
        self.render_manager.render()
"""