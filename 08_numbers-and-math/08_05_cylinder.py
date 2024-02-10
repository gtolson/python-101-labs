# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

import math

radius = 3.14
height = 5
pi = math.pi

volume = pi * radius ** 2 * height
volume = str(volume)

surface_area = (2 * pi * radius * height) + (2 * pi * radius ** 2)
surface_area = str(surface_area)

print(f"The volume of the cylinder is {volume}")
print(f"The surface area of the cylinder is {surface_area}")