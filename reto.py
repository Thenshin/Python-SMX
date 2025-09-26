dinero_total = 1000
eleccion = ""

while eleccion != "salir":
    print("tu saldo actual es", dinero_total, "€")
eleccion=int(input("escribe la palabra 'retirar' o 'salir' para terminar: "))     
while eleccion == 'retirar':
   monto=print("¿Cuanto quieres retirar: ")
if monto <=0:
    print("Error, no puedes retirar esta cantidad")
if monto > dinero_total:
    print("Error, no puedes retirar este dinero")
if monto %10 !=0:
    print("Error, no es multiplo de 10")
if dinero_total>=monto:
    print("retiro realizado con exito")
    dinero_total-=monto
    print("nuevo saldo", dinero_total, "€")
elif eleccion == 'salir':
    print("Gracias por usar este cajero")
else:
    print("Opcion no valida, pruebe de nuevo")        

