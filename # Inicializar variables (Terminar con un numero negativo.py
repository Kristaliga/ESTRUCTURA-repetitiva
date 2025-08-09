#Arellano Martinez Luis Fernando 250152
# Inicializar variables (Terminar con un numero negativo)

numeros = []
suma = 0.0
contador = 0

print("Ingrese números positivos (termine con un número negativo):")

while True:
    try:
        numero = float(input("Número: "))
        if numero < 0:
            break  # Terminar si se ingresa un negativo
        numeros.append(numero)
        suma += numero
        contador += 1
    except ValueError:
        print("¡Error! Ingrese un número válido.")

# Calcular la media si hay números válidos
if contador > 0:
    media = suma / contador
    print(f"\nLista ingresada: {numeros}")
    print(f"Cantidad de números válidos: {contador}")
    print(f"Suma total: {suma}")
    print(f"Media (promedio): {media:.2f}")  # Redondeado a 2 decimales
else:
    print("No se ingresaron números válidos.")