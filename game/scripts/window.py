from scripts.button import Button
import pygame

class Window:

    def __init__(self, surface) :
        self.surface = surface

    def add_button(self, pos, img) :

        button = Button(pos[0], pos[1], img, self.surface)

        return button.draw()

    def add_text(self, text, pos, size, color) :

        font = pygame.font.Font('assets/alagard.ttf', size)

        font_surf = font.render(f"{text}", False, color)

        self.surface.blit(font_surf, (pos))

    def add_background(self, img) :

        self.surface.blit(img, (0,0))
    
    def add_image(self, pos, img) :

        self.surface.blit(img, pos)

