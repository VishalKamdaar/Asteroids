import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        log_event("asteroid_split")
        random_angle = random.uniform(20 ,50)

        tmp = self.velocity.rotate(random_angle)
        tmp2 = self.velocity.rotate(-random_angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_rad)
        a2 = Asteroid(self.position.x, self.position.y, new_rad)

        a1.velocity = tmp * 1.2
        a2.velocity = tmp2 * 1.2
