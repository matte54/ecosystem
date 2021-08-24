import pygame
import random
import numpy as np
from noisemap import generatenoise

#resolution constants
WINDOWWIDTH = 1020
WINDOWHEIGHT = 820

pygame.display.set_caption("Ecosystem")
WIN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 30

def spawnBackground():
    WIN.fill((0, 0, 255))
    pygame.display.update()

def spawnLand():
    matrix = generatenoise()
    x = 0
    y = 0
    for i in range(matrix.shape[0]):
        x = 0
        y += 10
        for j in range(matrix.shape[1]):
            x += 10
            if matrix[i][j] == 1:
                r = pygame.draw.rect(WIN,(0, 250, 0),(x, y, 10, 10))
                land = pygame.Rect.union(r, r)
    pygame.display.update()
    return(land)

def spawnBushes(number, land):
    TREE_IMG = pygame.image.load("./assets/tree.png")
    for i in range(number):
        scale = random.randint(10,20)
        rotation = random.randint(0, 360)
        tree = pygame.transform.rotate(pygame.transform.scale(TREE_IMG, (scale, scale)), rotation)
        x = random.randint(0, WINDOWWIDTH)
        y = random.randint(0, WINDOWHEIGHT)
        if land.collidepoint(x, y) == False:
            WIN.blit(tree, (x, y))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    spawnBackground()
    land = spawnLand()
    #spawnBushes(100, land)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                spawnBackground()
                spawnLand()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

if __name__ == "__main__":
    main()
