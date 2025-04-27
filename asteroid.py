from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self,surface):
        pygame.draw.circle(surface,WHITE_COLOR,self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity *dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        v1 = self.velocity.rotate(rand_angle)
        v2 = self.velocity.rotate(-rand_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x,self.position.y,new_rad)
        a2 = Asteroid(self.position.x,self.position.y,new_rad)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
        