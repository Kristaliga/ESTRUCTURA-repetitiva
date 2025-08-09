#Arellano Martinez Luis Fernando 250152
#Obtener el genero valido ya sea hombre o mujer y encontrar al mas joven

def obtener_genero_valido(num_usuario):
    """Obtiene un género válido (H o M)."""
    while True:
        genero = input(f"Ingrese el género del usuario {num_usuario} (H para hombre, M para mujer): ").upper().strip()
        if genero in ['H', 'M']:
            return genero
        print("Error: Ingrese 'H' para hombre o 'M' para mujer.")

def obtener_edad_valida(num_usuario):
    """Obtiene una edad válida (entero positivo)."""
    while True:
        try:
            edad = int(input(f"Ingrese la edad del usuario {num_usuario}: "))
            if edad > 0:
                return edad
            print("Error: La edad debe ser un número positivo.")
        except ValueError:
            print("Error: Ingrese un número entero válido para la edad.")
def main():
    """Programa principal para contar géneros y encontrar el usuario más joven."""
    # Inicializar contadores
    hombres = 0
    mujeres = 0
    usuarios_validos = 0
    edad_minima = float('inf')  
    # Inicializar con infinito para encontrar el mínimo
    genero_mas_joven = None
    
    print("Ingrese el género y la edad de 5 usuarios:")
    
    # Procesar 5 usuarios
    while usuarios_validos < 5:
        usuarios_validos += 1
        genero = obtener_genero_valido(usuarios_validos)
        edad = obtener_edad_valida(usuarios_validos)
        
        # Contar género
        if genero == 'H':
            hombres += 1
        else:  # genero == 'M'
            mujeres += 1
        
        # Actualizar edad mínima y género asociado
        if edad < edad_minima:
            edad_minima = edad
            genero_mas_joven = genero
    
    # Imprimir resultados
    print("\nResultados:")
    print(f"Hombres: {hombres}")
    print(f"Mujeres: {mujeres}")
    genero_texto = "Hombre" if genero_mas_joven == 'H' else "Mujer"
    print(f"El usuario más joven tiene {edad_minima} años y es {genero_texto}")

# Ejecutar el programa
if __name__ == "__main__":
    main()