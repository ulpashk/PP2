#Write a Python program to calculate two date difference in seconds.

import datetime
y = int(input())
m = int(input())
d = int(input())
h = int(input())
minu = int(input())
sec = int(input())

y1,m1,d1,h1,minu1,sec1 = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
#x = datetime.datetime(2013,12,30,23,59,59)
x = datetime.datetime(y,m,d,h,minu,sec)
#y = datetime.datetime(2013,12,31,23,59,59)
y = datetime.datetime(y1,m1,d1,h1,minu1,sec1)
print((y-x).total_seconds())