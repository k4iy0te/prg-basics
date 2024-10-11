import math

height = input('Enter your height in meters: ')
height = int(height)
distance= int(3.57 * math.sqrt(height))

print(f"The distance to the horizon from a height of {height} meters is approximately {distance:.2f} kilometers!")

