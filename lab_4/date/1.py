#Write a Python program to subtract five days from current date.
import datetime

time_now = datetime.datetime.now()
print(time_now)
FiveDaysBefore = time_now.day - 5
new_time = datetime.datetime(time_now.year, time_now.month, FiveDaysBefore)
print(new_time)