import pygame

# tiles that have a rectangle and img
class Tile:
    def __init__(self, pos, img):
        self.img = img
        self.rect = self.img.get_rect(topleft = pos)

    def draw(self, surf) :
        surf.blit(self.img, (self.rect.x, self.rect.y))

    def update(self, x_shift, yshift = 0) :
        self.rect.x += x_shift
        