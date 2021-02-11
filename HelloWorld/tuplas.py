tup = ('Naranjas', 'Manzanas', 'Platanos')
print(tup)

#tup[0] = "cerezas"     Usar una tupla así dará un error porque no se pueden modificar

print(tup[0])
print(tup[1])
print(tup[0:2])

tup2 = (12,14)

tup3 = tup + tup2

print(tup3)

del tup3        #Esto borra la variable del programa

print(len(tup))
tup = ("Hola")

print(tup*4)