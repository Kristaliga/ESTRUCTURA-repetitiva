# Arellano Martinez Luis Fernando 250152
#Obtener numero  valido positivo 

def obtener_numero_valido():
    """Obtiene un número entero válido entre 0 y 32,000."""
    while True:
        try:
            numero = int(input("Ingrese un número entero (0 a 32000): "))
            if 0 <= numero <= 32000:
                return numero
            print("El número debe estar entre 0 y 32000. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def contar_cifras(numero):
    """Cuenta el número de cifras de un número entero."""
    if numero == 0:
        return 1
    return len(str(abs(numero)))

def main():
    """Programa principal para contar cifras."""
    print("Sistema para contar cifras de un número")
    numero = obtener_numero_valido()
    cifras = contar_cifras(numero)
    print(f"{cifras} {'cifra' if cifras == 1 else 'cifras'}")

# Ejecutar el programa
if __name__ == "__main__":
    main()