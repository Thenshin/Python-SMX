print("Nombrame un par de numero para poder crear una factura hasta que llegues a 0: ")
num=int(input())
total=0

if num > 0:
    total=total + num
    print("dime otro numero")
    num=int(input())
else:
    num<0
    print("este numero no es valido")