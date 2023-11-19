import sys
from modulo1 import menu1

def usarcmd_sys():
    if len(sys.argv) > 1:
        opcion = sys.argv[1]
        if opcion == "-ayuda":
            print("LAS OPCIONES SON: -autores, -version")
            exit()
        elif opcion == "-autores":
            print("        GRUPO006                 PROGRAMACION BASICA")
            print("Armando Trejo Flores              2127293 LF")
            print("Angel Alejandro Torres Anguiano   2051323 LA")
            print("Jonathan David Padron Antonio     1684805 LM")
            exit()
        elif opcion == "-version":
            print("PIA PAISESCOVID19 v3.0")
            exit()
        else:
            print("Opción desconocida. Usa -ayuda para ver las opciones disponibles.")
            exit()

def main():
    usarcmd_sys()
    menu1()

if __name__ == "__main__":
    main()