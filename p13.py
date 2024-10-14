import math 

numero = float(input("Introduce un número: "))

# Paso 3: Calcular la raíz cuadrada
raiz_cuadrada = math.sqrt(numero)

# Paso 4: Calcular la raíz cúbica
raiz_cubica = numero ** (1/3)  # Alternativa: math.pow(numero, 1/3)

# Paso 5: Mostrar los resultados
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica:.2f}")
