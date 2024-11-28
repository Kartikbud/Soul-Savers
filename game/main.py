import pygame, os
from pygame.locals import *
from scripts.settings import *
from scripts.level import Level
from scripts.window import Window

# defining game class to manage the levels and transitions
class PlayerGame:
    def __init__(self, time) :

        # creating first level, takes in time parameter so the time taken in the start screen is subtracted from total time
        self.level = Level(level1, screen, True, time )

        # creating a list for each level so I can clear the list to therfore delete the level after completed
        self.level1 = [self.level]
        self.level2 = []
        self.level3 = []

    def run(self) :

        # looking through each level list and checking if the variable that identifies whether the level is over or not is true if it is true the list will clear itself removing the level from the game and it will create the next level and append it to the corresponding list
        for level in self.level1:
            level.run()
            if level.next_level :
                self.level1.clear()
                self.level2.append(Level(level2, screen))
        for level in self.level2:
            level.run()
            if level.next_level:
                self.level2.clear()
                self.level3.append(Level(level3, screen))
        #for last level it clears itself from the list and records the final time it took to complete the game, it passes through this time into the end loop function so that it can be displayed
        for level in self.level3:
            level.run()
            if level.next_level:
                timer = level.current_time
                self.level3.clear()
                end_loop(timer)

# Using window class to make classes for different windows.
class MainMenu:

    def __init__(self) :

        self.window = Window(screen)
    
    def build(self) :
        window = self.window

        window.add_background(background)
        window.add_text('Soul Saver', (350, 250), 150, (255,255,255))
        window.add_image((1400-390, 400), player_img)
        
        
    def build_buttons(self) :  
        window = self.window
        clicked = False

        if window.add_button((700, 600), start) :
            clicked = True
        
        return clicked


class InfoMenu:
    def __init__(self):
        self.window = Window(screen)

    def build(self):
        self.window.add_background(background)
        self.window.add_background(pause_background)
        
# takes time as a parameter to display the final time taken to finish game
class EndMenu:

    def __init__(self, time):

        self.window = Window(screen)
        self.time = time

    def build(self):
        #self.window.surface.fill((0,0,0))
        self.window.add_background(background)
        self.window.add_text('Congrats you saved everyone', (160, 250), 80, (255,255,255))
        self.window.add_text('Your time: ' + str(self.time) + ' s', (400, 500), 60, (255,255,255))
        
                    
    
if __name__ == '__main__' : 
    
    #initializing pygame
    pygame.init()

    #setting FPS variable
    clock = pygame.time.Clock()

    #setting screen
    screen = pygame.display.set_mode((win_width, win_height))   

    bg_colour = (12,12,26)

    p_width, p_height = 44, 56

    player_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "character", 'idle', '1.png')), (p_width, p_height))


    floor = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "base.png")), (900,200))

    obstacle_book = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "book-obstacles4.png")), (76, 114))

    title = pygame.image.load(os.path.join("Assets", "title.png"))

    start = pygame.image.load(os.path.join("Assets", "start.png"))
    resume = pygame.image.load(os.path.join("Assets", "resume.png"))
    quit = pygame.image.load(os.path.join("Assets", "quit.png"))
    pause_background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pausebg.png")),(1400,800))

    background = pygame.transform.scale(pygame.image.load('assets/mainbackground.png'), (1400,800) )

    player_img = pygame.transform.scale(pygame.image.load('assets/titleimg.png'), (390,426))

    paused = False

    testbg = pygame.transform.scale(pygame.image.load('assets/background.png'), (1400,800))
    
    # defining object of game class
    
    main_menu = MainMenu()
    info_menu = InfoMenu()
    
    
    #main game loop, game as parameter because the instance of PlayerGame class is created in start loop and passed through into the game loop
    def playerLoop(game):

        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            #checking if player quits game and closing screen if they do
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()    
            game.run()

            pygame.display.flip()

    def start_loop():
        
        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            #checking if player quits game and closing screen if they do
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        
            main_menu.build()
            if main_menu.window.add_button((700, 600), start) :
                start_time = pygame.time.get_ticks()/1000
                game = PlayerGame(start_time)
                playerLoop(game)

            pygame.display.flip()
    
    def info_loop():
        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            #checking if player quits game and closing screen if they do
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
            
            info_menu.build()
    
    def end_loop(time):
        run = True
        while run:
            clock.tick(45)
            screen.fill(bg_colour)

            #checking if player quits game and closing screen if they do
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
            
            end_menu = EndMenu(time)
   
            end_menu.build()       
        
            pygame.display.flip()

    start_loop()