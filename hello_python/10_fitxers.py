''' Treball amb fitxers '''

def menu():
    print ('1)Entrar dades')
    print ('2)Llegir dades')
    print ('0) Sortir del programa')
    op=int(input("Tria opció: "))
    return op

opcio=menu()
while (opcio!=0):
    if (opcio==1):
        fo = open("fitxer.txt", "a+")
        print( "Nom del Fitxer", fo.name)
        noves_dades=input("Introdueix una frase: ")
        fo.write(noves_dades+'\n')
        fo.close()
    elif (opcio==2):
        print("Dades Fitxer:")
        fo = open("fitxer.txt", "r")
        print(fo.read())
        fo.close()
    else:
        print("T'has equivocat d'opció")    
    opcio=menu()

print ("Fins la pròxima!")