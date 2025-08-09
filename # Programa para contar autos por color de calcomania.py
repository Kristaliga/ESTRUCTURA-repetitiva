#Arellano Martinez Luis Fernando 250152
# Programa para contar autos por color de calcomanía según el último dígito de la placa

# Solicitar la cantidad de autos
n = int(input("Ingrese la cantidad de autos: "))

# Inicializar contadores para cada color
amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0

# Procesar cada auto
for i in range(n):
    # Solicitar el último dígito de la placa
    digito = int(input(f"Ingrese el último dígito de la placa del auto {i+1}: "))
    
    # Clasificar según el dígito
    if digito == 1 or digito == 2:
        amarilla += 1
    elif digito == 3 or digito == 4:
        rosa += 1
    elif digito == 5 or digito == 6:
        roja += 1
    elif digito == 7 or digito == 8:
        verde += 1
    elif digito == 9 or digito == 0:
        azul += 1

# Mostrar resultados
print(f"Autos con calcomanía amarilla: {amarilla}")
print(f"Autos con calcomanía rosa: {rosa}")
print(f"Autos con calcomanía roja: {roja}")
print(f"Autos con calcomanía verde: {verde}")
print(f"Autos con calcomanía azul: {azul}")