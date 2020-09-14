# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Formula Scavenger Hunt 3.0 Part B
# Date:        9/6/2020

# Defining variables
velocity = 0
kine_viscosity = 0
lin_dimension = 0
reynolds_number = 0

# Requesting user input
velocity = int(input("What is the velocity of the fluid? "))
kine_viscosity = int(input("What is the kinematic viscosity of the fluid? "))
lin_dimension = int(input("What is the linear dimension of the fluid? "))

# Calculating Reynold's Number with velocity*linear dimension / viscosity
reynolds_number = (velocity*lin_dimension)/kine_viscosity

# Printing final output
print("The Reynold's Number for the given fluid is",reynolds_number,end=".")
