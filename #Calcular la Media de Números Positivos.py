#Arellano Martinez Luis Fernando 250152
#Calcular la Media de Números Positivos

def calcular_media():
    suma = 0.0
    contador = 0
    
    print("\n=== Calculadora de Media ===")
    print("Ingrese números positivos (para terminar, ingrese un número negativo):")
    
    while True:
        try:
            entrada = input("Número: ")
            n = float(entrada)
            
            if n < 0:
                if contador == 0:
                    print("\n¡Advertencia! No se ingresaron números positivos.")
                break
                
            if n > 0:
                suma += n
                contador += 1
                print(f"-> Número aceptado: {n:.2f}")
            else:
                print("¡El cero no se considera! Ingrese un número positivo o negativo para terminar.")
                
        except ValueError:
            print("¡Error! Por favor ingrese un número válido.")
    
    if contador > 0:
        media = suma / contador
        print("\n=== Resultados ===")
        print(f"Total de números ingresados: {contador}")
        print(f"Suma total: {suma:.2f}")
        print(f"Media aritmética: {media:.2f}")

# Ejecutar la función
calcular_media()