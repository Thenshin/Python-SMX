nota=int(input("Ingrese la nota del estudiante: "))
if nota >=0 or nota <5:
    print("Insuficiente")
    if nota >=5 or nota <6:
        print("Suficiente")
    if nota >=6 or nota <7:
        print("Bien")
    if nota >=7 or nota <9:
        print("Notable")
    if nota >=9 or nota <=10:
        print("Sobresaliente")    