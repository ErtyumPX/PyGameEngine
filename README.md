# PyGameEngine
 
A library or so we can call an "engine" for Python's Pygame, our beloved game-making library for python users. Main purpose is to add must-have features for a game engine to ease the use.

This engine is still on developments and being updated often. Please do not hesitate to contribute and add your own flavour.

## License

This project is [MIT](https://github.com/ErtyumPX/PyGameEngine/blob/main/LICENSE) licensed.

## Setup

The folder "engine" is the main library. After you clone or download the repository, you can add the folder to your project and address it:
```python
import engine.ui_elements
```
Or, more easily...... 

Beware that used Python version of this project is [3.8.3](https://www.python.org/downloads/release/python-383).

## It Consists...

### User Interface Elements

Pygame itself does not provide any sorts of UI Elements more than a label that does not have any function. In the [ui_elements.py](https://github.com/ErtyumPX/PyGameEngine/blob/main/Engine/core/ui_elements.py) you can find the essential UI elements; texts, buttons with just texts or images and input boxes with core functionalities for adjusting and aligning.

There will be a multi-line supporting input box after fixing some certain bugs.

### Scene Management System

"will be added soon"

### Animation

An [animation library](https://github.com/ErtyumPX/PyGameEngine/blob/main/Engine/core/animation.py), to change a variable from one value to another by using threading. It has two main functions: By Speed and By Duration.

By Speed function changes the value by a certain amount in every frame, usefull for situations when the speed is defined but the duration of the animation is not important.

By Duration function changes the value in a linearly and reaches to the end poing in the given time span.

### Renderer

A little [render manager](https://github.com/ErtyumPX/PyGameEngine/blob/main/Engine/core/renderer.py) for updating and rendering all objects in one function in every scene. Once you register an object, it will rendered every time render method of the renderer is called, until it is removed from the render manager.

## Other Practices Used By The Author

### main.py

### defaults.py

### Scene Scripting

### Inheriting from Sprite
