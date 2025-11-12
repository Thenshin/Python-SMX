entrada = input("Introduce números separados por espacios: ").strip()
if not entrada:
    print("No se han introducido números.")
    raise SystemExit(0)

tokens = entrada.split()
total = 0.0
contador = 0

for t in tokens:
    try:
        n = float(t.replace(",", "."))
    except ValueError:
        print(f"Ignorado: '{t}' no es un número válido.")
        continue
    total += n
    contador += 1

if contador == 0:
    print("No hay números válidos para sumar.")
else:
    if total.is_integer():
        print("Suma total:", int(total))