from random import uniform
from math import hypot

n = int(input('input n:'))
m = 0

for i in range(n):
    d = hypot(uniform(0,1),uniform(0,1))
    if d < 1:
        m+=1

print(float(m*4 /n))
