def es_any_de_traspas(any):
    if any % 400 == 0:
        return True
    if any % 100 == 0:
        return False
    if any % 4 == 0:
        return True
    return False

anysprovar = [1900, 2000, 2016, 1987]
resultats = {any: es_any_de_traspas(any) for any in anysprovar}
print(resultats)
