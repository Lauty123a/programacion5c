import random

estudiantes = ["juan maria", "carlitos", "jose", "valentin", "broca"]
orden_exposicion = []

for _ in range(len(estudiantes)):
    indice = random.randint(0, len(estudiantes) - 1)
    estudiante_elegido = estudiantes[indice]
    orden_exposicion.append(estudiante_elegido)
    del estudiantes[indice]

print("Orden de exposición:")
for i, estudiante in enumerate(orden_exposicion, 1):
    print(f"{i}. {estudiante}")