from numpy import conj, angle, arange, linspace
import matplotlib.pyplot as plt
from plotFasor import *

"""
colores maplotlib!
b : blue.
g : green.
r : red.
c : cyan.
m : magenta.
y : yellow.
k : black.
w : white
"""

## impedancias
zr = 20
zl = 100j
zc = -60j

## despejamos variables de interés
v = 220
i = v / paralell(zr, zl + zc)

print("i = ", printComplex(i))

vr = v
i1 = vr / zr

i2 = v / (zl + zc)
vl = i2 * zl
vc = i2 * zc

## potencias complejas!
sr = vr * conj(i1)
sl = vl * conj(i2)
sc = vc * conj(i2)
sf = -v * conj(i)


ax = plt.subplot(111, projection='polar')

print("sr = ", printComplex(sr))
print("sl = ", printComplex(sl))
print("sc = ", printComplex(sc))
print("sf = ", printComplex(sf))
print("stotal = ", printComplex(sr + sl + sc + sf))

## Dibuajamos los fasores con funciones de plotFasor.py (en la misma carpeta)

drawLine(sr, "r", "Resistencia")
drawLine(sl, "g", "Bobina")
drawLine(sc, "b", "Capacitor")
drawLine(sf, "m", "Fuente")

## agregamos grid, leyenda y titulo

ax.grid(True)
ax.set_title("Potencias complejas (kW + jkVAR = kVA)", va='bottom')
ax.legend()

## mostramos to-do. También se podría guardar en un archivo png directamente
plt.show()
