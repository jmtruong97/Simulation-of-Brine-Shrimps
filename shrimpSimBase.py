#
# Author : Juanitta Truong
#
# shrimpSimBase.py - Basic simulation of brine shrimp for assignment, S2 2019. 
# 
# References
# def main:
#   File name: shrimpSimBase.py
#   Author: Valerie (Lecturer)
#   Date: 2/10/2019 – Base version for assignment
#   Location: Curtin University
#
#
# 
#

import random
import matplotlib.pyplot as plt
import numpy as np
import sys
from shrimp import Shrimp 

def checkRate(m, deathrate): #checks user's input, changes state of shrimp to dead depending on probability 
    if (random.randint(0,100)) <= deathrate:
        m.state = "dead"
        
def checkChance(m, XMAX, YMAX, agestep, reproducerate): #checks users input, adds newegg depending on probability and whether it's an adult
    newegg = None
    if ((random.randint(0,100)) <= reproducerate) and m.state == "adult":
        randX = np.random.randint(0,XMAX)
        randY = np.random.randint(0,YMAX)
        newegg = Shrimp([randX,randY], XMAX, YMAX, agestep)
    return newegg

def checkValid(XMAX, YMAX, population, agestep, timestep, deathrate, reproducerate): #checks if user's input is valid
    valid = False 
    if (XMAX > 0) and (YMAX > 0) and (population > 0) and (agestep > 0) and (timestep > 0) and (deathrate > 0) and (deathrate < 100) and (reproducerate > 0) and (reproducerate < 100):
        valid = True
    return valid
        
def main(): #main function that plots the shrimps
    monkeys = []
    try:
        if len(sys.argv) == 8:
            XMAX = int(sys.argv[1])
            YMAX = int(sys.argv[2])
            population = int(sys.argv[3])
            agestep = int(sys.argv[4])
            timestep = int(sys.argv[5])
            deathrate = int(sys.argv[6])
            reproducerate = int(sys.argv[7])
            if checkValid(XMAX, YMAX, population, agestep, timestep, deathrate, reproducerate) == True:
                 print('\nTank size: (',XMAX, ',',YMAX, ')')
                 print('\nShrimp Population: ', population)
                 print('\nAge Step: ', agestep, 'Day(s)')
                 print('\nTime Step: ', timestep, 'Day(s)')
                 print('\nDeath Rate is: ', deathrate, '%')
                 print('\nReproduction Rate: ', reproducerate, '%')
                 for i in range(population): #for loop in the range of user's input population
                      randX = np.random.randint(0,XMAX) 
                      randY = np.random.randint(0,YMAX) 
                      monkeys.append(Shrimp([randX,randY], XMAX, YMAX, agestep)) #imports 4 parameters from class Shrimp
                      
                 for i in range(timestep): #number iterations is user's input timestep
                      print("\n ### TIMESTEP ", i, "###")
                      for m in monkeys:
                          checkRate(m, deathrate)
                          m.stepChange() #calls to increase age and movement and state of shrimps
                          newegg = checkChance(m, XMAX, YMAX, agestep, reproducerate)
                          if newegg is not None:
                              monkeys.append(newegg)
                          for m2 in monkeys: 
                              m.checkPos(m2) #calls to check for collisions and to handle it
                          print(m.__str__()) #prints shrimps' states and coordinates at each timestep
                          plt.plot(m.pos[0], m.pos[1], m.getColor(), markersize=m.getSize())  #calls color and size functions
                          plt.xlim(0,XMAX) 
                          plt.ylim(0,YMAX)
                      plt.show()
            else:
                print('Arguments must be a positive integer or percentage less than 100%...')
        else:
            print('Not enough arguments...')
    except ValueError:
        print('Arguments must be an integer...')
    
if __name__ == "__main__": #lets the computer know to always start at the main and execute main before anything else
    main()
