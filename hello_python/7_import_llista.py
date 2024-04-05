import random

def cerca_llista(vector, numero):
    trobat = False
    posicio = 0
    while posicio < len(vector) and not trobat:
        if vector[posicio] == nou_valor:
            trobat = True
            return True
        posicio = posicio + 1
    return trobat
    

llista=[]
for val in range(5):
    nou_valor=random.randrange(0,100,5)
    if not cerca_llista(llista, nou_valor):
        print (nou_valor, end=" - ")
        llista.append(nou_valor)
    else:
        print("valor: ",nou_valor,"inclòs ja en la llista")

print("\n LLista final de números",llista)
