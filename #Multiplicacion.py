#Arellano Martinez Luis Fernando 250152
#MULTIPLICACION

acumulador = 1
n = int(input("De que numero quieres saber su tabla de multiplicar: "))
# leer 5 numeros usando un bucle for
print(f"la tabla de multiplicar del {n} es:")
for j in range(n):  # numero de la tabla
    for i in range(10):  # multiplicaciones hasta el 10
        mul = (j+1)*(i+1)

        print(f"{n} x {i+1} = {mul}")