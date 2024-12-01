import pygame

from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS
from constants import ASTEROID_SPAWN_RATE
from constants import ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Game start
    pygame.init()
    print(
        f"""
        Starting asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
        """
    )
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Obj groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    # Game Objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("        Game Closing...")
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        # Update & draw objects
        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        # Next frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # 60 FPS


if __name__ == "__main__":
    main()
