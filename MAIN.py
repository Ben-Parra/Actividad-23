from funciones import *


while True:
    try:
        limpiar()
        print("Cosas varias")
        print("1.- Calcular el IVA de un producto")
        print("2.- Calcular el descuento de un producto")
        print("3.- Calcular su IMC")
        print("0.- Salir")
        opcion=int(input("Ingrese su opcion : "))
        match opcion:
            case 0:
                break
            case 1:
                print("Calcular IVA")
                precio=int(input("Ingrese el valor del producto del cual quire saber su IVA : "))
                if precio>0:
                 calculariva(precio)
                else:
                 print("Precio ingresado no valido")
            case 2:
                print("Calcular el descuento")
                precio=int(input("Ingrese un precio a su eleccion : "))
                if precio>0:
                 desc=int(input("Ingrese el descuento que desea hacerle : "))
                 if desc>0:
                    descuento(precio,desc)
                 else:
                    print("Descuento ingresado no valido")
                else:
                   print("Precio ingresado no valido")
            case 3:
                print("Calcular IMC")
                altura=float(input("Ingrese su altura en metros : "))
                if altura>0:
                   peso=float(input("Ingrese su peso en kilogramos : "))
                   if peso>0:
                      calcularIMC(altura,peso)
                   else:
                      print("Peso ingresado no valido")
                else:
                   print("Altura ingresada no valida")
            case _:
                print("Opcion no valida")
    except:
        print("error")