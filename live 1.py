import random

letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def creaRotor(letras):
    lista1 = list(letras)
    lista2 = []
    contador = 0 
    for letra in letras:
        n = random.randrange(len(letras))
        while n in lista2:
            n = random.randrange(len(letras))
        lista1[contador] = letras[n]
        lista2.append(n)
        contador += 1
    return lista1

rotor1 = creaRotor("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")