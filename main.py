import pygame
import random
import string

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
        self.juvenile = True
        self.sex = random.randint(0,1) #0=female 1=male
        #set unique name
        self.name = f"bunny{''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))}"
        if self.sex:
            i = "male"
            self.animal_surface = pygame.image.load('./assets/bunnymale.png').convert_alpha()
        else:
            i = "female"
            self.animal_surface = pygame.image.load('./assets/bunnyfemale.png').convert_alpha()
        #print(f'created {i} {self.name}')
        #place animal
        self.x = 1020 / 2 - 40
        self.y = 820 / 2 - 40
        self.animal_surface = pygame.transform.scale(self.animal_surface, (20, 20))
        self.animal_rect = self.animal_surface.get_rect(center = (self.x, self.y))

        #awareness circle stuff
        self.aware_surface = pygame.Surface((100,100))
        self.aware_surface.set_colorkey((0, 0, 0))
        self.aware_surface.set_alpha(100)
        self.awarecircle = pygame.draw.circle(self.aware_surface, (255,255,0), (50, 50), (round(self.awareness * 50 // 1)))

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
        WIN.blit(self.aware_surface, (self.x - 40, self.y - 40))
        WIN.blit(self.animal_surface, (self.x, self.y))


    def brain(self, animal_list, food_list):
        if self.hunger > 0.5 or self.health < 1.0 or self.pregnant == True:
            #find food
            #this is not gonna cut it
            print('Finding food...')
            for x in food_list:
                fxc = round(x.x)
                fyc = round(x.y)
                if fxc > (i.x - 10) and fxc < (i.x + 10) and fyc > (i.y - 10) and fyc < (i.y + 10):
                    #print(f'{i.name} is eating {x.name}')
                    food_list.remove(x)
        elif self.repoUrge > 0.5:
            #find mate
            pass
        else:
            #roam
            self.moveTick()


    def mate(self):
        pass

    def eat(self):
        pass

    def moveTick(self):
        self.tickcount += 1
        if self.tickcount % (self.time + self.rtime) == 0:
            self.rtime = random.randint(0, 60) # choose new randtime
            self.dx = random.randint(0, 2) - 1 # rand from -1 to 1
            self.dy = random.randint(0, 2) - 1
            #print(f'{self.name} changing dir x:{self.dx} y:{self.dy}')
        #check out of bounds
        if self.x > self.WINDOWWIDTH - 20:
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


class food():
    def __init__(self):
        self.sprite = pygame.image.load("./assets/tree.png")
        self.scale = 10
        self.rotation = random.randint(0, 360)
        self.f = pygame.transform.rotate(pygame.transform.scale(self.sprite, (self.scale, self.scale)), self.rotation)
        self.x = random.randint((0 + 20), (WINDOWWIDTH - 20))
        self.y = random.randint((0 + 20), (WINDOWHEIGHT - 20))
        self.name = f"food{''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))}"
        self.tagged = False # set this to true after bunny has started eating?

    def tick(self):
        WIN.blit(self.f, (self.x, self.y))

def grow(food_list):
    # chance to grow food
    foodchance = random.randint(1, 100)
    if len(food_list) < 100 and foodchance > 85:
        r = random.randint(3, 25)
        print(f'Growing {r} food')
        for i in range(r):
            f = food()
            food_list.append(f)

def main():
    clock = pygame.time.Clock()
    run = True
    animal_list = []
    food_list = []
    for i in range(100):
        f = food()
        food_list.append(f)
    for i in range(50):
        x = Animal()
        animal_list.append(x)
    while run:
        WIN.fill((0, 250, 0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x = Animal()
                animal_list.append(x)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('pressed space')

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        for i in food_list:
            i.tick()
        grow(food_list)

        for i in animal_list:
            i.brain(animal_list, food_list)

        pygame.display.flip() # updates the screen

if __name__ == "__main__":
    main()
