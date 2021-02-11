print(abs(-15))
print(abs(15))          #Devuelve el valor absoluto de el número

print("---------------------------------------------------")

print(bool(0))
print(bool(1))          #Devuelve un valor booleano (true/false)

print("---------------------------------------------------")

print(dir("Hola"))      #Devulve un arreglo de funciones que se pueden hacer con un tipo de dato string

print("---------------------------------------------------")

sent = "Hola"
help(sent.upper)        #Devuelve la descripción de lo que hace esa función
help(sent.splitlines)  

print("---------------------------------------------------")

sent = "print('Hi')"
eval(sent)              #Evalua la cadena y si hay una función de Python la ejecuta (sólo si es una sola línea de código)

print("---------------------------------------------------")

exec(sent)              #Evalua la cadena y si hay una función de Python la ejecuta (Puede ejecutar múltiples líneas de código)

print("---------------------------------------------------")

a = 1
print(str(a))           #Convierte el tipo de dato a un String
print(float(a))         #Convierte el tipo de dato a un Flotante
print(int(a))           #Convierte el tipo de dato a un Entero