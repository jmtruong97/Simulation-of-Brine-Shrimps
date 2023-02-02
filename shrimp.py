#
# Author : Juanitta Truong
# ID : 18360682
#
# shrimp.py - Class definitions for simulation of brine shrimp 
#
# References
# def init:
#   File name: shrimp.py
#   Author: Valerie (Lecturer)
#   Date: 2/10/2019 – Base version for assignment
#   Location: Curtin University
#
# def __str__:
#   File name: shrimp.py
#   Author: Valerie (Lecturer)
#   Date: 2/10/2019 – Base version for assignment
#   Location: Curtin University
#
# def getSize:
#   File name: shrimp.py
#   Author: Valerie (Lecturer)
#   Date: 2/10/2019 – Base version for assignment
#   Location: Curtin University
#
# def stepChange:
#   File name: shrimp.py
#   Author: Valerie (Lecturer)
#   Date: 2/10/2019 – Base version for assignment
#   Location: Curtin University
#
#
#
import random 

class Shrimp():
    states = ["egg", "hatchling", "juvenile", "adult", "dead"]
    directions = ["upmax", "downmax", "leftmax", "rightmax"] 
    
    def __init__(self, pos, XMAX, YMAX, agestep): #initialising the shrimps, 4 parameters
        self.pos = pos 
        self.state = self.states[0] #intial state is egg
        self.age = 0 
        self.XMAX = XMAX #tank width (x)
        self.YMAX = YMAX #tank height (y)
        self.direction = self.directions[random.randint(0,3)] #inital direction is random 
        self.agestep = agestep 
        
    def __str__(self): #returns which state at which position to caller in main
        return self.state + " @ " + str(self.pos) 
    
    def getAge(self): #checks age, changes state depending on age
        if (self.age <= 1 and self.age >= 0) and self.state != "dead": #only changes state if it isn't dead
            self.state = "egg"
        elif (self.age <= 7 and self.age > 1) and self.state != "dead":
            self.state = "hatchling"
        elif (self.age <= 21 and self.age > 7) and self.state != "dead":
            self.state = "juvenile"
        elif (self.age <= 28 and self.age > 21) and self.state != "dead":
            self.state = "adult"
        else:
            if self.age >= 29:
                self.state = "dead"
            
    def getSize(self): #checks state, sets the size of shrimp depending on it's state
        if self.state == "egg":
            size = 1
        elif self.state == "hatchling":
            size = 3
        elif self.state == "juvenile":
            size = 5
        elif self.state == "adult":
            size = 7
        else:
            size = 7
        return size #returns sizes to caller in plt.plot
    
    def getColor(self): #checks state, sets colour of shrimps depending on it's state
        if self.state == "egg":
            color = 'yo' #y for yellow and o for dots
        elif self.state == "hatchling":
            color = 'ro' #r for red
        elif self.state == "juvenile":
            color = 'bo' #b for blue
        elif self.state == "adult":
            color = 'mo' #m for magenta 
        else:
            color = 'kx' #k for black, x for crosses
        return color #returns colours to caller in plt.plot
    
    def checkWall(self): #checks if shrimps collide into walls, sets pos, changes direction
        if self.pos[1] >= self.YMAX: 
            self.pos[1] = self.YMAX - 15 
            self.direction = "downmax" 
        elif self.pos[1] <= 0: 
            self.pos[1] = 15 
            self.direction = "upmax" 
        elif self.pos[0] >= self.XMAX: 
            self.pos[0] = self.XMAX - 15 
            self.direction = "leftmax" 
        elif self.pos[0] <= 0: 
            self.pos[0] = 15 
            self.direction = "rightmax" 
            
    def getMovement(self, xspeed, yspeed): #checks direction, sets movement in that direction 
        if self.direction == "downmax": 
            self.pos[1] -= yspeed 
        elif self.direction == "upmax":
            self.pos[1] += yspeed 
        elif self.direction == "leftmax":
            self.pos[0] -= xspeed 
        elif self.direction == "rightmax":
            self.pos[0] += xspeed 
        self.checkWall() #calls to check and handle collisions with walls
        
    def stepChange(self): #adds agestep, checks states, changes its speed and movement depending on state
        self.age += self.agestep 
        self.getAge() #checks age, changes state
        if self.state == "hatchling":
            xspeed = round(self.XMAX/random.randint(8,10)) 
            yspeed = round(self.YMAX/random.randint(8,10)) 
            self.getMovement(xspeed, yspeed) #calls movement and direction
        elif self.state == "juvenile":
            xspeed = round(self.XMAX/random.randint(5,8))
            yspeed = round(self.YMAX/random.randint(5,8))
            self.getMovement(xspeed, yspeed)
        elif self.state == "adult":
            xspeed = round(self.XMAX/random.randint(2,5))
            yspeed = round(self.YMAX/random.randint(2,5))
            self.getMovement(xspeed, yspeed)
        elif self.state == "dead":
                 self.pos[1] = 5 #dead shrimps stays at the bottom of tank
        
    def checkCollisions(self, m): #checks for collisions with opposite directions, changes pos
        if self.direction == "upmax" and m.direction == "downmax": 
            self.pos[1] -= 10 
            m.pos[1] += 10 
        elif self.direction == "downmax" and m.direction == "upmax":
            self.pos[1] += 10
            m.pos[1] -= 10
        elif self.direction == "leftmax" and m.direction == "rightmax":
            self.pos[0] += 10 
            m.pos[0] -= 10 
        elif self.direction == "rightmax" and m.direction == "leftmax":
            self.pos[0] -= 10
            m.pos[0] += 10
   
    def checkPos(self, m): #checks for collision in same pos, calls functions to handle collisions, changes movement
        x = m.pos[0]
        y = m.pos[1]
        if self.pos[0] == x and self.pos[1] == y:
            self.checkCollisions(m)
            m.getMovement(10,10) 
            self.getMovement(10,10) 
           






