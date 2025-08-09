#Arellano Martinez Luis Fernando 250152
# Programa para calcular el total a pagar en la tienda Enano, S.A. con descuento del 20% en artículos de etiqueta roja

total = 0.0
while True:
    # Solicitar precio del artículo
    precio = float(input("Ingrese el precio del artículo (o 0 para terminar): "))
    
    # Verificar si el usuario desea terminar
    if precio == 0:
        break
    
    # Solicitar si el artículo tiene etiqueta roja
    etiqueta = input("¿El artículo tiene etiqueta roja? (s/n): ").lower()
    
    # Calcular precio con descuento si aplica
    if etiqueta == 's':
        precio_con_descuento = precio * 0.8  # Aplica 20% de descuento
    else:
        precio_con_descuento = precio
    
    # Sumar al total
    total += precio_con_descuento

# Mostrar el total a pagar
print(f"El total a pagar es: ${total:.2f}")