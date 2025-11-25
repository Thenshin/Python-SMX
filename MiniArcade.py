import random
import time

def mostrar_titulo():
    print("=" * 40)
    print("MINI-ARCADE DE PYTHON")
    print("=" * 40)
    print()

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("\n--- Piedra, Papel o Tijera ---")
    while True:
        jugador = input("Elige (piedra, papel, tijera): ").lower()
        if jugador not in opciones:
            print("Opción no válida. Intenta otra vez.")
            continue
        bot = random.choice(opciones)
        print(f"El bot eligió: {bot}")
        if jugador == bot:
            print("¡Empate!")
        elif (jugador == "piedra" and bot == "tijera") or \
             (jugador == "papel" and bot == "piedra") or \
             (jugador == "tijera" and bot == "papel"):
            print("¡Ganaste! Enhorbuena.")
        else:
            print("Perdiste")
        jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != 's':
            break  
    print()

def adivina_numero():
    print("\n--- Adivina el Número ---")
    dificultad = {"1": 20, "2": 50, "3": 100}
    while True:
        print("Elige dificultad:")
        print("1. Fácil (1-20)")
        print("2. Normal (1-50)")
        print("3. Complicado (1-100)")
        dif = input("Opción: ")
        if dif in dificultad:
            max_num = dificultad[dif]
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
    secreto = random.randint(1, max_num)
    intentos = 5
    inicio = time.time()
    print(f"Adivina el número entre 1 y {max_num}. ¡Tienes {intentos} intentos!")
    while intentos > 0:
        try:
            guess = int(input("Tu intento: "))
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")
            continue
        if guess == secreto:
            duracion = round(time.time() - inicio, 2)
            print(f"¡Correcto! Lo adivinaste en {duracion} segundos.")
            break
        elif guess < secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        intentos -= 1
        print(f"Intentos restantes: {intentos}")
    else:
        print(f"Te quedaste sin intentos. El número era {secreto}.")
    print()

def calculo_mental():
    print("\n--- Cálculo Mental ---")
    tiempo_limite = 15
    inicio = time.time()
    aciertos = 0
    while time.time() - inicio < tiempo_limite:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        resultado = eval(f"{a}{op}{b}")
        try:
            resp = int(input(f"{a} {op} {b} = "))
        except ValueError:
            print("Entrada inválida.")
            continue
        if resp == resultado:
            aciertos += 1
            print("Correcto!\n")
        else:
            print(f"Incorrecto. Era {resultado}\n")
    print(f"¡Tiempo terminado! Aciertos totales: {aciertos}\n")

def eco_loco():
    print("\n--- Eco Loco ---")
    texto = input("Escribe algo: ")
    invertido = texto[::-1]
    vocales = sum(1 for c in texto.lower() if c in "aeiouáéíóú")
    print(f"Invertido: {invertido}")
    print(f"Nº de caracteres: {len(texto)}")
    print(f"Nº de vocales: {vocales}\n")

def main():
    while True:
        mostrar_titulo()
        print("1. Piedra, Papel o Tijera")
        print("2. Adivina el Número")
        print("3. Cálculo Mental")
        print("4. Eco Loco")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            piedra_papel_tijera()
        elif opcion == "2":
            adivina_numero()
        elif opcion == "3":
            calculo_mental()
        elif opcion == "4":
            eco_loco()
        elif opcion == "0":
            print("¡Gracias por jugar en el Mini-Arcade! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
