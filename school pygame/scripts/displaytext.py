import pygame
from scripts.button import Button

class Textbox:
    def __init__(self, img, pos, surface) :
        # makes a button using the pos, img, and surface
        # creates a list to store the text in to make it removable from screen
        self.list = []
        self.button = Button(pos[0], pos[1], img, surface)
        self.list.append(self.button)
    
    def draw(self):
        # blits whatever is in list to screen and does nothing if clicked
        for text in self.list :
            if text.draw():
                None
    
    def remove(self) :
        # removes text from list if function is called and removes text from screen
        for text in self.list :
            self.list.remove(text)

# P.S. button function is unessecary, originally i wanted to make it clickable but I changed it and was too lazy to change code


    