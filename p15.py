
A = float(input("Introduce el valor de A: "))

B = float(input("Introduce el valor de B: "))

temp = A
A = B
B = temp

print(f"El valor final de A es: {A:.2f}")
print(f"El valor final de B es: {B:.2f}")
