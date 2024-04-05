#https://blog.hubspot.es/website/while-python
import random

# DEFINIM LES OPCIONS DE JOC

opcions = ["pedra", "paper", "tisores"]

# INICIALITZEM LES VARIABLES

jugador_punts = 0
ordinador_punts = 0

# REPETIM FINS QUE ALGÚ ACONSEGUEIXI 3 PUNTS

while jugador_punts < 3 and ordinador_punts < 3:
    # L'ORDINADOR SELECCIONA UNA OPCIÓ ALEATÒRIA
    ordinador_opcio = random.choice(opcions)
    # EL JUGADOR SELECCIONA LA SEVA OPCIÓ
    jugador_opcio = input("Escull pedra, paper o tisores: ")

    # IMPRIMIM LES OPCIONS ESCOLLIDES
    print("Jugador:", jugador_opcio)
    print("Ordinador:", ordinador_opcio)

    # DETERMINEM EL GUANYADOR DE LA RONDA
    if jugador_opcio == ordinador_opcio:
        print("Empat!")
    elif (jugador_opcio == "pedra" and ordinador_opcio == "tisores") or \
         (jugador_opcio == "paper" and ordinador_opcio == "pedra") or \
         (jugador_opcio == "tisores" and ordinador_opcio == "paper"):
        print("Has guanyat!")
        jugador_punts += 1
    else:
        print("Has perdut!")
        ordinador_punts += 1

    # IMPRIMIM ELS PUNTS ACTUALS
    print("Jugador:", jugador_punts)
    print("Ordinador:", ordinador_punts)
    print()

# IMPRIMIM EL GUANYADOR DEL JOC
if jugador_punts > ordinador_punts:
    print("Has guanyat el joc!")
else:
    print("Has perdut el joc!")