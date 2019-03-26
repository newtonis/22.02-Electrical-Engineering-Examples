from math import *
from cmath import *

class Res:
    value = None
    def __init__(self,value =None):
        self.value = value
    def __floordiv__(self, other):
        return Res(self.value * other.value / (self.value + other.value))
    def __add__(self, other):
        return Res(self.value+other.value)
    def __mul__(self, other):
        return Res(self.value*other.value)
    def vdiv(self,r1,r2):
        return Res(r2.value/(r1.value + r2.value))
    __rmul__ = __mul__

L = 1
C = 0.2
R = 8
w = 5
s = 1j*w

Z1 = R
Z2 = 1/(s*C)
Z3 = s*L

V1 = rect(14.1,radians(0))
UC1 =  V1 *( Z2*Z3/(Z2+Z3))/((Z2*Z3/(Z2+Z3))+Z1)
I1 = rect(1.41, pi/2)
UC2 = I1 * Z2 * (Z1*Z3/(Z1+Z3))/((Z1*Z3/(Z1+Z3))+Z2)
def polarprint(name,var):
    print(name,hypot(var.real,var.imag),"/",degrees(atan2(var.imag,var.real)))
polarprint("UC1=",UC1)
polarprint("UC2=",UC2)

polarprint("UC=",UC1+UC2)
