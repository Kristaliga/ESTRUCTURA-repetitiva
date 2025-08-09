#Arellano Martinez Luis Fernando 250152
#Inicializar la variable para el numero mayor con un valor muy pequeño

mayor = float('-inf')


# Leer 5 números usando bucle for
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    # Comparar el número actual con el mayor encontrado hasta ahí
    if num > mayor:
        mayor = num
        contador +=1  # Solo incrementar cuando encontramos un nuevo mayor
    acumulador +=num  # Sumar todos los números independientemente

# Imprimir resultados
print(f"El número mayor es: {mayor}")
print(f"El número de veces que cambió el número mayor: {contador}")
print(f"La suma de los números es: {acumulador}")