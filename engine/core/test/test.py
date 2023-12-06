import sys
sys.path.append('../')
from ui_elements import Button, ProcessElements, Alignment
import pygame
from pygame import Surface

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
root: Surface = pygame.display.set_mode(SIZE)
BACKGROUND_COLOR = (70, 70, 70)

BUTTONS: list[Button] = []
BUTTONS.append(Button(root, WIDTH/2, HEIGHT/2,
                    100, 100, alignment=Alignment.CENTER,
                    click_function=lambda: print('click'),
                    pressed_event=lambda: print('pressed')))

game = True
while game:
    ALL_EVENTS: list[pygame.event.Event] = pygame.event.get()
    PRESSED: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
    MOUSE_POS: tuple[int, int] = pygame.mouse.get_pos()
    for event in ALL_EVENTS:
        if event.type == pygame.QUIT:
            game = False
    root.fill(BACKGROUND_COLOR)
    
    ProcessElements(ALL_EVENTS, PRESSED, MOUSE_POS, BUTTONS)
    for button in BUTTONS:
        button.render()

    pygame.display.flip()


