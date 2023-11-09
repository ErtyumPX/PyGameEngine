import pygame, random
from time import time
from enum import Enum
from pygame import Vector2

class Curves(Enum):
    Linear = 0

def InterpolateValue(start_value: float, end_value: float, alpha: float, curve: Curves = Curves.Linear) -> int:
    """
    Interpolates between two values. Values could be int but output will be float either way.
    """
    if(start_value == end_value): return start_value
    return start_value + (end_value - start_value) * alpha

def InterpolateVector(start_vector, end_vector, alpha: float, curve: Curves = Curves.Linear):
    """
    Interpolates between two vectors. Vector values could be pygame.Vector2, pygame.Vector3
    """
    if(start_vector == end_vector): return start_vector
    return start_vector + (end_vector - start_vector) * alpha

def InterpolateTuples(start_tuple: tuple, end_tuple: tuple, alpha: float, curve: Curves = Curves.Linear) -> tuple:
    """
    Interpolates between two tuples. Tuple values could be int but output will be float either way.
    """
    if(start_tuple == end_tuple): return start_tuple
    return tuple(InterpolateValue(start_tuple[i], end_tuple[i], alpha, curve) for i in range(len(start_tuple)))

class Particle():
    def __init__(self, position: Vector2, creation_time: int, life_time: int, 
                 initial_color:tuple, initial_radius: int, initial_velocity: Vector2,
                 last_color: tuple, last_radius: int, last_velocity: Vector2):
        """
        All coordinates are according to the surface the particle is drawn on, not relative to the particle system they belong
        position: tuple (x, y) -> Starting position of the particle. Stored in each since it could be randomized
        creation_time: int (ms) -> Time when the particle was created
        life_time: int (ms) -> How long the particle will live
        initial_color: tuple (r, g, b, a) -> Starting color of the particle, supports alpha values
        initial_radius: int -> Starting radius of the particle
        initial_velocity: tuple (x, y) -> Starting velocity of the particle
        """
        self.position = position
        self.creation_time = creation_time
        self.life_time = life_time
        self.color = initial_color
        self.radius = initial_radius
        self.velocity = initial_velocity
        self.last_color = last_color
        self.last_radius = last_radius
        self.last_velocity = last_velocity

        self.life_time_normalized = 0

    def move(self, current_time: int, delta_time: int):
        self.position += self.velocity * delta_time
        self.life_time_normalized = (current_time - self.creation_time) / self.life_time
        self.velocity = InterpolateVector(self.velocity, self.last_velocity, self.life_time_normalized, Curves.Linear)
        self.color = InterpolateTuples(self.initial_color, self.last_color, self.life_time_normalized, Curves.Linear)
        self.radius = InterpolateValue(self.initial_radius, self.last_radius, self.life_time_normalized, Curves.Linear)



class ParticleSystem():
    """
    Position: tuple (x, y)
    Duration: int (ms) -> -1 means in a loop, continues forever until manually stopped
    Particle Life Time: int (ms)
    Start Delay: int (ms)
    Gravity: tuple (x, y) -> gravity acceleration in x and y direction
    Emission:
        Emission Rate: int (ms) -> how often a particle is emitted
        Emitter Shape: Enum -> "circle", "square", "line", "point"
    Particle:
        Color: tuple (r, g, b)
        Size: int (px)
        Shape: Enum -> "circle", "square", "line", "point" or an image
        Initial Velocity: tuple (x, y)
    Change:
        Size over Time: Enum -> "increase", "decrease", "none"
        Color over time: Enum -> "fade", "none"
    """
    """
    For now, the emitter shape is a point, all particles are emitted from the same point
    """
    def __init__(self, surface:pygame.Surface, position: Vector2, duration: int):
        pass

        #self.particle_list = [Particle(self.pos, [random.random(), random.random()], gravity, time()) for _ in range(max_particle)]

    def update(self, delta_time: int):
        for part in self.all_particles:
            # draw particle
            if time() - part.creation_time >= self.life_time:
                self.particle_list.remove(part)
                self.particle_list.append(Particle(self.pos, [random.random(), random.random()], self.gravity, time()))
            else:
                part.move()

