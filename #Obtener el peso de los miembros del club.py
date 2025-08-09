#Arellano Martinez Luis Fernando 250152
#Obtener el peso de los miembros del club 

def obtener_peso_valido(mensaje):
    """Obtiene un peso válido (numérico y no negativo)."""
    while True:
        try:
            peso = float(input(mensaje))
            if peso < 0:
                print("El peso no puede ser negativo. Intente de nuevo.")
                continue
            return peso
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

def calcular_promedio_pesajes():
    """Calcula el promedio de los pesajes en 10 básculas."""
    total = 0.0
    for i in range(1, 11):
        mensaje = f"Ingrese el peso en la báscula {i} (kg): "
        peso = obtener_peso_valido(mensaje)
        total += peso
    return total / 10

def procesar_miembro(numero_miembro):
    """Procesa los datos de un miembro y determina el cambio de peso."""
    print(f"\n--- Miembro {numero_miembro} ---")
    peso_anterior = obtener_peso_valido("Ingrese el peso anterior (kg): ")
    print("Ingrese los pesos en las 10 básculas:")
    promedio_actual = calcular_promedio_pesajes()
    
    diferencia = promedio_actual - peso_anterior
    if diferencia > 0:
        estado = "SUBIO"
        cantidad = diferencia
    else:
        estado = "BAJO"
        cantidad = -diferencia
    
    print(f"{estado}: {cantidad:.2f} kg")
    return estado, cantidad

def control_peso_club():
    """Sistema principal para procesar los 5 miembros."""
    print("Sistema de control de peso del club contra la obesidad")
    for miembro in range(1, 6):
        procesar_miembro(miembro)

# Ejecutar el programa
if __name__ == "__main__":
    control_peso_club()