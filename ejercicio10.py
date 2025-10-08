# Programa que pide precios hasta que se escriba 0 y muestra el total con 2 decimales
total = 0.0
while True:
	precio = float(input("Introduce el precio (0 para terminar): "))
	if precio == 0:
		break
	total += precio
print(f"El total de la factura es: {total:.2f}")
