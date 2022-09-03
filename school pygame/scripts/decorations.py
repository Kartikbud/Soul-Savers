import pygame
from scripts.tile import Tile

class Decoration(Tile):

    def __init__(self, img, pos) :
        super().__init__(pos, img)


