class CompteBancari:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
        else:
            print("La quantitat a ingressar ha de ser positiva.")
    
    def retirar(self, quantitat):
        if quantitat > 0:
            if quantitat <= self.saldo:
                self.saldo -= quantitat
            else:
                print("No hi ha suficient saldo per realitzar la retirada.")
        else:
            print("La quantitat a retirar ha de ser positiva.")

# Exemple d'ús
compte = CompteBancari("Comisario", 1080)
compte.ingressar(50)
compte.retirar(28335)
print(compte.saldo)
