import csv

def split_measurements(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        description = []
        current_measurement = []
        for row in reader:
            if row and row[0].startswith('#'): 
                measurement = []
                description.append(row)  # Comienza una nueva medición con la línea actual
            else: measurement.append()
        return current_measurement
"""         if current_measurement:  # Agrega la última medición si no está vacía
            measurements.append(current_measurement) """
   

# Uso de la función
measurements = split_measurements('dataset.csv')
print(measurements)
