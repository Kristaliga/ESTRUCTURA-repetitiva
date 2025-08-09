#Arellano Martinez Luis Fernando 250152
# Verificar si un Número es Par o Impar dentro del Rango [1, 50]

while True:
    try:
        n = int(input("Ingrese un número entre 1 y 50: "))
        if 1 <= n <= 50:
            if n % 2 == 0:
                print("Número par")
            else:
                print("Número impar")
            break  # Termina el bucle si el número es válido
        else:
            print("¡Error! El número debe estar entre 1 y 50.")
    except ValueError:
        print("¡Error! Ingrese un número entero válido.")