from random import*
def generaNumeroAleatorio (minimo,maximo):
    if minimo > maximo:
        aux = maximo
        minimo = maximo
        maximo = aux
        return ranint (minimo,maximo)
        if minimo < maximo:
            return randint (minimo,maximo)
