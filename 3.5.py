###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = input('The value of side a: ')
a = int(a)
b = input('The value of side b: ')
b = int(b)

diagonal = math.sqrt(a**2 + b**2)
print('The length of said rectangle is: ', diagonal)