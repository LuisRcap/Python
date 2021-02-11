estudiantes = ["Juan", 12, "María", 13, "Memo", 15]

estudiantes = {
    "Juan": 12,
    "María": 13,
    "Memo": 15
}

print(estudiantes)

print(estudiantes["María"])
print(estudiantes["Juan"])

estudiantes["María"] = 15

print(estudiantes["María"])

del estudiantes["Memo"]
print(estudiantes)
print(len(estudiantes))

estudiantes = {
    "Juan": 12,
    "Juan": 14,
    "Juan": 16
}

print(estudiantes["Juan"])