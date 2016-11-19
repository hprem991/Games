#author Prem
#Date 18 Nov 2016


import random

class Bullet:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Ship:
    def __init__(self, height, width, max):
        self.height = height
        self.width = width
        self.health = 100
        self.x = random.randrange(0, max)
        self.y = random.randrange(0, max)
        self.size = max

    def heal(self):
        self.health += (0.5 * self.health)
        print("Spaceship got its health recovered back by 5%")

    def attack(self, x, y):
        if (((self.x + (self.width / 2)  >= x ) and ( self.x - (self.width / 2)  <= x )) and ((self.y + (self.height / 2) >= y) and (self.y - (self.height / 2) <= y))):
            print("May Day, May Day !!! I am hit")
            if(self.health < 5):
                print("I am going down")
                print("YOU WON")
            else:
                self.health -= (0.5 * self.health)

    def Position(self):
        newX = self.x + random.randrange(-1, 1)
        newY = self.y + random.randrange(-1, 1)
        while ((newX < 0 or newX >= self.size) or (newY < 0) and (newY >= self.size)):
            newX = self.x + random.randrange(-1, 1)
            newY = self.y + random.randrange(-1, 1)
        self.x = newX
        self.y = newY

class Game:
    def  __init__(self, size):
        self.size = size
        self.space = [[0] * size for i in range(size)]
        self.ship = Ship(5, 5, size)
        self.bullet = Bullet(1,1)
        self.counter = 0

    def attack(self):
        self.updatePosition(self.ship.x,self.ship.y)
        while(self.ship.health > 5):
            self.printSpace(self.size)
            x = int(input("Guess Row:"))
            y = int(input("Guess Col:"))
            while ((x < 0 or x >= self.size) or (y < 0) and (y >= self.size)):
                print("Enter Valid values between 0 and "+format(self.size)+" Motherfucker")
                x = int(input("Guess Row:"))
                y = int(input("Guess Col:"))

            self.counter += 1 #was thinkin if counter can be a timer control to regain health


            # This Big if case is for even bigger scenarios when object width and height matters, however here is just comparator check
            #if (((self.ship.x + (self.ship.width / 2)  >= x ) and (self.ship.x - (self.ship.width / 2)  <= x )) and ((self.ship.y + (self.ship.height / 2) >= y) and (self.ship.y - (self.ship.height / 2) <= y))):


            if((x == self.ship.x) and (y == self.ship.y)):
                print("May Day, May Day !!! I am hit")
                self.ship.health -= (0.5 * self.ship.health)
                if(self.ship.health < 5):
                    print("I am going down")
                    print("YOU WON")
                    self.ship.health = 0

            else:
                print("Are you fucking Drunk, you are wasting your ammo")

            if(self.counter % 4 == 0):
                print("Keep sucking my dick son of a bitch!!!")
                self.ship.heal()
                counter = 0
            self.ship.Position()
            self.updatePosition(self.ship.x,self.ship.y)


    def updatePosition(self, x, y):
            self.space = [[0] * self.size for i in range(self.size)]
            self.space[x][y] = 'X'


    def printSpace(self, size):
        print()
        print("Spaceship health :-> " +format(self.ship.health))
        for i in range(self.size):
            for j in range(self.size):
                #use the following line if using python 3 else uncomment the next line
                print(self.space[i][j], end = " ")
                #print(self.space[i][j]),
            print("\n")


def main():
     val =  (int)(input ("Enter Space Size:"))
     battle = Game(val)
     if((int)(input("Do you wanna fuck with me bitch? (Y = 1 / N = 0)")) == 1):
         battle.attack()
     else:
         print("Loser Motherfucker Coward, GTFO Here Bitch!!!")

if __name__ == "__main__":
    main()

