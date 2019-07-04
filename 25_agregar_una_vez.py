elementos = [1, 5, -2]

def agregar_una_vez(lista,i):
    try:
        if i in lista:
            raise ValueError
        else:
            lista.append(i)
    except ValueError:
        print("Error: No se pueden agregar elementos repetidos", i)

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")

print(elementos)

print ('Error: No se pueden agregar elementos repetidos')
[1, 5, -2, 10, 'Hola']

