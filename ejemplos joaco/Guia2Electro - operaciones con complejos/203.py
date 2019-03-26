from math import *
from cmath import *
w = 2*pi*50
UAB = rect(141,radians(60))
ZR = 10
ZL = 30*1j
ZC = -30*1j
Z= ZR+ZC+ZL
I= UAB/Z

UR = I*ZR
UL = I*ZL
UC = I*ZC

def polarprint(name,var):
    print(name,hypot(var.real,var.imag),"/",degrees(atan2(var.imag,var.real)))
polarprint("I=",I)
polarprint("UR=",UR)
polarprint("UL=",UL)
polarprint("UC=",UC)
