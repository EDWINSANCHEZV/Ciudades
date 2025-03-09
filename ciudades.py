import random

# Definir dimensiones de la matriz
num_ciudades = 3   # Número de ciudades
num_semanas = 2    # Número de semanas
num_dias = 7       # Días de la semana (Lunes - Domingo)

# Crear una matriz 3D con temperaturas aleatorias entre 15°C y 35°C
matriz_temperaturas = []
for ciudad in range(num_ciudades):
    semanas = []
    for semana in range(num_semanas):
        dias = [random.randint(15, 35) for _ in range(num_dias)]
        semanas.append(dias)
    matriz_temperaturas.append(semanas)

# Mostrar las temperaturas generadas
print("\n Temperaturas registradas:")
for ciudad in range(num_ciudades):
    print(f"\n Ciudad {ciudad + 1}:")
    for semana in range(num_semanas):
        print(f"   Semana {semana + 1}: {matriz_temperaturas[ciudad][semana]}")

# Calcular y mostrar los promedios de temperatura por ciudad y semana
print("\n Promedios de temperatura por ciudad y semana:")
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        suma_temperaturas = sum(matriz_temperaturas[ciudad][semana])
        promedio = suma_temperaturas / num_dias
        print(f" Ciudad {ciudad+1},  Semana {semana+1}: Promedio = {promedio:.2f}°C")
