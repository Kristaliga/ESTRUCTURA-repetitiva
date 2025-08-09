#Arellano Martinez Luis Fernando 250152
#Pida al usuario escribir un entero diferente de cero y después imprima su recíproco.

def obtener_entero_no_cero():
    """Obtiene un número entero diferente de cero."""
    while True:
        try:
            numero = int(input("Ingrese un número entero diferente de cero: "))
            if numero == 0:
                print("Error: El número no puede ser cero. Intente de nuevo.")
                continue
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def main():
    """Programa principal para calcular el recíproco."""
    print("Sistema para calcular el recíproco de un número entero")
    numero = obtener_entero_no_cero()
    reciproco = 1 / numero
    print(f"El recíproco de {numero} es {reciproco:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()