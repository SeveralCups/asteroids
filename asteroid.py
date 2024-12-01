import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if (
            self.position.y < 0 - (self.radius * 3)
            or self.position.y > SCREEN_HEIGHT + (self.radius * 3)
            or self.position.x < 0 - (self.radius * 3)
            or self.position.x > SCREEN_WIDTH + (self.radius * 3)
        ):
            self.kill()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid_a_vel = self.velocity.rotate(random_angle) * 1.2
        asteroid_b_vel = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = asteroid_a_vel
        asteroid_b.velocity = asteroid_b_vel
