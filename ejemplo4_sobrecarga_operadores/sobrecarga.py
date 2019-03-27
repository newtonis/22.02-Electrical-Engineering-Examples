## lo unico importante de ejemplo es la sobrecarga de operadores (el operador //)
## No es importante el cálculo que esta haciendo este ejemplo

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

k=1e3
Rs = Res(10*k)
Rf = Res(1*k)
RL = Res(10*k)
r = Res(100)

ro = Res(1*k)
ri = Res(100*k)
Avol = 1e4

T = Res(None)
R1aux0 = ro+RL
## aca pueden observar la sobrecarga del //
R2aux0 = r//(Rf+Rs//ri)
R1aux1 = Rf
R2aux1 = Rs//ri
T= T.vdiv(R1aux0,R2aux0)*T.vdiv(R1aux1,R2aux1)
T.value= T.value*-Avol
print(T.value)