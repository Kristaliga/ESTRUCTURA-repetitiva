#Arellano Martinez Luis Fernando 250152
#Determinar cuanto dinero recibira cada obrero

def calcular_pago(horas_trabajadas, pago_por_hora):
    if horas_trabajadas <= 40:
        return horas_trabajadas * pago_por_hora
    else:
        horas_extras = horas_trabajadas - 40
        if horas_extras <= 8:
            pago_extras = horas_extras * pago_por_hora * 2
        else:
            primeras_8 = 8 * pago_por_hora * 2
            resto = (horas_extras - 8) * pago_por_hora * 3
            pago_extras = primeras_8 + resto
        return 40 * pago_por_hora + pago_extras

# Solicitar datos
n = int(input("Ingrese el número de obreros: "))
pago_hora_normal = float(input("Ingrese el pago por hora normal: "))

# Calcular pago para cada obrero
print("\nPagos semanales:")
for i in range(1, n+1):
    horas = float(input(f"Ingrese las horas trabajadas por el obrero {i}: "))
    pago = calcular_pago(horas, pago_hora_normal)
    print(f"Obrero {i}: ${pago:.2f}")