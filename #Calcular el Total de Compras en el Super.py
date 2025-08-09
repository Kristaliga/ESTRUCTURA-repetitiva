#Arellano Martinez Luis Fernando 250152
#Calcular el Total de Compras en el Supermercado

total = 0.0

while True:
    try:
        precio = float(input("Ingrese el precio del artículo: $"))
        cantidad = int(input("Ingrese la cantidad: "))
        
        if precio <= 0 or cantidad <= 0:
            print("¡Error! Ingrese valores positivos.")
            continue
        
        subtotal = precio * cantidad
        total += subtotal
        
        print(f"Gasto en este artículo: ${subtotal:.2f}")
        print(f"Total acumulado: ${total:.2f}")
        
        continuar = input("¿Agregar otro artículo? (si/no): ").lower()
        if continuar != "si":
            break
    except ValueError:
        print("¡Error! Ingrese números válidos.")

print("\n--- TOTAL A PAGAR ---")
print(f"Monto final: ${total:.2f}")