import pygame

class CapturedSoul:
    def __init__(self, pos, img) :
        self.index = 0
        
        # defining base values
        self.pos = pos
        self.animation = img
        self.img = self.animation[0]
        self.rect = self.img.get_rect(topleft=self.pos)

        self.animate_speed = 0.08

    def animate(self):
        # same animation system as player
        self.index += self.animate_speed

        if self.index >= 3:
            self.index = 0
        
        img = self.animation[int(self.index)]
        self.img = img

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))