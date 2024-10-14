
total_compra = float(input("Introduce el total de la compra: "))

descuento = total_compra * 0.15

total_a_pagar = total_compra - descuento

print(f"\nTotal de la compra: {total_compra:.2f}")
print(f"Descuento (15%): {descuento:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")
