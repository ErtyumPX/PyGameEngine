class Scene:
    def __init__(self, surface):
        self.surface = surface
        self.next_scene = self

    def process_input(self, events: list, pressed_keys, mouse_pos: tuple) -> None:
        pass
    
    def update(self, delta_time: int) -> None:
        pass
    
    def render(self) -> None:
        pass

    def terminate(self) -> None:
        self.next_scene = None