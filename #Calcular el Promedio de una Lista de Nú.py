#Arellano Martinez Luis Fernando 250152
#Control de Producción Diaria de Copias
# Inicializar contadores diarios

copias_offset = 0
copias_estandar = 0

while True:
    # Solicitar datos
    tipo = input("Ingrese el tipo de impresión (offset/estandar): ").lower()
    if tipo not in ["offset", "estandar"]:
        print("¡Tipo inválido!")
        continue
    
    try:
        copias = int(input("Número de copias solicitadas: "))
    except ValueError:
        print("¡Ingrese un número válido!")
        continue
    
    # Verificar límites
    if tipo == "offset":
        limite = 10000
        pendientes = copias_offset
    else:
        limite = 50000
        pendientes = copias_estandar
    
    if (pendientes + copias) <= limite:
        if tipo == "offset":
            copias_offset += copias
        else:
            copias_estandar += copias
        print(f"✅ Aceptado. Copias {tipo} pendientes: {pendientes + copias}")
    else:
        print(f"❌ Rechazado. Límite {limite} excedido.")
    
    # ¿Otra orden?
    if input("¿Ingresar otra orden? (si/no): ").lower() != "si":
        break

# Resumen
print("\n--- Resumen Diario ---")
print(f"Copias offset: {copias_offset}")
print(f"Copias estándar: {copias_estandar}")