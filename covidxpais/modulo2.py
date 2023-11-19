from openpyxl import Workbook
import numpy as np
import matplotlib.pyplot as plt

def promedio(consultas):
    for continente, paises in consultas.items():
        casos_activos = [pais['Casos Activos'] for pais in paises]
        
        media = np.mean(casos_activos)
        mediana = np.median(casos_activos)
        maximo = np.max(casos_activos)
        minimo = np.min(casos_activos)

        print(f'\nEstadísticas para {continente}:')
        print(f'Promedio: {media}')
        print(f'Mediana: {mediana}')
        print(f'Maximo: {maximo}')
        print(f'Mínimo: {minimo}')

def guardar_en_txt(consultas):
    nombre_archivo = input("Ingrese un nombre para el archivo (sin extensión): ")
    nombre_archivo += ".txt"

    with open(nombre_archivo, 'w') as archivo:
        for continente, datos_paises in consultas.items():
            archivo.write(f"Continente: {continente}\n")
            for datos_pais in datos_paises:
                archivo.write(f"Pais: {datos_pais['Pais']}\n")
                archivo.write(f"Casos Activos: {datos_pais['Casos Activos']}\n")
                archivo.write("\n")
            archivo.write("\n")

    print(f"La información se ha guardado en {nombre_archivo}")

def guardar_en_excel(consultas):
    wb = Workbook()
    ws = wb.active

    for continente, datos_paises in consultas.items():
        ws.append([f"Continente: {continente}"])
        ws.append(["Pais", "Casos Activos"])
        for datos_pais in datos_paises:
            ws.append([datos_pais['Pais'], datos_pais['Casos Activos']])
        ws.append([])

    nombre_archivo = input("Ingrese un nombre para el archivo Excel (sin extensión): ")
    nombre_archivo += ".xlsx"
    wb.save(nombre_archivo)

    print(f"La información se ha guardado en {nombre_archivo}")

def graficar_casos_activos(consultas):
    for continente, datos_paises in consultas.items():
        nombres_paises = [datos['Pais'] for datos in datos_paises]
        casos_activos = [datos['Casos Activos'] for datos in datos_paises]

        plt.figure(figsize=(10, 6))
        plt.bar(nombres_paises, casos_activos, color='green')
        plt.xlabel('País')
        plt.ylabel('Casos Activos')
        plt.title(f'Casos Activos por País en {continente}')
        plt.xticks(rotation=45, ha='right')#inclina los titulos par que no se amontonen, en caso de ser muchos claro
        plt.tight_layout()

        plt.show()