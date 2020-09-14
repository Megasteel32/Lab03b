# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Angry Birds Simulator 4000
# Date:        9/6/2020

# Import math
from math import *

# Defining variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0
t1 = 0
t2 = 0
vx = 0
vy = 0
overall_velocity = 0
kinetic_energy = 0
mass = 3

# Requesting user input with this cool input thingy I learned
x1, y1 = input("What is the x and y value of the first point (seperate with a comma and space)? ").split(", ")
x1, y1 = [int(x1), int(y1)]
t1 = int(input("What is the time value of the first point? "))
x2, y2 = input("What is the x and y value of the second point (seperate with a comma and space)? ").split(", ")
x2, y2 = [int(x2), int(y2)]
t2 = int(input("What is the time value of the second point? "))

# Calculate vx and vy
vx = (x2 - x1)/(t2 - t1)
vy = (y2 - y1)/(t2 - t1)

# Calculate hypotenus thingy using math.hypot (well I already imported math so yeah dont need the math.)
overall_velocity = hypot(vx, vy)

# Calculate kinetic energy using 1/2 * mass * velocity squared
kinetic_energy = 0.5 * mass * overall_velocity**2

# Prints out the final stuff
print("The overall velocity of Red the angry bird (tm) is",round(overall_velocity,3),"meters per second",end=".\n")
print("The kinetic energy of Red the angry bird (tm) is",round(kinetic_energy,3),"Joules",end=".")