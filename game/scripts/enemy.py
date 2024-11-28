import pygame
from scripts.bullet import Bullet2

class EnemyFly:

    def __init__(self, img, pos, screen, rect, dist, speed) :
        
        self.pos = pos
        self.img = img

        self.original_pos = pos

        self.rect = self.img.get_rect(center=pos)

        # bullet surface is a plain rectangular surface
        self.bullet_surf = pygame.Surface((12.75, 6)).convert_alpha()

        self.screen = screen

        self.bullets = []

        # variable that defines whether or not a bullet can be shot and if it has been shot already
        self.shot = False

        self.cooldown = 1200

        self.speed = speed

        self.player_rect = rect

        self.rects = []

        self.create_rects(dist)


    def create_rects(self, dist) :
        
        # creates rects to the left and right of the enemy at a distance defined in the parameter
        self.rect_left = pygame.Rect((self.pos[0]-dist, self.pos[1]), (2, 44))
        self.rect_right = pygame.Rect((self.pos[0]+dist, self.pos[1]), (2, 44))

        # adds each rect to the list of rects
        self.rects.append(self.rect_left)
        self.rects.append(self.rect_right)


    def bullet_recharge(self) :
        
        # if the bullet has been shot it keeps track of the time it was shot and waits until the cooldown to make the variable false once again which allows for a bullet to be shot again
        if self.shot:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.cooldown:
                self.shot = False

    def bullet_update_draw(self) :


        # if the variable is set to false than an instance of bullet class is added to list of bullets and variable is set to true
        if self.shot == False:
            self.bullets.append(Bullet2(self.rect.centerx, self.rect.bottom, self.bullet_surf, self.player_rect))
            self.shot = True
            self.bullet_time = pygame.time.get_ticks()

        # draws and updates the bullets in the list
        for bullet in self.bullets[:] :
            bullet.draw(self.screen)
            bullet.update()

    def draw(self) :
        # draws the enemy onto screen
        self.screen.blit(self.img, (self.rect.x, self.rect.y))
    
    def movement(self) :

        # moves the enemy on the x axis and if the enemy hits with one of the collider rects the enemy switches directions
        self.rect.x += self.speed

        for rect in self.rects :
            if rect.colliderect(self.rect) :
                self.speed *= -1




    def update(self) :

        self.bullet_recharge()
        self.bullet_update_draw()
        self.movement()
