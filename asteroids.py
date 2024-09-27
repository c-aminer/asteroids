from circleshape import *
from player import * 
from constants import *
import random





class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rnd_angle = random.uniform(20, 50)
        new_vector_one = self.velocity.rotate(rnd_angle) * 1.2
        new_vector_two = self.velocity.rotate(-rnd_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_one.velocity = new_vector_one
        new_two.velocity = new_vector_two





