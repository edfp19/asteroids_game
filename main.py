#this is the initial commit from local laptop
import pygame
import sys

#game constants
from constants import *
#player values and drawings
from player import Player
#asteroid drawings
from asteroids import Asteroid
#this creates the asteroid field
from asteroidfield import * 
# this takes the shot class
from shot import *

#iniatilize main function
def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
# display the screen with the values found in constants file. 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# this is done so you have a 'starting point' 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
# initialize clock
    clock = pygame.time.Clock()
    """
    This creates pygame groups. This basically groups several objects that share some characteristics. 
    For example, updatable takes Player, Asteroid, AsteroidFields 
    """
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawables, shots)
    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
# initialize the little thingy in the middle of the screen
    player = Player(x, y)
# infinite loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # use the updatable group and run the update method described in player, asteroid etc
        updatable.update(dt)
        player.update_timer(dt)
        #loop through every drawable and draw their members on screen
        #Checks for collisions 
        for asteroid in asteroids:
            if asteroid.check_collision(player): 
                print("GAME OVER!")
                sys.exit()
            for bullet in shots: 
                if bullet.check_collision(asteroid): 
                    asteroid.kill()
                    bullet.kill()
        for drawable in drawables:
            drawable.draw(screen)
        # call the shots 

        
        """
        update dt. That's just a delta of time that we use as a parameter for the object to move and things to refresh
        60 FPS divided by 1000 coverts it into miliseconds 
        I don't really know the reason behind this, gotta get into it
        """

        dt = clock.tick(60)/1000 # Convert milliseconds to seconds
        #flips the screen. Also don't know why
        pygame.display.flip()
#this is so it can *just* run from main. You can't import it elsewhere
if __name__ == "__main__":
    main()
