from circleshape import CircleShape
import pygame
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        #self.velocity = pygame.Vector2(0, 0)


    def draw(self,surface):
        pygame.draw.circle(surface,WHITE_COLOR,self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity *dt
