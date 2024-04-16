#Escriviu un programa en Python per fer una llista de grups de música dels països catalans.
#pas1
musicat = []
print(musicat)

# pas 2
musicat.insert(0,"La Fumiga")
musicat.insert(1,"The Tyets")
musicat.insert(2,"Ginestà")
print(musicat)

#pas3
for i in range (2):
    nou_grup=str(input("Nou grup: "))
    musicat.append(nou_grup)
print(musicat)

#pas4
musicat.pop(3)
musicat.pop(3)
print(musicat)

#pas 5
musicat.insert(0,"iaia")
print(musicat)


    
    

