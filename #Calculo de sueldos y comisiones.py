#Luis Fernando Arellano Martinez 250152
#Calculo de sueldos y comisiones 

# Solicitar datos al gerente
n_vendedores = int(input("Ingrese el número de vendedores: "))
sueldo_base = float(input("Ingrese el sueldo base por vendedor: "))
ventas_por_semana = 3  # Cada vendedor hace 3 ventas/semana

# Procesar cada vendedor
for i in range(1, n_vendedores + 1):
    print(f"\n--- Vendedor {i} ---")
    
    # Ingresar monto de cada venta
    total_ventas = 0
    for j in range(1, ventas_por_semana + 1):
        venta = float(input(f"Ingrese el monto de la venta {j}: "))
        total_ventas += venta
    
    # Calcular comisiones (10% del total de ventas)
    comisiones = total_ventas * 0.10
    
    # Calcular sueldo total (base + comisiones)
    sueldo_total = sueldo_base + comisiones
    
    # Mostrar resultados
    print(f"\nResumen para el vendedor {i}:")
    print(f"- Total ventas: ${total_ventas:.2f}")
    print(f"- Comisiones (10%): ${comisiones:.2f}")
    print(f"- Sueldo total: ${sueldo_total:.2f}")

print("\n--- Proceso completado ---")