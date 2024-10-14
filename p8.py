
sueldo_base = float(input("Introduce el sueldo base del vendedor: "))

venta1 = float(input("Introduce el monto de la primera venta: "))
venta2 = float(input("Introduce el monto de la segunda venta: "))
venta3 = float(input("Introduce el monto de la tercera venta: "))

total_ventas = venta1 + venta2 + venta3

comisiones = total_ventas * 0.10

sueldo_total = sueldo_base + comisiones

print(f"\nTotal de ventas: {total_ventas:.2f}")
print(f"Comisiones (10%): {comisiones:.2f}")
print(f"Sueldo total del vendedor: {sueldo_total:.2f}")
