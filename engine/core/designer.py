import pygame
from ui_elements import Button, ProcessElements, Alignment
from scene import Scene
import importlib.util
import time, sys
from pathlib import Path
from tkinter.filedialog import askopenfilename
import tkinter as tk
tk.Tk().withdraw()

#CONSTANTS
FRAME_RATE = 120
WINDOW_NAME = "PyGame Designer"
SIZE = 800, 500

pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
root = pygame.display.set_mode(SIZE)
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

def OpenFileExplorer() -> None:
    path = askopenfilename()
    GetScenesFromPath(path)

def IsInheritFromScene(class_type:type) -> bool:
    return type(class_type) is type and issubclass(class_type, Scene) and class_type != Scene

def OpenDesignerForScene(new_scene:Scene, new_size:tuple = None) -> None:
    global designer_active, active_scene, root
    active_scene = new_scene
    print(active_scene)
    if new_size is not None:
        root = pygame.display.set_mode(new_size)
    designer_active = True

def GetScenesFromPath(path:str) -> None:
    global imported_module
    path_i = Path(path)
    for parent_path in path_i.parents:
        sys.path.append(str(parent_path))
    imported_module = importlib.import_module(path_i.stem)
    for type_ in dir(imported_module):
        type_class = getattr(imported_module, type_)
        if(IsInheritFromScene(type_class)):
            global active_scene_path, active_scene_module_stem, last_modified_time
            active_scene_module_stem = path_i.stem
            active_scene_path = path
            last_modified_time = Path(active_scene_path).stat().st_mtime
            OpenDesignerForScene(type_class(root), (800, 500)) # TODO: currently the size is hardcoded
            return

def CheckIfTheFileIsModified() -> None:
    if active_scene_path is None: return
    global last_modified_time
    current_modified_time = Path(active_scene_path).stat().st_mtime
    if current_modified_time != last_modified_time:
        print("Reloading")
        last_modified_time = current_modified_time
        ReloadScene(active_scene_module_stem)

def ReloadScene(stem:str=None) -> None:
    global imported_module
    imported_module = importlib.reload(imported_module)
    for type_ in dir(imported_module):
        type_class = getattr(imported_module, type_)
        if(IsInheritFromScene(type_class)):
            OpenDesignerForScene(type_class(root), (800, 500)) # TODO: currently the size is hardcoded
            return

select_path_button: Button = Button(root, SIZE[0]/2, SIZE[1]/2, 200, 50, text="Select Path", func=OpenFileExplorer, alignment=Alignment.CENTER)

designer_active: bool = True

imported_module = None

active_scene: Scene = None
active_scene_path: str = None
active_scene_module_stem: str = None

last_modified_time: float = -1
modifying_check_delay: float = 1
last_checked_time: float = time.time()

while designer_active:
    pressed_keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            designer_active = False
            active_scene = None
            

    # Simulate the scene
    if active_scene is not None:
        active_scene.process_input(events, pressed_keys, mouse_pos)
        active_scene.update()
        if active_scene == active_scene.next_scene:
            active_scene.render()
        else:
            active_scene = active_scene.next_scene
    # If there is no scene, display the select path button
    else:
        root.fill((0,0,0))
        ProcessElements(events, pressed_keys, mouse_pos, [select_path_button])
        select_path_button.render()

    # Check if the Scene file is modified
    if time.time() - last_checked_time >= modifying_check_delay:
        last_checked_time = time.time()
        CheckIfTheFileIsModified()

    # Update and tick
    pygame.display.flip()
    clock.tick(FRAME_RATE)
print("Exited")
pygame.quit()