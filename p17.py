
HH = int(input("Introduce la hora de partida (HH): "))
MM = int(input("Introduce los minutos de partida (MM): "))
SS = int(input("Introduce los segundos de partida (SS): "))

T = int(input("Introduce el tiempo de viaje en segundos: "))

total_segundos_partida = HH * 3600 + MM * 60 + SS

total_segundos_llegada = total_segundos_partida + T

HH_llegada = (total_segundos_llegada // 3600) % 24  
MM_llegada = (total_segundos_llegada % 3600) // 60  
SS_llegada = total_segundos_llegada % 60            

print(f"El ciclista llegará a la ciudad B a las {HH_llegada:02}:{MM_llegada:02}:{SS_llegada:02}")
