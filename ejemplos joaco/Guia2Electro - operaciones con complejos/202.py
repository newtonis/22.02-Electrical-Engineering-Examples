from math import *
from cmath import *
w = 2*pi*50
C = 50e-6
R=20
L=100e-3
UAB = rect(500,radians(130))
s= 1j*w

ZC = 1/(s*C)
ZR = R
ZL = s*L

YC = 1/ZC
YR = 1/ZR
YL = 1/ZL
Y = YC + YR + YL
Z = 1/Y
I =  UAB/Z
IC = UAB/ZC
IR = UAB/ZR
IL = UAB/ZL

def polarprint(name,var):
    print(name,hypot(var.real,var.imag),"/",degrees(atan2(var.imag,var.real)))
polarprint("YC =",YC)
polarprint("YR =",YR)
polarprint("YL =",YL)
polarprint("Y =",Y)
polarprint("Z=",Z)
polarprint("I=",I)
polarprint("IC =",IC)
polarprint("IR =",IR)
polarprint("IL =",IL)

