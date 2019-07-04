num = int(input('Introduzca un numero '))
multiplicador = 0
while num < 0:
    print ('El numero introducido no puede ser negativo.')
num = int(input('Introduzca otro numero '))
while multiplicador <= 10:
    resultado = num*multiplicador
print(num,'x', multiplicador, '=', resultado)

input ('Pulse ENTER para finalizar')
