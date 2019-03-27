from numpy import conj, angle, arange, linspace
import matplotlib.pyplot as plt
from math import pi

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

## paralelo de resistencias
def paralell(a, b):
    return (a*b)/(a+b)


def drawLine(vector, color, title):
    # r es un vector con 100 elemenots con las coordenadas polares (la componente radial) de la flecha fasorial
    r = linspace(0, abs(vector)/1000, 100) # dividmos por 1000 para tener la potencia en kW
    # theta es un vector con len(r) veces el mismo valor, porque en coordenadas polares
    # la flecha fasorial tiene siempre la misma componente angular
    theta = [angle(vector)] * len(r)

    # ploteamos colocando en primer lugar el vector con los componentes angulares
    # y en el segundo el vector con los componentes radiales
    plt.plot(theta, r, color)
    # ploteamos en el extremo de la flecha un puntito de color
    plt.plot([angle(vector)], [abs(vector)/1000], color + "o", alpha=0.5, label = title)


def printComplex(complexNum):
    # mostramos un numero complejo con módulo y fase
    mod = round(abs(complexNum), 2)
    phase = round(angle(complexNum) / pi * 180.0, 2)

    mod = str(mod)
    phase = str(phase)

    return mod + " < " + phase + "°"
