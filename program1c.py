# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Formula Scavenger Hunt 3.0 Part C
# Date:        9/6/2020

# Define variables
sb_constant = 5.67*10**-8
temperature = 0
energy_radiated = 0

# Request user input
temperature = int(input("What is the temperature of the black body in Kelvin? "))

# Calculate energy radiated with temperature to the fourth power times the stefan-boltzmann constant

energy_radiated = temperature**4 * sb_constant

# Print result
print("The energy radiated from the black body across all wavelenghts is",energy_radiated,end=".")