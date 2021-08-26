import pygame
import random
import sys
import string
import numpy as np

#resolution constants
WINDOWWIDTH = 1020
WINDOWHEIGHT = 820

#init stuff
pygame.display.set_caption("Ecosystem")
WIN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 30

class Animal():
    def __init__(self):
        #screenspaces variables
        self.WINDOWWIDTH = 1020
        self.WINDOWHEIGHT = 820
        #animal variables
        self.awareness = 0.4
        self.health = 1.0
        self.hunger = 0.0
        self.repoUrge = 0.0
        self.pregnancy = 0.0
        self.pregnant = False
        self.maturity = 0.0
        self.sex = random.randint(0,1) #0=female 1=male
        #set unique name
        self.name = f"bunny{''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))}"
        if self.sex:
            i = "male"
            self.animal_surface = pygame.image.load('./assets/bunnymale.png').convert_alpha()
        else:
            i = "female"
            self.animal_surface = pygame.image.load('./assets/bunnyfemale.png').convert_alpha()
        #print(f'created animal {i} {self.name}')
        #place animal on random screen pos
        self.x = 1020 / 2 - 40
        self.y = 820 / 2 - 40
        self.animal_surface = pygame.transform.scale(self.animal_surface, (20, 20))
        self.animal_rect = self.animal_surface.get_rect(center = (self.x, self.y))
        WIN.blit(self.animal_surface, (self.animal_rect))
        #rogue movement stuff
        self.x = 1020 / 2 - 40
        self.y = 820 / 2 - 40
        self.dx = 0
        self.dy = 0
        self.tickcount = 0
        self.time = 120 # base number of ticks before change dir
        self.rtime = random.randint(0, 60)
        self.canmove = True
        self.spriteFlipped = False
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        WIN.blit(self.animal_surface, (self.x, self.y))

    def moveTick(self):
        self.tickcount += 1
        if self.tickcount % (self.time + self.rtime) == 0:
            self.rtime = random.randint(0, 60) # choose new randtime
            self.dx = random.randint(0, 2) - 1 # rand from -1 to 1
            self.dy = random.randint(0, 2) - 1
            #print(f'{self.name} changing dir x:{self.dx} y:{self.dy}')
        #check out of bounds
        if self.x > self.WINDOWWIDTH - 5:
            self.rtime = 60
            self.dx = -2
        if self.x < 0 + 5:
            self.rtime = 60
            self.dx = 2
        if self.y > self.WINDOWHEIGHT - 20:
            self.rtime = 60
            self.dy = -2
        if self.y < 0 + 20:
            self.rtime = 60
            self.dy = 2
        #do the move
        self.move(self.dx, self.dy)
        #points the sprite in the move direction
        if self.dx < 0 and self.spriteFlipped:
            self.animal_surface = pygame.transform.flip(self.animal_surface, True, False)
            self.spriteFlipped = False
        if self.dx > 0 and not self.spriteFlipped:
            self.animal_surface = pygame.transform.flip(self.animal_surface, True, False)
            self.spriteFlipped = True

def spawnFood(number):
    FOOD_IMG = pygame.image.load("./assets/tree.png")
    currentFood = []
    for i in range(number):
        scale = random.randint(5, 15)
        rotation = random.randint(0, 360)
        food = pygame.transform.rotate(pygame.transform.scale(FOOD_IMG, (scale, scale)), rotation)
        x = random.randint(0, WINDOWWIDTH)
        y = random.randint(0, WINDOWHEIGHT)
        foodX = WIN.blit(food, (x, y))
        print(foodX)
        print(type(foodX))
        currentFood.append(foodX)
    pygame.display.update()
    return(currentFood)

def spawnBackground():
    WIN.fill((0, 250, 0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    spawnBackground()
    foodList = spawnFood(30)
    animal_list = []
    for i in range(50):
        x = Animal()
        animal_list.append(x)
    while run:
        WIN.fill((0, 250, 0))
        clock.tick(FPS)
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONUP:
            #    x = Animal()
            #    animal_list.append(x)



            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        for i in animal_list:
            i.moveTick()
        pygame.display.flip() # updates the screen

if __name__ == "__main__":
    main()
