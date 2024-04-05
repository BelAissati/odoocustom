class Persona:
    def __init__(self, nom="XX", edat=0):
        self.nom = nom
        self.edat = edat

    def __str__(self):
        return f"{self.nom} ({self.edat})"
    
    def saluda(self):
        print("Hola, em dic " + self.nom + " i tinc " + str(self.edat) + " anys.")

    def introduir_dades(self):
        self.nom = input("Introdueix el nom: ")
        self.edat=int(input("Introdueix l'edat: "))

p1 = Persona("Anna", 25)
#p1.saluda()

p2 = Persona("Antonia", 63)
#p2.saluda()

persones=[p1,p2]

for persona in persones:
    persona.saluda()

p3 = Persona("Amanda", 47)

persones.append(p3)
print(p3)

for persona in persones:
    persona.saluda()

persones.pop()
persones.remove(persones[0])

print(persones)
for persona in persones:
    print(persona)