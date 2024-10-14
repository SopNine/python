
d = float(input("Introduce la distancia entre los dos vehículos (en km): "))

v1 = float(input("Introduce la velocidad del vehículo más lento (v1 en km/h): "))

v2 = float(input("Introduce la velocidad del vehículo más rápido (v2 en km/h): "))


if v2 > v1:
    tiempo_horas = d / (v2 - v1)
    
    tiempo_minutos = tiempo_horas * 60
    
    print(f"El vehículo más rápido alcanzará al más lento en: {tiempo_minutos:.2f} minutos")
else:
    print("La velocidad del vehículo más rápido debe ser mayor que la del más lento.")
