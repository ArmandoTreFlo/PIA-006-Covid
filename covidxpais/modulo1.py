import requests
from modulo2 import graficar_casos_activos, guardar_en_excel, guardar_en_txt, promedio

consultas = {}
url_continentes = "https://disease.sh/v3/covid-19/countries"
norame = []
surame = []
asia = []
europa = []
oceania = []
africa = []

def menu1():
    llenar_listas(url_continentes)#llena las listas de los paises :p
    while True:
        print("""
-------------------------------------------------------------
Seleccione un continente:
1. América Norte
2. América Sur
3. Asia
4. Europa
5. Australia-Oceanía
6. África
7. CONTINUAR____________             
8. {---SALIR DEL PROGRAMA---}
-------------------------------------------------------------
        """)
        opcion = input("Ingrese el número correspondiente al continente: ")

        try:
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                menu_continente(opcion)
            elif opcion == 7:
                return menu2()
            elif opcion == 8:
                salida()
            else:
                diferente()
        except ValueError:
            diferente()

def menu2():
    reiniciar = True

    while reiniciar:
        print("""
-------------------------------------------------------------
Seleccione una opción:
1. Escoger otro continente
2. Graficar
3. Guardar en un documento.txt
4. Guardar en un excel
5. Calculos matematicos(promedio)
6. {---SALIR DEL PROGRAMA---}
-------------------------------------------------------------
        """)
        opcion = input("Ingrese el número correspondiente a la opción: ")

        try:
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                if opcion == 1:
                    menu1()
                elif opcion == 2:
                    graficar_casos_activos(consultas)
                elif opcion == 3:
                    guardar_en_txt(consultas)
                elif opcion == 4:
                    guardar_en_excel(consultas)
                elif opcion == 5:
                    promedio(consultas)
                elif opcion == 6:
                    salida()

                respuesta = input("¿Desea regresar al menú principal? (s/n)(n cerrara el programa): ").lower()

                try:
                    if respuesta == 's':
                        reiniciar = True
                    elif respuesta == 'n':
                        reiniciar = False
                        salida()
                        exit()
                    else:
                        raise ValueError("Respuesta inválida. Debe ser 's' o 'n', se asume que quieres volver.")
                except ValueError as e:
                    print(f"Error: {e}")

            else:
                diferente()
        except ValueError:
            diferente()

def salida():
    while True:
        try:
            c = int(input("""
-------------------------------------------------------------
¿Está seguro que quiere salir del programa?
    (1) Sí, salir del programa
    (2) No, regresar al menú principal
-------------------------------------------------------------
    """))
            if c == 1:
                print("¡Adiós... :'(")
                print(consultas)
                print("----------------------------------------------------------")
                exit() 
            elif c == 2:
                return False
            else:
                diferente()
        except ValueError:
            diferente()

def diferente():
    print('Opción inválida, introduzca un valor correcto')

def llenar_listas(url_continentes):
    try:
        r = requests.get(url_continentes)
        data = r.json()

        for pais in data:
            nompais = pais["country"]
            region = pais["continent"]

            if region == "North America":
                norame.append(nompais)
            elif region == "South America":
                surame.append(nompais)
            elif region == "Asia":
                asia.append(nompais)
            elif region == "Europe":
                europa.append(nompais)
            elif region == "Australia-Oceania":
                oceania.append(nompais)
            elif region == "Africa":
                africa.append(nompais)

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a la API: {e}")

def obtener_datos_pais(pais, continente):
    try:
        url = f'https://disease.sh/v3/covid-19/countries/{pais}'
        response = requests.get(url)
        data = response.json()

        if 'active' in data:
            casos_activos = data['active']
            return {
                'Pais': pais,
                'Continente': continente,
                'Casos Activos': casos_activos
            }
        else:
            return {
                'error': 'La respuesta no contiene datos válidos'
            }

    except requests.exceptions.RequestException as e:
        return {
            'error': f'Error de solicitud: {e}'
        }
    except KeyError as e:
        return {
            'error': f'Error al obtener datos: {e}'
        }
    except Exception as e:
        return {
            'error': f'Error desconocido: {e}'
        }

def guardar_informacion(continente, datos_pais):
    if consultas.get(continente) is None:
        consultas[continente] = [datos_pais]
    else:
        if datos_pais not in consultas[continente]:
            consultas[continente].append(datos_pais)
        else:
            print("Datos ya ingresados previamente para este país!")

def mostrar_paises(paises):
    for i, pais in enumerate(paises, start=1):
        print(f"{i}. {pais}")

def menu_continente(opcion):
    continente = None
    paises = None

    if opcion == 1:
        continente = 'North America'
        paises = norame
    elif opcion == 2:
        continente = 'South America'
        paises = surame
    elif opcion == 3:
        continente = 'Asia'
        paises = asia
    elif opcion == 4:
        continente = 'Europe'
        paises = europa
    elif opcion == 5:
        continente = 'Australia-Oceania'
        paises = oceania
    elif opcion == 6:
        continente = 'Africa'
        paises = africa

    print(f"\nPaíses en {continente}:")
    mostrar_paises(paises)

    while True:
        seleccion_pais = input("Seleccione un país (o 0 para volver al menú principal): ")
        try:
            seleccion_pais = int(seleccion_pais)
            if 0 <= seleccion_pais <= len(paises):
                if seleccion_pais == 0:
                    break
                else:
                    nombre_pais = paises[seleccion_pais - 1]
                    datos_pais = obtener_datos_pais(nombre_pais, continente)
                    print("\nDatos del país seleccionado:")
                    for clave, valor in datos_pais.items():
                        print(f"{clave}: {valor}")

                    guardar = input("¿Quiere guardar la información? (s/n): ").lower()
                    if guardar == 's':
                        guardar_informacion(continente, datos_pais)
                    elif guardar == 'n':
                        print("Información descartada.")
                    else:
                        print("Entrada inválida. Se asumirá como 'n' (no guardar).")
            
            else:
                print("Selección inválida. Introduzca un número válido.")
        except ValueError:
            print("Selección inválida. Introduzca un número válido.")
