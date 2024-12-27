import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_SCALE_FACTOR

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
       self.kill()
       if self.radius <= ASTEROID_MIN_RADIUS:
           return
       radius = self.radius - ASTEROID_MIN_RADIUS
       x, y = self.position.x, self.position.y
       a, b = Asteroid(x, y, radius), Asteroid(x, y, radius)
       angle = random.uniform(20, 50)
       a.velocity = self.velocity.rotate(angle) * ASTEROID_SPLIT_SPEED_SCALE_FACTOR
       b.velocity = self.velocity.rotate(-angle) * ASTEROID_SPLIT_SPEED_SCALE_FACTOR
