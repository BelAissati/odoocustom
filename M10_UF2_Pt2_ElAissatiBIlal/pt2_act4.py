import getpass
import re
import os

# Establece el directorio de trabajo en el directorio del script (aqui he tingut que buscar ajuda perque tenia problemes amb la ruta del arxiu)
directori_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(directori_script)

def validar_usuari(nom_usuari):
    return re.match("^[a-z0-9]+$", nom_usuari)

def afegir_usuari(nom_usuari, contrasenya):
    with open("dades.txt", "a") as file:
        file.write(f"{nom_usuari}:{contrasenya}\n")

def mostrar_usuaris():
    print("Usuaris registrats:")
    try:
        with open("dades.txt", "r") as file:
            for line in file:
                print(line.split(':')[0])
    except FileNotFoundError:
        print("No s'ha trobat el fitxer 'dades.txt'.")

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
