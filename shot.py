import pygame

from circleshape import CircleShape
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        if (
            self.position.y < 0 - (self.radius * 1.2)
            or self.position.y > SCREEN_HEIGHT + (self.radius * 1.2)
            or self.position.x < 0 - (self.radius * 1.2)
            or self.position.x > SCREEN_WIDTH + (self.radius * 1.2)
        ):
            self.kill()
