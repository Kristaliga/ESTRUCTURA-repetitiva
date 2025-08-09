#Arellano Martinez Luis Fernando 250152
#Calculo de Inversion con interes compuesto mensual (2% anual)

capital = float(input("ingrese la cantidad a invertir: "))
tasa_anual = 0.02 # 2% de interes anual 
meses = 12 # 1 año


#Calcular intereses mensaul y monto fijo final 
tasa_mensual = tasa_anual / 12
monto_final = capital * (1 + tasa_mensual) ** meses 

#Mostrar resultados 
print("\n--- resumen de inversion ---")
print(f"capital inicial: ${capital:,.2f}")
print(f"tasa de interes anual: {tasa_anual*100}%")
print (f"tasa de interes mensual:{tasa_mensual*100:.6f}%")
print (f"periodo: {meses} meses (1 año)")
print (f"monto final: ${monto_final:.2f}")
print(f"ganancia obtenida: ${monto_final - capital:,.2f}")