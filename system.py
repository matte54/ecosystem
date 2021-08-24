import random
import string

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
        else:
            i = "female"
        print(f'created animal {i} {self.name}')











#testbunny = Animal()
#print(f'{testbunny.name} sex:{testbunny.sex} hunger:{testbunny.hunger} thirst:{testbunny.thirst}')
