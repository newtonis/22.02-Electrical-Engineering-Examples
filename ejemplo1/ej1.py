from numpy import conj, angle, arange, linspace
import matplotlib.pyplot as plt
from plotFasor import *

"""
b : blue.
g : green.
r : red.
c : cyan.
m : magenta.
y : yellow.
k : black.
w : white
"""

zr = 20
zl = 100j
zc = -60j

v = 220
i = v / paralell(zr, zl + zc)

vr = v
i1 = vr / zr

i2 = v / (zl + zc)
vl = i2 * zl
vc = i2 * zc

sr = vr * conj(i1)
sl = vl * conj(i2)
sc = vc * conj(i2)

sf = -v * conj(i)

ax = plt.subplot(111, projection='polar')

drawLine(sr, "r", "Resistencia")
drawLine(sl, "g", "Bobina")
drawLine(sc, "b", "Capacitor")
drawLine(sf, "m", "Fuente")

ax.grid(True)
ax.set_title("Potencias complejas (kW + jkVAR = kVA)", va='bottom')
ax.legend()

plt.show()

# print(sr, sl, sc, sf)

# print(sr + sl + sc + sf)