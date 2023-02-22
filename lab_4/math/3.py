#Write a Python program to calculate the area of regular polygon
import math
print('Input number of sides:')
n = int(input())
print('Input the length of a side:')
s = int(input())
p = n * s
a = 2 * math.tan((180/n) * (math.pi/180))
b = s / a
A = n*s*b * (1/2)
print('The area of the polygon is:', int(A))