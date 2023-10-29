import csv
import os

def split_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        file_number = 1
        current_file = open(f'medicion{file_number}.csv', 'w')
        writer = csv.writer(current_file)
        for row in reader:
            if row and row[0].startswith('#'):
                if os.fstat(current_file.fileno()).st_size > 0:  # Si el archivo actual no está vacío, entonces crea uno nuevo
                    current_file.close()
                    file_number += 1
                    current_file = open(f'medicion{file_number}.csv', 'w')
                    writer = csv.writer(current_file)
            else:
                writer.writerow(row)
        current_file.close()

# Uso de la función
split_csv('dataset.csv')

