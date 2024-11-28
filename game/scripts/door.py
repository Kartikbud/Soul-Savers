from scripts.button import Button
from scripts.tile import Tile

# same as tile
class door(Tile):
    def __init__(self, pos, img):
        super().__init__(pos, img)
        
