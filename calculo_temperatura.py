def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad en base a los datos proporcionados.

    :param datos: Un diccionario donde las claves son los nombres de las ciudades
                  y los valores son listas con las temperaturas semanales.
    :return: Un diccionario con las ciudades y sus temperaturas promedio.
    """
    promedios = {}  # Diccionario para almacenar los resultados

    for ciudad, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)  # Suma las temperaturas y divide por la cantidad
        promedios[ciudad] = round(promedio, 2)  # Redondea el resultado a 2 decimales

    return promedios


# Datos de ejemplo: temperaturas de 3 ciudades en 4 semanas
datos_ciudades = {
    "Quito": [15, 17, 16, 14],
    "Guayaquil": [28, 30, 29, 27],
    "Cuenca": [12, 14, 13, 11]
}

# Prueba de la función
resultado = calcular_temperatura_promedio(datos_ciudades)
print("Temperaturas promedio por ciudad:", resultado)