#Arellano Martinez Luis Fernando 250152
#Cajero de Supermercado

def obtener_respuesta_si_no(mensaje):
    """Valida que la entrada sea 's' o 'n'."""
    while True:
        respuesta = input(mensaje).lower().strip()
        if respuesta in ['s', 'n']:
            return respuesta
        print("Por favor, ingrese 's' para sí o 'n' para no.")

def obtener_precio_articulo():
    """Obtiene y valida el precio de un artículo."""
    while True:
        entrada = input("Ingrese el precio del artículo (o 'fin' para terminar): ").lower().strip()
        if entrada == 'fin':
            return None
        try:
            precio = float(entrada)
            if precio < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
                continue
            return precio
        except ValueError:
            print("Por favor, ingrese un precio numérico válido o 'fin'.")

def procesar_cliente():
    """Procesa los artículos de un cliente y devuelve el total."""
    total_cliente = 0.0
    print("\n--- Nuevo cliente ---")
    while True:
        precio = obtener_precio_articulo()
        if precio is None:  # El usuario ingresó 'fin'
            break
        total_cliente += precio
    print(f"Total a pagar por el cliente: ${total_cliente:.2f}")
    return total_cliente

def cajero_supermercado():
    """Sistema principal del cajero de supermercado."""
    total_dia = 0.0
    print("Sistema de caja de supermercado")
    
    while True:
        if obtener_respuesta_si_no("¿Registrar nuevo cliente? (s/n): ") == 'n':
            break
        total_dia += procesar_cliente()
    
    print(f"\nTotal cobrado en el día: ${total_dia:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    cajero_supermercado()