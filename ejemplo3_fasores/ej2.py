import matplotlib.pyplot as plt
from plotFasor import *

## variables del problema
ifuente = 5
w = 2

r0 = 2
r1 = 1
r2 = 2

c = 0.25
l = 0.5

zl = 1j * w * l
zc = 1 / (1j * w * c)

z1 = r1 + zl
z2 = r2 + zc

i1 = ifuente * z2 / (z1 + z2)
i2 = ifuente * z1 / (z1 + z2)

## corrientes complejas
print("i1 = ", printComplex(i1))
print("i2 = ", printComplex(i2))

## cuenterio
vfuente = -ifuente * (paralell(r1 + zl, r2 + zc) + 2)

sfuente = vfuente * conj(ifuente)

vr0 = ifuente * r0
vr1 = i1 * r1
vr2 = i2 * r2

sr0 = vr0 * conj(ifuente)
sr1 = vr1 * conj(i1)
sr2 = vr2 * conj(i2)

vb = i1 * zl
vc = i2 * zc


sl = vb * conj(i1)
sc = vc * conj(i2)


ax = plt.subplot(111, projection='polar')

## dibujamos las potencias complejas

drawLine(sr0, "r", "R0")
drawLine(sr1, "g", "R1")
drawLine(sr2, "b", "R2")
drawLine(sl, "c", "L")
drawLine(sc, "m", "C")
drawLine(sfuente, "y", "F")

print("sr0 = ", printComplex(sr0))
print("sr1 = ", printComplex(sr1))
print("sr2 = ", printComplex(sr2))
print("s1 = ", printComplex(sl))
print("sc = ", printComplex(sc))
print("sfuente = ", printComplex(sfuente))

print("ptotal = ", printComplex(sr0 + sr1 + sr2 + sl + sc + sfuente))

ax.grid(True)
ax.set_title("Potencias complejas (kW + jkVAR = kVA)", va='bottom')
ax.legend()

plt.show()