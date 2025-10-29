
n = int(input("Tamaño de la matriz: "))

m = []
for i in range(n):
    fila = []
    for j in range(n):
        x = int(input(f"Elemento [{i},{j}]: "))
        fila.append(x)
    m.append(fila)

identidad = True
for i in range(n):
    for j in range(n):
        if i == j and m[i][j] != 1:
            identidad = False
        if i != j and m[i][j] != 0:
            identidad = False

if identidad:
    print("Es una matriz identidad")
else:
    print("No es una matriz identidad")
