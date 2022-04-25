import math
input__angle=int(input("Enter angle between 0 to 345 with increment of 15 degree:"))
print(f"{input__angle})  {round(math.sin(input__angle),4)} {round(math.cos(input__angle),4)}")
#alternative way

from math import *
for i in range(0,360,15):
    print(i,"---", round(sin(i),4), round(cos(i),4))