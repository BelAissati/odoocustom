import os

def comptar_elements(arxiu, opcio):
    try:
        with open(arxiu, 'r', encoding='utf-8') as file:
            contingut = file.readlines()
    except FileNotFoundError:
        return "Error: L'arxiu no s'ha trobat."
    
    if opcio == 1:
        return len(contingut)
    elif opcio == 2:
        return sum(len(linia.split()) for linia in contingut)
    elif opcio == 3:
        return sum(len(linia) for linia in contingut)
    else:
        return None

def main():
    directori_actual = os.path.dirname(os.path.realpath(__file__))
    opcions = {'1': "línies", '2': "paraules", '3': "caràcters"}

    while True:
        print("\nMenú:")
        print("1. Comptar línies")
        print("2. Comptar paraules")
        print("3. Comptar caràcters")
        print("0. Sortir")
        
        opcio = input("Tria una opció: ")

        if opcio == '0':
            break
        elif opcio in opcions:
            arxiu = os.path.join(directori_actual, "a.txt")  # Pot ser 'a.txt' o 'b.txt'
            resultat = comptar_elements(arxiu, int(opcio))
            if isinstance(resultat, int):
                print(f"El nombre de {opcions[opcio]} comptats és: {resultat}")
            else:
                print(resultat)
        else:
            print("Opció no vàlida. Siusplau, introdueix un número vàlid.")

if __name__ == "__main__":
    main()
