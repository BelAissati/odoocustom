class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any
    
    def informacio(self):
        print(f"El llibre {self.titol} el va escriure {self.autor} l'any {self.any}")

# Exemple d'ús
llib = Llibre("Ubuntu", "Shuttleworth", 2014)
llib.informacio()  # Això mostrarà "El llibre Ubuntu el va escriure Shuttleworth l'any 2014"
