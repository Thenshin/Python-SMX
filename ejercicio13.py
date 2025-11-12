import re

texto = input("Introduce un texto: ")
if not texto:
    print("No se ha introducido texto.")
    raise SystemExit(0)

matches = re.findall(r'\bpython\b', texto, flags=re.IGNORECASE)
count = len(matches)

if count == 0:
    print("La palabra 'Python' no aparece en el texto.")
elif count == 1:
    print("La palabra 'Python' aparece 1 vez.")
else:
    print(f"La palabra 'Python' aparece {count} veces.")