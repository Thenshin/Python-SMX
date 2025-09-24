nota1=int(input("Ingrese la nota del estudiante: "))
nota2=int(input("Ingrese la nota del estudiante: "))
nota3=int(input("Ingrese la nota del estudiante: "))
notatotal= nota1*0.3 + nota2*0.2 + nota3*0.5
if nota1 < 4 and nota2 <4 and nota3 <4:
    print("TU nota final es un 0")
elif nota1 < 4 or nota2 <4 or nota3 <4:
    print("Tu nota final es un 2")
elif nota1 > 4 or nota2 > 4 or nota3 >4:
    print("Tu nota final es: ", notatotal)
else:
    print("Vuelve a introducir las notas")    

