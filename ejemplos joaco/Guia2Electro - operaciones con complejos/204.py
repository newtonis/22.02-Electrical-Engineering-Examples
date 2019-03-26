from math import *
from cmath import *
w = 400
IT = rect(10,radians(90))
s = w*1j

R = 20
C = 1250e-6
L = 10e-3

ZC = 1/(s*C)
ZL = s*L
ZA = (ZC*ZL)/(ZC+ZL)


VR = IT*R
VA = IT*ZA
IC = VA/ZC
IL = VA/ZL

def polarprint(name,var):
    print(name,hypot(var.real,var.imag),"/",degrees(atan2(var.imag,var.real)))
polarprint("VR = ",VR)
polarprint("VA =",VA)
polarprint("IC =",IC)
polarprint("IL =",IL)