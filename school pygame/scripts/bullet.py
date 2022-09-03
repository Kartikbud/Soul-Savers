import pygame, math

class Bullet2:
    def __init__(self, x, y, image, rect):
        self.pos = (x, y)
        mx, my = rect.centerx, rect.centery
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = image
        self.bullet.fill((255, 50, 50))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 13

    def update(self):
        self.pos = (
            self.pos[0] + self.dir[0] * self.speed,
            self.pos[1] + self.dir[1] * self.speed,
        )

    def draw(self, surf):
        self.bullet_rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.bullet_rect)