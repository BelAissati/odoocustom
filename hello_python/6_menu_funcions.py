def menu():
    print ('1)Suma números')
    print ('2)Resta números')
    print ('3)Multiplica números')
    print ('0) Sortir del programa')
    op=int(input("Tria opció: "))
    return op
    
    
def suma(x,y):
    result=x+y
    return result

def resta(x,y):
    result=x-y
    return result

def multiplica(x,y):
    result=x*y
    return result
    
a=int(input("Introdueix el número a: "))
b=int(input("Introdueix el número b: "))
opcio=menu()
while (opcio!=0):
    if (opcio==1):
        print(suma(a,b))
    elif (opcio==2):
        print(resta(a,b))
    elif (opcio==3):
        print(multiplica(a,b))
    else:
        print("T'has equivocat d'opció")    
    opcio=menu()

print ("Fins la pròxima!")
