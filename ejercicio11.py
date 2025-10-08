# Programa que pide N números positivos y muestra el mayor y el menor
n = int(input("Cuantos números vas a introducir?: "))
if n <= 0:
    print("Debes introducir al menos un número.")
else:
    numero = float(input("Introduce un numero positivo: "))
    mayor = numero
    menor = numero
    for i in range(n - 1):
        numero = float(input("Introduce un número positivo: "))
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
