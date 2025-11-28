import random
import time
import os
import ast

RANKING_FILE = os.path.abspath(__file__)

# Marcadores que delimitan el bloque donde se almacenará el ranking
RANKING_START = ""

# --- RANKING START ---
{'Prueba': {'eco_loco': [7]}, 'jose': {'piedra_papel_tijera': [0]}}
# --- RANKING END ---

RANKING_END=""


def load_ranking():
    """Leer el ranking desde el propio archivo `miniarcade.py`.

    Busca el bloque entre `RANKING_START` y `RANKING_END` y evalúa
    su contenido con `ast.literal_eval` para obtener la estructura.
    """
    try:
        with open(RANKING_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return {}

    start = text.find(RANKING_START)
    end = text.find(RANKING_END)
    if start == -1 or end == -1 or end < start:
        return {}

    # extraer el contenido entre los marcadores
    block = text[start + len(RANKING_START):end].strip()
    if not block:
        return {}

    try:
        # Esperamos que block sea la representación literal de un dict
        ranking = ast.literal_eval(block)
        # normalizar formatos antiguos si es necesario
        for name, val in list(ranking.items()):
            if isinstance(val, int):
                ranking[name] = {"partidas": [val]}
            elif isinstance(val, dict):
                for g, scores in list(val.items()):
                    if isinstance(scores, int):
                        val[g] = [scores]
        return ranking
    except Exception:
        return {}

def save_ranking(ranking):
    """Guardar el dict `ranking` dentro de este mismo archivo entre los marcadores.

    Si el bloque ya existe lo reemplaza, si no lo añade al final del archivo.
    """
    try:
        with open(RANKING_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return

    block_text = "\n" + RANKING_START + "\n" + repr(ranking) + "\n" + RANKING_END + "\n"

    start = text.find(RANKING_START)
    end = text.find(RANKING_END)
    if start != -1 and end != -1 and end > start:
        # reemplazar el bloque existente
        new_text = text[:start] + block_text + text[end + len(RANKING_END):]
    else:
        # añadir el bloque al final
        new_text = text + "\n" + block_text

    try:
        with open(RANKING_FILE, 'w', encoding='utf-8') as f:
            f.write(new_text)
    except Exception:
        pass

def add_player_play(name):
    # mantener compatibilidad: incremento simple (no game info)
    ranking = load_ranking()
    if name not in ranking:
        ranking[name] = {}
    ranking[name].setdefault('partidas', []).append(1)
    save_ranking(ranking)
    return len(ranking[name].get('partidas', []))

def add_player_score(name, game, score):
    ranking = load_ranking()
    if name not in ranking or not isinstance(ranking[name], dict):
        ranking[name] = {}
    ranking[name].setdefault(game, []).append(score)
    save_ranking(ranking)
    return len(ranking[name][game])

def show_ranking():
    ranking = load_ranking()
    if not ranking:
        print("\nNo hay jugadores registrados aún. Juega para añadir entradas al ranking.\n")
        return
    # Calcular total de partidas por jugador (suma de listas)
    players_stats = []
    for name, games in ranking.items():
        if not isinstance(games, dict):
            players_stats.append((name, 0, {}))
            continue
        total = sum(len(scores) for scores in games.values() if isinstance(scores, list))
        players_stats.append((name, total, games))

    players_stats.sort(key=lambda x: x[1], reverse=True)
    print("\n--- Ranking de jugadores (por número total de partidas) ---")
    for i, (name, total, games) in enumerate(players_stats, 1):
        print(f"{i}. {name} - {total} partidas")
        # Mostrar detalle por juego
        for g, scores in games.items():
            if not isinstance(scores, list):
                continue
            plays = len(scores)
            best = max(scores) if scores else 0
            avg = round(sum(scores) / plays, 2) if plays else 0
            print(f"    - {g}: {plays} partidas, mejor={best}, media={avg}")
    print()

def mostrar_titulo():
    print("=" * 40)
    print("MINI-ARCADE DE PYTHON")
    print("=" * 40)
    print()

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("\n--- Piedra, Papel o Tijera ---")
    # jugar varias rondas en una sesión; la puntuación es número de victorias
    victorias = 0
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
            victorias += 1
        else:
            print("Perdiste")
        jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != 's':
            break
    print()
    return victorias

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
    # puntuación: si adivinó, puntuación = intentos restantes + 1, si no, 0
    return (intentos + 1) if guess == secreto else 0

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
    return aciertos

def eco_loco():
    print("\n--- Eco Loco ---")
    texto = input("Escribe algo: ")
    invertido = texto[::-1]
    vocales = sum(1 for c in texto.lower() if c in "aeiouáéíóú")
    print(f"Invertido: {invertido}")
    print(f"Nº de caracteres: {len(texto)}")
    print(f"Nº de vocales: {vocales}\n")
    # puntuación: número de vocales
    return vocales

def main():
    while True:
        mostrar_titulo()
        print("1. Piedra, Papel o Tijera")
        print("2. Adivina el Número")
        print("3. Cálculo Mental")
        print("4. Eco Loco")
        print("5. Mostrar ranking de jugadores")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion in ("1", "2", "3", "4"):
            nombre = input("Nombre del jugador (dejar vacío para no registrar): ").strip()
            score = None
            game_key = None
            if opcion == "1":
                score = piedra_papel_tijera()
                game_key = 'piedra_papel_tijera'
            elif opcion == "2":
                score = adivina_numero()
                game_key = 'adivina_numero'
            elif opcion == "3":
                score = calculo_mental()
                game_key = 'calculo_mental'
            elif opcion == "4":
                score = eco_loco()
                game_key = 'eco_loco'
            if nombre and game_key is not None:
                add_player_score(nombre, game_key, score)
                print(f"Registro: {nombre} -> {game_key} = {score} (guardado en ranking).\n")
            continue
        elif opcion == "5":
            show_ranking()
            continue
        elif opcion == "0":
            print("¡Gracias por jugar en el Mini-Arcade! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
            time.sleep(1.5)

if __name__ == "__main__":
    main()