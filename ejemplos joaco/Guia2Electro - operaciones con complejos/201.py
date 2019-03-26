from math import *
from cmath import *
w = 2*pi*50
ZAB = 20
L1 = 90e-3
C1 = 320e-6
ZBC = 1/(1j*w*C1)
ZCD = 15
ZDE = 1j*w*L1
ZTOT = ZAB + ZBC + ZCD + ZDE
YTOT = 1/ZTOT
UAE = rect(100,radians(30))
I = UAE/ZTOT
UAB = I*ZAB
UBC = I*ZBC
UCD = I*ZCD
UDE = I*ZDE

def polarprint(name,var):
    print(name,hypot(var.real,var.imag),"/",degrees(atan2(var.imag,var.real)))

polarprint("ZAB =",ZAB)
polarprint("ZBC =",ZBC)
polarprint("ZCD =",ZCD)
polarprint("ZDE =",ZDE)
polarprint("Z =",ZTOT)
polarprint("Y =",YTOT)
polarprint("I =",I)
polarprint("UAB =",UAB)
polarprint("UBC=",UBC)
polarprint("UCD=",UCD)
polarprint("UDE=",UDE)
