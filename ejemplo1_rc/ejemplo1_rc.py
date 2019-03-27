import math
import numpy
import matplotlib.pyplot as plt

#  Descarga de un capacitor

# valores de los componentes
R = 25
C = 0.01

# condiciones iniciales
VC0 = 12

tau = R*C  # constante de tiempo

# genero un vector con tiempos para evaluar las funciones y plotear
t = numpy.arange(0, 6*tau, tau/100)

# evaluo la funcion que calcule en los puntos de t
uc = [VC0 * math.exp(-tt/tau) for tt in t]

plt.plot(t, uc)
plt.ylabel("Tensión (V)")
plt.xlabel("Tiempo (s)")

# pongo una grilla
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

# muestro el grafico que prepare
plt.show()
