print("Introduce nombres separados por comas: ")
entrada = input()
nombres = [s.strip() for s in entrada.split(',') if s.strip()]
if nombres:
    print("Lista en orden inverso:", ", ".join(nombres[::-1]))
else:
    print("No se han introducido nombres.")