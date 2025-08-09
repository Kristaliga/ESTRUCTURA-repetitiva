#Arellano Martinez Luis Fernando 250152
# Algoritmo para sumar monedas de 5, 10, 20 y 50 sucres

print("Ingrese la cantidad de monedas de cada denominación:")

# Solicitar al usuario la cantidad de cada tipo de moneda
monedas_5 = int(input("Monedas de 5 sucres: "))
monedas_10 = int(input("Monedas de 10 sucres: "))
monedas_20 = int(input("Monedas de 20 sucres: "))
monedas_50 = int(input("Monedas de 50 sucres: "))

# Calcular el total
total = (monedas_5 * 5) + (monedas_10 * 10) + (monedas_20 * 20) + (monedas_50 * 50)

# Mostrar el resultado
print(f"\nEl total de dinero es: {total} sucres")