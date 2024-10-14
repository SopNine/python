
monedas_2e = int(input("Introduce la cantidad de monedas de 2 euros: "))

monedas_1e = int(input("Introduce la cantidad de monedas de 1 euro: "))

monedas_50c = int(input("Introduce la cantidad de monedas de 50 céntimos: "))

monedas_20c = int(input("Introduce la cantidad de monedas de 20 céntimos: "))

monedas_10c = int(input("Introduce la cantidad de monedas de 10 céntimos: "))

total_euros = (monedas_2e * 2) + (monedas_1e)
total_centimos = (monedas_50c * 50) + (monedas_20c * 20) + (monedas_10c * 10)

total_euros += total_centimos // 100  
total_centimos = total_centimos % 100

print(f"Tienes un total de {total_euros} euros y {total_centimos} céntimos.")

