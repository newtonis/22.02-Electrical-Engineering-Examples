from math import *
from cmath import *

V1 = rect(40,radians(0))
V2 = rect(50,radians(90))

ZR = 20
ZC = -1j*20
ZL = 1j*10

num = (V1/ZR) + (V2/ZL)
den = (1/ZC)+1/(ZR)+1/(ZL)
VB = num/den

def polarprint(name,var):
    print(name,hypot(var.real,var.imag),"/",degrees(atan2(var.imag,var.real)))

polarprint("VB =",VB)

IR = (V1-VB)/(ZR)
IL = (V2-VB)/(ZL)
IC = VB/(ZC)

polarprint("IR =",IR)
polarprint("IL =",IL)
polarprint("IC =",IC)
