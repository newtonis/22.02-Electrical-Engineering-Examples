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
R1 = Res(1*k)
R2 = Res(1*k)
R3 = Res(100*k)
R4 = Res(1*k)
RL = Res(2*k)
ro = Res(1*k)
ri = Res(100*k)
Avol = 1e4

T = Res(None)
R1aux0 = ro
## aca pueden observar la sobrecarga del //
R2aux0 = (RL//(R3+(R4//(R2+(R1//ri)))))
R1aux1 = R3
R2aux1 = (R4//(R2+(R1//ri)))
R1aux2 = R2
R2aux2 = R1//ri
T= T.vdiv(R1aux0,R2aux0)*T.vdiv(R1aux1,R2aux1)*T.vdiv(R1aux2,R2aux2)
T.value= T.value*-Avol
print(T.value)
