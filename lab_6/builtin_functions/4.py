#Write a Python program that invoke square root function after specific milliseconds
import time 
import math 
n = int(input())
milisec = int(input())
time.sleep(milisec * 10 ** (-3))
sqr_root = math.sqrt(n)
print("Square root of", n, "after", milisec, "miliseconds is:", sqr_root)