#this is the initial commit from local accenture laptop
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        dt = clock.tick(60)/1000 # Convert milliseconds to seconds
        pygame.display.flip()

if __name__ == "__main__":
    main()
