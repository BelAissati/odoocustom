import getpass
import re

def validar_usuari(nom_usuari):
    return re.match("^[a-z0-9]+$", nom_usuari)

def afegir_usuari(nom_usuari, contrasenya):
    with open("dades.txt", "a") as file:
        file.write(f"{nom_usuari}:{contrasenya}\n")

def mostrar_usuaris():
    print("Usuaris registrats:")
    with open("dades.txt", "r") as file:
        for line in file:
            print(line.split(':')[0])

def main():
    nom_usuari = input("Introdueix el teu nom d'usuari: ")
    if validar_usuari(nom_usuari):
        contrasenya = getpass.getpass("Introdueix la teva contrasenya: ")
        afegir_usuari(nom_usuari, contrasenya)
        mostrar_usuaris()
    else:
        print("Error: El nom d'usuari només pot contenir caràcters alfanumèrics i no pot incloure espais.")

if __name__ == "__main__":
    main()
