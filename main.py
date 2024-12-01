import pygame

from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS
from constants import ASTEROID_SPAWN_RATE
from constants import ASTEROID_MAX_RADIUS
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(
        f"""
        Starting asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
        """
    )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("        Game Closing...")
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # 60FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
