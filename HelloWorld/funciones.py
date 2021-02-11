def HolaMundo():
    print("Hola Mundo")

HolaMundo()

def Saludo(nombre):
    print("Hola " + nombre + "!")

Saludo("Luis")

def suma(num1, num2):
    print("La suma es: ", (num1 + num2))

suma(5, 15)

def getSuma(num1, num2):
    return num1 + num2

print("La suma retornada es: ", getSuma(10, 30))