import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub classes must override
        pass

    def update(self, dt):
        # Sub classes must override
        pass

    def detect_collision(self, collider) -> bool:
        return self.position.distance_to(collider.position) <= self.radius + collider.radius
