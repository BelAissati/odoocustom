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
print(p1)

p2 = Persona()
p2.introduir_dades()
p2.saluda()

    