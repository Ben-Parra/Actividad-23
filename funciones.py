from os import system
from msvcrt import getch

def limpiar():
    print("Presione una tecla para continuar")
    getch()
    system("cls")


def calculariva (precio):
    iva=round(precio*0.19)
    print(f"El IVA de ${precio} es de ${iva}")

def descuento(precio,desc):
    valor=precio-(round(precio*(desc/100)))
    print(f"El precio del producto, que era de ${precio}, aplicandole un descuento del {desc}%, queda en un total de ${valor}")

def calcularIMC(altura,peso):
    IMC=round(peso/(altura**2),1)
    print(f"Su IMC es de {IMC}")
    if IMC<18.5:
        print("Usted esta bajo peso")
    elif IMC>=18.5 and IMC<=24.9:
        print("Usted esta en un peso adecuado")
    elif IMC>=25 and IMC<=29.9:
        print("Usted esta con sobre peso")
    elif IMC>=30 and IMC<=34.9:
        print("Usted esta con obesidad grado 1 ")
    elif IMC>35 and IMC<=39.9:
        print("Usted esta con obesidad grado 2 ")
    else:
        print("Usted esta con obesidad grado 3 ")
