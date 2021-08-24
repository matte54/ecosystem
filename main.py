import pygame
import random
import sys
import string
import numpy as np
from system import Animal

#resolution constants
WINDOWWIDTH = 1020
WINDOWHEIGHT = 820

#init stuff
pygame.display.set_caption("Ecosystem")
WIN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 30

class Animal():
    def __init__(self):
        self.moveSpeed = 0.5
        self.awareness = 0.4
        self.health = 1.0
        self.hunger = 0.0
        #self.thirst = 0.0
        self.repoUrge = 0.0
        self.pregnancy = 0.0
        self.pregnant = False
        self.maturity = 0.0
        self.sex = random.randint(0,1) #0=female 1=male
        self.name = f"bunny{''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))}"
        if self.sex:
            i = "male"
            self.animal_surface = pygame.image.load('./assets/bunnymale.png').convert_alpha()
        else:
            i = "female"
            self.animal_surface = pygame.image.load('./assets/bunnyfemale.png').convert_alpha()
        print(f'created animal {i} {self.name}')

        randomWidth = random.randint(0, 1020)
        randomHeight = random.randint(0, 820)
        self.animal_surface = pygame.transform.scale(self.animal_surface, (20, 20))
        self.animal_rect = self.animal_surface.get_rect(topleft = (randomWidth, randomHeight))
        WIN.blit(self.animal_surface, (self.animal_rect))




def spawnBackground():
    WIN.fill((0, 250, 0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    spawnBackground()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x = Animal()



            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()


        pygame.display.update()

if __name__ == "__main__":
    main()
