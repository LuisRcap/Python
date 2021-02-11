class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def getNombre(self):
        print("Tu nombre es: " + self.nombre)
    def getEdad(self):
        print("Tu edad es: " + self.edad)

p1 = Persona("Miguel", "22")

p1.getNombre()
p1.getEdad()