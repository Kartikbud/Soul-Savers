import pygame
from scripts.settings import *
from scripts.tile import Tile
from scripts.player import Player
from scripts.decorations import Decoration
from scripts.enemy import EnemyFly
from scripts.button import Button
from scripts.displaytext import Textbox
from scripts.soul import CapturedSoul
from scripts.window import Window
import os
from scripts.door import door

pause_background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pausebg.png")),(1400,800))

class PauseMenu:

    def __init__(self, pause_time, screen) :

        self.window = Window(screen)
        self.pause_time = pause_time

    def build(self) :
        window = self.window

        window.add_background(pause_background)


class Level:
    def __init__(self, level_data, surface, start_instructions=False, time_offset=0) :
        self.display_surface = surface

        # defines whether or not the level needs the start instructions
        self.start_bool = start_instructions

        self.level_data = level_data

        self.time_offset = time_offset

        t = tile_size 

        
        self.pause_menu_list = []

        self.testbg = pygame.transform.scale(pygame.image.load('assets/background.png'), (1400,800))
        
        # importing all the tiles
        self.main = pygame.transform.scale(pygame.image.load('assets/tileset/main.png'), (t,t))
        self.left = pygame.transform.scale(pygame.image.load('assets/tileset/left.png'), (t,t))
        self.right = pygame.transform.scale(pygame.image.load('assets/tileset/right.png'), (t,t))
        self.topright = pygame.transform.scale(pygame.image.load('assets/tileset/top-right.png'), (t,t))
        self.topleft = pygame.transform.scale(pygame.image.load('assets/tileset/top-left.png'), (t,t))
        self.bottomleft = pygame.transform.scale(pygame.image.load('assets/tileset/bottom-left.png'), (t,t))
        self.bottomright = pygame.transform.scale(pygame.image.load('assets/tileset/bottom-right.png'), (t,t))
        self.top = pygame.transform.scale(pygame.image.load('assets/tileset/top.png'), (t,t))
        self.bottom = pygame.transform.scale(pygame.image.load('assets/tileset/bottom.png'), (t,t))
        self.inside_bottom_right = pygame.transform.scale(pygame.image.load('assets/tileset/bottom-right-inside.png'), (t,t))
        self.inside_bottom_left = pygame.transform.scale(pygame.image.load('assets/tileset/bottom-left-inside.png'), (t,t))
        self.inside_top_right = pygame.transform.scale(pygame.image.load('assets/tileset/top-right-inside.png'), (t,t))
        self.inside_top_left = pygame.transform.scale(pygame.image.load('assets/tileset/top-left-inside.png'), (t,t))

        # importing other assets
        self.grass = pygame.transform.scale(pygame.image.load('assets/tileset/grass.png'), (27,30))
        self.robot = pygame.transform.scale(pygame.image.load('assets/robot.png'), (33,33))
        self.souls = [pygame.transform.scale(pygame.image.load('assets/soul.png'), (36,48)), pygame.transform.scale(pygame.image.load('assets/soul2.png'), (36,48)), pygame.transform.scale(pygame.image.load('assets/soul4.png'), (36,48))]
        self.font = pygame.font.Font('assets/alagard.ttf', 45)

        self.souls_pos = []

        self.captured_souls_imgs = [pygame.transform.scale(pygame.image.load('assets/captured soul/captured-soul1.png'), (24,33)), pygame.transform.scale(pygame.image.load('assets/captured soul/captured-soul2.png'), (24,33)), pygame.transform.scale(pygame.image.load('assets/captured soul/captured-soul3.png'), (24,33))]

        self.resume = pygame.image.load(os.path.join("assets", "resume.png"))
        self.quit = pygame.image.load(os.path.join("assets", "quitpause.png"))

        self.started = False

        self.counter = 0

        self.door_img = pygame.transform.scale(pygame.image.load('assets/door.png'), (48,64))

        # calling setup function to build the level and create the player
        self.setup_player(self.level_data['level_map'])
        self.setup_level(self.level_data['level_map'])

        self.shift = 0

        self.index = 0

        self.yshift = 0
        self.gravity = False
        self.stuck = False

        self.pausebutton = pygame.image.load(os.path.join("Assets", "pausebutton.png"))
        self.pause_button = Button(700, 100, self.pausebutton, self.display_surface)

        self.paused = False

        #texts
        self.start_img = pygame.image.load('assets/text/Sprite-0003.png')
        self.start_img2 = pygame.image.load('assets/text/Sprite-0001.png')
        self.start_instructions = Textbox(self.start_img, (220,460), self.display_surface)
        self.start_instructions2 = Textbox(self.start_img2, (720,660), self.display_surface)

        self.start_instructions_list = [self.start_instructions, self.start_instructions2]

        self.souls_saved = 0

        self.ticker = 0

        self.playing_anim = False

        self.pause_offset = 0


        self.next_level = False

    # similar method used for making tiles, has to be done seperately because the enemy object requires the player rect as a parameter and if it was done in the same function the player object would be undefined    
    def setup_player(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'P' :
                    self.main_player = Player((x,y), self.display_surface)
                    self.px, self.py = x,y


    def setup_level(self, layout) :
        self.tiles = []
        self.decos = []
        self.enemies = []
        self.captured_souls = []

        level = self.level_data

        #Enumerating through each row (getting both the iteration and the index) and placing a specific tile that corresponds to the character and creating instance of the class
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X' :
                    tile = Tile((x,y), self.main)
                    self.tiles.append(tile)
                if cell == 'L' :
                    tile = Tile((x,y), self.left)
                    self.tiles.append(tile)
                if cell == 'W' :
                    tile = Tile((x,y), self.topleft)
                    self.tiles.append(tile)
                if cell == 'T' :
                    tile = Tile((x,y), self.top)
                    self.tiles.append(tile)
                if cell == 'R' :
                    tile = Tile((x,y), self.right)
                    self.tiles.append(tile)
                if cell == 'D' :
                    tile = Tile((x,y), self.topright)
                    self.tiles.append(tile)
                if cell == 'A' :
                    tile = Tile((x,y), self.bottomleft)
                    self.tiles.append(tile)
                if cell == 'S' :
                    tile = Tile((x,y), self.bottomright)
                    self.tiles.append(tile)
                if cell == 'B' :
                    tile = Tile((x,y), self.bottom)
                    self.tiles.append(tile)
                if cell == 'E' :
                    tile = Tile((x,y), self.inside_top_right)
                    self.tiles.append(tile)
                if cell == 'Q' :
                    tile = Tile((x,y), self.inside_top_left)
                    self.tiles.append(tile)
                if cell == 'Y' :
                    tile = Tile((x,y), self.inside_bottom_right)
                    self.tiles.append(tile)
                if cell == 'U' :
                    tile = Tile((x,y), self.inside_bottom_left)
                    self.tiles.append(tile)
                if cell == 'M' :
                    decoration = Decoration(self.grass, (x,y+18))
                    self.decos.append(decoration)

                if cell == 's' :
                    soul = CapturedSoul((x,y + 10), self.captured_souls_imgs)
                    self.captured_souls.append(soul)
                    self.souls_pos.append((x,y+10))
                    self.counter += 1
                
                if cell == 'd' :
                    self.door_obj = door((x, y-16), self.door_img)
            
                    
    
                if cell == 'e' :
                    enemy = EnemyFly(self.robot, (x,y), self.display_surface, self.main_player.rect, level['enemy_dist'], level['enemy_speed'])
                    self.enemies.append(enemy)
    
    
    def horizontal_collision(self) :
        player = self.main_player

        # applying the players x axis movement and dealing with collisions
        player.rect.x += player.direction.x * player.move_speed

        # when player hits a tile it cheack for right side or left side. If player collides on the right side of itself and hits the left side of 
        # the tile it automatically moves the player to the left side of the tile and vice-versa
        for tile in self.tiles:
            if tile.rect.colliderect(player.rect) :
                if player.direction.x < 0 :
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0 :
                    player.rect.right = tile.rect.left
        
        #if the player is going off the screen it move position to be against the wall so the player doesnt go off the screen
        if player.rect.x >= win_width:
            player.rect.right = win_width
        elif player.rect.x <= 0:
            player.rect.left = 0
     

    def vertical_collision(self) :
        player = self.main_player

        # applying gravity to the player and dealing with vertical collisions
        if not self.paused:    
            player.apply_gravity()

        # looks for collision and if bottom of player collides with top of tile it moves the player to the top of the tile automatically and vice-versa
        for tile in self.tiles:

            if tile.rect.colliderect(player.rect) :

                if player.direction.y > 0 :
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0 :
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0.1
        
        # if the player falls out of the screen it calls reset function
        if player.rect.y >= win_height:
            self.reset()
            

    def bulletCollision(self) :
        # looks at each individual tile and then looks at each bullet in the enemies' bullets and the player's bullets. If a bullet hits a tile it gets 
        # removed from the list of bullets and therefore disappears
        for tile in self.tiles:
            
            for enemy in self.enemies :
                for bullet in enemy.bullets[:] :
                    if bullet.bullet_rect.colliderect(tile) :
                        enemy.bullets.remove(bullet)


    def enemy_bullet_player_collision(self) :
        player = self.main_player

        # looks through each bullet of the enemies and if their is a collision with the player the index will go up which decreases the health
        for enemy in self.enemies:
            for bullet in enemy.bullets[:] :
                if bullet.bullet_rect.colliderect(player.rect) :
                    self.index += 1
                    enemy.bullets.remove(bullet)


    def soul_counter(self) :

        # if the index is greater than 2 the level resets which means the player has 3 lives
        if self.index > 2 :
            self.reset()

        # displays the soul icon corresponding to the index, larger the index smaller the soul  
        self.display_surface.blit(self.souls[self.index], (1300, 60))
    

    def print_text(self) :
        # getting the amount of time passed since the game started and subtracting the offset from the start screen
        self.current_time = round(((pygame.time.get_ticks())/1000) - self.time_offset - self.pause_offset, 3)

        # rendering the time onto the screen
        self.time_text = self.font.render(f"{self.current_time}", False, (255, 255, 255))
        self.display_surface.blit(self.time_text, (70,65))

        # prints the amount of souls saved out of the amount of souls there are
        self.soul_text = self.font.render(f"{self.souls_saved} / {self.counter}", False, (255, 255, 255))
        self.display_surface.blit(self.soul_text, (70,700))


    def reset(self):
        # resets all counts of health and souls saved
        self.souls_saved = 0
        self.index = 0

        # moves player to the original position
        self.main_player.rect.x, self.main_player.rect.y = self.px, self.py

        # deletes all the souls in the map
        self.captured_souls.clear()

        # looks for each each position of the original souls and creates a new soul object using that position and appends to list of souls
        for pos in self.souls_pos:
            soul = CapturedSoul(pos, self.captured_souls_imgs)
            self.captured_souls.append(soul)

        # if there are less than 3 souls made for some reason the missing one is made
        if len(self.captured_souls) < self.counter:
            pos_list = []
            # looks through each original position
            for pos in self.souls_pos:
                # looks through each position of the souls that have spawned and adds it to a list
                for soul in self.captured_souls:
                    pos_list.append(soul.pos)
                    # checks if any of the original positions are in the positions from the list and creates a new soul using that position
                    if pos not in pos_list:
                        self.captured_souls.append(CapturedSoul(pos, self.captured_souls_imgs))
    
    def build_pause_menu(self):

        # looks through pause_menu_list and if the pause menu is there it builds it and its buttons
        for pause in self.pause_menu_list :
            pause.build()
            # if resume button is clicked clears itself from list to remove it from screen
            if pause.window.add_button((200, 90), self.resume):
                self.paused = False
                # keeps track of the time that the resume button is clicked
                resume_time = pygame.time.get_ticks()
                print(pause.pause_time)
                print(resume_time)
                # to calculate the time paused subtract the time passed through initialization of menu from the resume time
                time_paused = resume_time - pause.pause_time
                print(time_paused/1000)
                # add time paused to offset so that in print statement the current time is offset by this amount
                self.pause_offset += time_paused/1000
                # removes itself from list
                self.pause_menu_list.remove(pause)
            # if quit button is clicked game quits
            if pause.window.add_button((200, 240), self.quit):
                pygame.quit()
        

    def run(self) :

        # permittable is variable that defines whether the level is completed or not and if all three souls have been collected it is set to true
        if self.souls_saved == self.counter:
            self.permittable = True
        else:
            self.permittable = False
            
        
        # draws the door onto the screen    
        self.door_obj.draw(self.display_surface)
        
        # checks for collision with door and player, if permittable is set to true it will end level and create the new level
        if self.door_obj.rect.colliderect(self.main_player.rect) and self.permittable:
            self.next_level = True
        
        # draws the tiles
        for tile in self.tiles:
            tile.draw(self.display_surface)
            #tile.update(self.shift, self.yshift)
        
        # draws the grass
        for deco in self.decos :
            deco.draw(self.display_surface)
            #deco.update(self.shift, self.yshift)
        
        # draws the enemies
        for enemy in self.enemies :
            enemy.draw()
            if self.start_bool:
                # checks if the instructions gave cleared and game is not paused then updates the enemies
                if not self.paused and self.started:
                    enemy.update()

            else:
                if not self.paused:
                    enemy.update()
        

        # draws each of the souls and animates it
        for soul in self.captured_souls:
            soul.draw(self.display_surface)
            soul.animate()
            # if the player collides with soul it adds to counter and removes itself from list 
            if soul.rect.colliderect(self.main_player.rect):
                self.captured_souls.remove(soul)
                self.souls_saved += 1
        
        # if level parameter is set to true it prints out instructions and takes it off of screen if the player moves at all
        if self.start_bool:
    
            self.start_instructions2.draw()
            self.start_instructions.draw()
            if self.main_player.direction.x != 0:
                self.start_instructions2.remove()
                self.start_instructions.remove()
                self.started = True

        # if the game is not paused the player will update and the player won't move
        if not self.paused:
            self.main_player.update()
            self.horizontal_collision()
        # applies gravity to the player and manages vertical collisions with tiles
        self.vertical_collision()
        # draws the player to screen
        self.main_player.draw(self.display_surface)
        # runs enemy bullet-tile function
        self.bulletCollision()

        # if the game is not paused it will call print function
        if not self.paused:    
            self.print_text()
        if self.start_bool:    
            if self.started:   
                self.enemy_bullet_player_collision()
        elif not self.start_bool:
            self.enemy_bullet_player_collision()
        self.soul_counter()

        # when the pause button is pressed sets pause bool to True and stops updating everything
        if self.pause_button.draw() and not self.paused:
            self.paused = True
            # gets the time that game was paused and passes through the pause object that is created
            pause_time = pygame.time.get_ticks()
            self.pause_menu_list.append(PauseMenu(pause_time, self.display_surface))
        self.build_pause_menu()

            
        
        

        


