# Feu un programa en Python que demani 2 nombres sencers i que calculi la divisió, indicant si és exacta o no.

num1=float(input("Introdueix el primer operador: "))
num2=float(input("Introdueix el segon operador: "))

divisio= num1/num2

print("La divisio es " , divisio)

if num1 % num2 ==0:
    print("Es exacta")
else: print("No es exacta")