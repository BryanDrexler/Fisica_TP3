import csv
import os
import pandas as pd

import csv

def read_measures():
    datos = []
    for i in range(1, 14):
        # Construimos el nombre del archivo
        archivo = f"mediciones/medicion{i}.csv"
        datos_archivo = []

        with open(archivo, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Omitir la primera fila

            for row in csvreader:
                datos_archivo.append(row)

        datos.append(datos_archivo)

    return datos

datos = read_measures()

print(datos)

