#Write a Python program to calculate the area of a trapezoid.
import math
print('Height:')
h = int(input())
print('Base, first value:')
fv = int(input())
print('Base, second value:')
sv = int(input())

area = (fv+sv)/2 * h
print('Expected Output:', area)