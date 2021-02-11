nombre = "Miguel"

print(nombre + " tiene 15 años")

sent = "%s tiene 15 años"

print(sent)
print(sent%nombre)

sent = "%s %s es el presidente de los US"
print(sent%("Joe", "Biden"))

sent = "%s tiene %d años"
print(sent%(nombre,15))