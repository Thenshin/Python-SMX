
def mcd(a: int, b: int) -> int:
    """Devuelve el máximo común divisor de a y b (algoritmo de Euclides)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def esPrimo(n: int) -> bool:
    """Devuelve True si n es primo, False en caso contrario."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    print(f"MCD de 20 y 12: {mcd(20, 12)}")  

    primos = [n for n in range(1, 51) if esPrimo(n)]
    print("Primos entre 1 y 50:", primos)

