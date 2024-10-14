
correctas = int(input("Introduce la cantidad de respuestas correctas: "))

incorrectas = int(input("Introduce la cantidad de respuestas incorrectas: "))

blanco = int(input("Introduce la cantidad de respuestas en blanco: "))

nota_final = (correctas * 5) + (incorrectas * -1) + (blanco * 0)

print(f"La nota final del estudiante es: {nota_final}")
