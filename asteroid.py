from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float)-> None:
        super().__init__(x, y, radius)

    def draw(self, screen)-> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float)-> None:
        self.position += self.velocity * dt

    def split(self)-> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_ang = random.uniform(20,50)
        new_ang1_velocity = self.velocity.rotate(new_ang)
        new_ang2_velocity = self.velocity.rotate(-new_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
        new_asteroid1.velocity = new_ang1_velocity * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_ang2_velocity * 1.2
