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


def paralell(a, b):
    return (a*b)/(a+b)


def drawLine(vector, color, title):
    r = linspace(0, abs(vector)/1000, 100)
    theta = [angle(vector)] * len(r)

    plt.plot(theta, r, color)
    plt.plot([angle(vector)], [abs(vector)/1000], color + "o", alpha=0.5, label = title)


def printComplex(complexNum):
    mod = round(abs(complexNum), 2)
    phase = round(angle(complexNum) / pi * 180.0, 2)

    mod = str(mod)
    phase = str(phase)

    return mod + " < " + phase + "°"
