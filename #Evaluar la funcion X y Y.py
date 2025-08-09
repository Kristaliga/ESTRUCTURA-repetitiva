#Arellano Martinez Luis Fernando 250152
#Evaluar la funcion 

def evaluar_funcion(x):
    """Evalúa la función y = 4x^2 - 16x + 15."""
    return 4 * x ** 2 - 16 * x + 15

def main():
    """Programa principal para evaluar la función en el rango de 1 a 2."""
    print("Sistema para evaluar la función y = 4x^2 - 16x + 15")
    print("Valor de X  Valor de Y")
    
    x = 1.0
    while x <= 2.0:
        y = evaluar_funcion(x)
        estado = "Positivo" if y > 0 else "No Positivo"
        print(f"{x:.1f}        {y:.2f}      {estado}")
        x += 0.1  # Incremento de 0.1

# Ejecutar el programa
if __name__ == "__main__":
    main()