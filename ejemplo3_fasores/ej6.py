from math import acos, sin
from numpy import conj
from plotFasor import *

k = 1000

s1 = 60*k + 60*k*sin(acos(0.75))*1j
s2 = -20*k*1j
s3 = 10*k + 10*k*sin(acos(0.6))

s = s1 + s2 + s3
v = 220

i = conj(s / v)

print("i = ", printComplex(i), "A")