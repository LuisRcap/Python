c = 0

while c < 5:
    print(c)
    c = c + 1

print("------------")

c = 0
while(c < 5):
    print(c)
    if(c == 3):
        break
    c += 1

print("------------")

c = 0
while(c < 5):
    c += 1
    if(c == 3):
        continue
    print(c)

print("------------")

c = 0
while(c < 5):
    c += 1
    if(c == 3):
        pass
    print(c)