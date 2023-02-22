#Write a Python program to drop microseconds from datetime.

import datetime

timeNow = datetime.datetime.now().replace(microsecond = 0)

print(timeNow)