numero_secreto = 9
intento=int(input("Adivina el numero entre 1 y 10: "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("el numero no es correcto, es mayor")
    else:
        print("el numero no es correcto, es menor")

    intento = int(input("Intenta de nuevo: "))
print("Felicidades, adivinaste el numero")

