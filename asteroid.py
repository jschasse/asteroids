import pygame
import random
from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        r_number = random.uniform(20, 50)
        r_pos_angle = self.velocity.rotate(r_number)
        r_neg_angle = self.velocity.rotate(-r_number)
        
        first_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        second_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        first_asteroid.velocity = r_pos_angle * 1.2
        second_asteroid.velocity = r_neg_angle * 1.2
        