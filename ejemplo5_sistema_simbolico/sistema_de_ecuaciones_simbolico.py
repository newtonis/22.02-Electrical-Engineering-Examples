## instalar sympy
# pip install sympy

import sympy as sp

## ingognitas y parámetros
v1, v2, vx, vout1, vfeed, vout = sp.symbols("v1 v2 vx vout1 vfeed vout")
r1, r2, r3, r4, r5, r6, r7, r8, r9 = sp.symbols("r1 r2 r3 r4 r5 r6 r7 r8 r9")


h = sp.solve([
    (vout1-v1)/r3-(v1-vx)/r4,# = 0
    (vx-v2)/r6-v2/r7,# = 0
    (vfeed-vx)/r5-(vx-v2)/r6-(vx-v1)/r4,# = 0
    vout1/r1+vout/r2# = 0
    ],
    (vx, vout1, vfeed, vout)
)

print(sp.pretty(h[vout]))

