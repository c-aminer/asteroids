from circleshape import *
from player import * 
from constants import *





class Asteroid(CircleShape):

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt



