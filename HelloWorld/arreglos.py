shoplist= ["Manzanas", "Naranjas", "Platanos", "Queso"]
print(shoplist)

print(shoplist[0])
print(shoplist[2])
print(shoplist[3])
print(shoplist[1])

print(shoplist[0:2])
print(shoplist[0:3])

shoplist.append("Mora azul")

print(shoplist)

shoplist[0] = "Cerezas"

print(shoplist)

del shoplist[1]

print(shoplist)
print(len(shoplist))

shoplist2 = ["Pan", "Mermelada", "Mantequilla"]

print(shoplist + shoplist2)

print(shoplist*2)

listNum = [1, 4, 7, 23, 6]
print(max(listNum))
print(min(listNum))