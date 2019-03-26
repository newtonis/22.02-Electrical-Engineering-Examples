import math
import numpy
import matplotlib.pyplot as plt

#  Resolución de circuito RLC serie sobreamortiguado

# valores de los componentes
R = 25
L = 5
C = 0.01

# condiciones iniciales
VC0 = 12
IL0 = 0

w0 = math.sqrt(1/(L*C))  # frecuencia de resonancia
alpha = R/(2*L)          # factor de amortiguamiento

# las constantes de tiempo son las raices del polinomio caracteristico, que como el sistema es sobreamortiguado
# son reales, negativas y distintas entre si
[s1, s2] = numpy.roots([1, 2*alpha, w0**2])
s1 = -s1
s2 = -s2

# para obtener las constantes para terminar de resolver la EDO, aplicamos las condiciones iniciales
[a, b] = numpy.linalg.solve([[1, 1], [s1, s2]], [VC0, IL0])

# genero un vector con tiempos para evaluar las funciones y plotear
t = numpy.arange(0, 30, 0.01)

# evaluo las funciones que calcule en los puntos de t
uc = [a * math.exp(-s1 * tt) + b * math.exp(-s2*tt) for tt in t]
il = [-C*(a*s1*math.exp(-s1 * tt) + b*s2*math.exp(-s2*tt)) for tt in t]

# plt.plot(t, uc)
# plt.ylabel("Tensión (V)")

plt.plot(t, il)
plt.ylabel("Corriente (A)")

plt.xlabel("Tiempo (s)")

# pongo una grilla
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

# muestro el grafico que prepare
plt.show()
