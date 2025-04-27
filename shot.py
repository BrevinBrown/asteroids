from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,radius=SHOT_RADIUS)

    def draw(self,surface):
        pygame.draw.circle(surface,WHITE_COLOR,self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED *dt
