from pygame import Surface

class Scene:
    def __init__(self, surface: Surface, size: tuple = (0, 0)):
        self.surface: Surface = surface
        self.next_scene: Scene = self
        self.size: tuple = size

    def process_input(self, events: list, pressed_keys, mouse_pos: tuple) -> None:
        pass
    
    def update(self, delta_time: int) -> None:
        pass
    
    def render(self) -> None:
        pass

    def terminate(self) -> None:
        self.next_scene = None