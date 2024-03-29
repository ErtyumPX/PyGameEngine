# PyGameEngine
 
A library or so we can call an "engine" for Python's Pygame, our beloved game-making library for python users. Main purpose is to add must-have features for a game engine to ease the use.

This engine is still on developments and being updated often. Please do not hesitate to contribute and add your own flavour.

## License

This project is [MIT](https://github.com/ErtyumPX/PyGameEngine/blob/main/LICENSE) licensed.

## Setup

The directory engine/core is the main library. After you clone or download the repository, you can add the it to your project. A more thorough setup will be added soon.

Beware that used Python version of this project is [3.8.3](https://www.python.org/downloads/release/python-383) and the used Pygame version is [2.0.1](https://www.pygame.org/project/5409/7928).

## It Consists...

### User Interface Elements

Pygame itself does not provide any sorts of UI Elements more than a label that does not have any function. In the [ui_elements.py](https://github.com/ErtyumPX/PyGameEngine/blob/main/engine/core/ui_elements.py) you can find the essential UI elements; texts, buttons with just texts or images and input boxes with core functionalities for adjusting and aligning.

There will be a multi-line supporting input box after fixing some certain bugs.

### Scene Management System

"will be added soon"

### Animation

An [animation library](https://github.com/ErtyumPX/PyGameEngine/blob/main/engine/core/animation.py), to change a value asyncronously. It's currently being refactored and the new version will be presented soon.

### Renderer

A [render manager](https://github.com/ErtyumPX/PyGameEngine/blob/main/engine/core/renderer.py) for updating and rendering all objects in one function in every scene. Once you register an object, it will rendered every time render method is called, until it is removed from the render manager. While registering, the user could specify the z-index to decide the depth of the element while rendering.

## Other Practices Used By The Author

This section represents the practices used by the developers.

### main.py

The file that is used to create the root of the game and to run it. You can mainly create your Game class instance here and run the game by initializing the first scene.

### defaults.py

Mainly used to hold all the constants and static values in one place that  will be used across the project. It's important not to import modules that could cause circular import error.

### Scene Scripting

A sincere suggestion is to create a script for all classes that will derive from [Scene](https://github.com/ErtyumPX/PyGameEngine/blob/main/engine/core/scene.py). A basic Scene looks like this:

```python
from scene import Scene
from renderer import RenderManager
from ui_elements import Button, ProcessElements
import pygame, defaults

class MenuScene(Scene):
    def __init__(self, main_surface):
        Scene.__init__(main_surface)
        self.render_manager = RenderManager(main_surface, background_color=(80, 80, 80))
        self.BUTTONS = [Button(main_surface, x=10, y=10), Button(main_surface, x=100, y=100)]
        self.render_manager.register_all(self.BUTTONS)

    def process_input(self, events: list, pressed_keys, mouse_pos: tuple) -> None:
        ProcessElements(events, pressed_keys, mouse_pos, self.BUTTONS)
    
    def update(self, delta_time: int) -> None:
        pass
    
    def render(self) -> None:
        self.render_manager.render()
```
