import pygame
from scripts.support import import_folder

class Player():
    def __init__(self, pos, screen) :

        self.import_assets()

        self.screen = screen

        # movement
        self.jump_speed = -12
        self.move_speed = 6

        #vector to keep track of direction of the player; allows for me to know if the player is going left, right, down, or up
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.6

        #animation
        self.frame_index = 0
        self.animation_speed = 0.28

        self.img = self.animations['idle'][self.frame_index]

        self.rect = self.img.get_rect(topleft = pos)

        #status
        self.status = 'idle'
        self.face_right = True



    # looks through each key in the dictionary and adds the list of imgs that are returned from the functin to each key
    def import_assets(self) :
        character_path = 'assets/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys() :
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    
    # the folder of imgs is set to the status of the player
    def animate(self) :
        animation = self.animations[self.status]

        # if the status is idle the animation speed is slightly slower
        # the way the animation works is by looping through the list of imgs by defining an index variable that keeps getting added a frame speed onto. Because the function is run in a loop the index is always getting added onto and eventually it changes from a 0 to a 1 and then to a 2. the index is used to define what index of the list is blitted onto the screen so as it goes up the imgs change.
        if self.status == 'idle':
            self.frame_index += (self.animation_speed - 0.15)
        else:
           self.frame_index += self.animation_speed


        if self.frame_index >= len(animation) :
            self.frame_index = 0

        img = animation[int(self.frame_index)]

        # depending on the vector direction the imgs will be flipped to face the opposite direction 
        if self.face_right:
            self.img =  img
        else :
            self.img = pygame.transform.flip(img, True, False)

    def get_state(self) :
        # checks the vector and the direction to confirm the status of the player.
        # first looks at y vector and if it is negative player is jumping, if it is positive it is falling(reason it is above 1 and not 0 is because the gravity is 0.8 and the player is constantly falling at that rate at being reset to 0 because it collides with tile over and over again)
        if self.direction.y < 0 :
            self.status = 'jump'
        elif self.direction.y > 1 :
            self.status = 'fall'
        else:
            # then looks that the x vector to see if moving or not and if it is moving horizontally at all status is set to run or else it is idle
            if self.direction.x != 0:
                self.status = 'run'
            else :
                self.status = 'idle'

    # the way the gravity works is by constantly updating the y vector to make it larger and then adding the y vector to players position to make it ifall down increasingly faster
    def apply_gravity(self) :
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # because the y vector is being added on to the y position if the y vector is assigned to a negative value the players y position would go up in movement but then come down due to the y vector still being added onto.
    def jumpfunct(self) :
        self.direction.y = self.jump_speed

    def getInput(self) :
        keys = pygame.key.get_pressed()

        # if the key to move left is clicked the x vector is assigned to a negative 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT] :
            self.direction.x = -1
            self.face_right = False
        # if the key to move right is clicked the x vector is assigned to a positive 1 and the variable of facing right is assigned true
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT] :
            self.direction.x = 1
            self.face_right = True
        # if neither are clicked then the vector is set to 0
        else :
            self.direction.x = 0

        # if the jump keys are being pressed and the player is not falling or in the air the jump function is called
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.direction.y == 0:
            self.jumpfunct()

    def update(self) :
        # runs all functions that are to be run in the loop
        self.getInput()
        self.get_state()
        self.animate()
 
    # bilts the player onto the screen according to the img
    def draw(self, surf) :

        surf.blit(self.img, (self.rect.x, self.rect.y))


            




