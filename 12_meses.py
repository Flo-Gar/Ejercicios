meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre", "Octubre","Noviembre","Diciembre"]
salir = False
while not salir:
    numero = int (input ("Dame un numero : "))
    if numero == 0 :
        salir = True
    else:
        if (numero>=1 and numero<=len(meses)):
            print (meses[numero−1])
            else:
                print ( "Dar un numero entre el 1 y ", len(meses))
input ('Pulse ENTER para finalizar')
