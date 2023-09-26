#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math 
r = input("radius")
h = input("hight")
r = int(r)
h= int(h)
sa = math.pi*r*(r+math.sqrt(h**2+r**2))
print(sa)
