# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Formula Scavenger Hunt 3.0 Part A
# Date:        9/6/2020

# Defining variables (yeah I know I don't have to do this here but it helps me later)
kinetic_energy = 0
mass = 0
velocity = 0

# Requesting user input and setting floats to integers
mass = int(input("What is the mass of the object? "))
velocity = int(input("What is the velocity of the object? "))

# Calculating kinetic energy with 1/2 * mass * velocity squared
kinetic_energy = (0.5 * mass * velocity**2)

# Printing result
print("The kinetic energy of the object with mass",mass,"and velocity",velocity,"is",kinetic_energy,"Joules.")