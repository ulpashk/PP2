#Write a Python program to print yesterday, today, tomorrow.
import datetime
timeNow = datetime.datetime.now()

yday = timeNow.day - 1
yesterday = datetime.datetime(timeNow.year, timeNow.month, yday)
print("Yesterday:", yesterday)

print("Today:", timeNow)

trow = timeNow.day + 1
tomorrow = datetime.datetime(timeNow.year, timeNow.month, trow)
print("Tomorrow:", tomorrow)