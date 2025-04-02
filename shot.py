from circleshape import * 
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity): 
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, color=(255, 255, 255), center=[self.position.x, self.position.y], radius=self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt