class Padre:
    def __init__(self):
        print("Esta es la clase padre")
    def funcionPadre(self):
        print("Esta es la función padre")
    def prueba(self):
        print("Padre")

p = Padre()

p.funcionPadre()
print("------------")

class hijo(Padre):
    def __init__(self):
        print("Esta es la clase hijo")
    def funcionHijo(self):
        print("Esta es la función hijo")
    def prueba(self):                       #Sobreescribe la función para hacerla propia y la función con el mismo nombre que se heredó
        print("Hijo")                       #es borrada

h = hijo()

h.funcionHijo()
h.funcionPadre()
print("------------")
h.prueba()