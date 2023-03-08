#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os

for i in range(26):
    name = chr(i + 65) + ".txt"
    print(name)
    file = open(name, 'w')
    file.close()