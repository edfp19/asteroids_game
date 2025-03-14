#this is the initial commit from local accenture laptop
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import * 

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    player = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        dt = clock.tick(60)/1000 # Convert milliseconds to seconds
        pygame.display.flip()

if __name__ == "__main__":
    main()
