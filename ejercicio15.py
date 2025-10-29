numeros = []

while True:
    num = int(input("Escribe un número (0 para terminar): "))
    if num == 0:
        break
    numeros.append(num)

print("\nLista de números introducidos:", numeros)

buscar = int(input("\n¿Qué número quieres buscar?: "))

posiciones = []
for i in range(len(numeros)):
    if numeros[i] == buscar:
        posiciones.append(i)

if posiciones:
    print(f"El número {buscar} aparece en las posiciones: {posiciones}")
else:
    print(f"El número {buscar} no aparece en la lista.")