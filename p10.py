
calificacion1 = float(input("Introduce la primera calificación parcial: "))
calificacion2 = float(input("Introduce la segunda calificación parcial: "))
calificacion3 = float(input("Introduce la tercera calificación parcial: "))

promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3

calificacion_examen_final = float(input("Introduce la calificación del examen final: "))

calificacion_trabajo_final = float(input("Introduce la calificación del trabajo final: "))

calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)

print(f"\nLa calificación final en la materia de Algoritmos es: {calificacion_final:.2f}")
