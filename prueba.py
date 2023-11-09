import numpy as np
from scipy.optimize import curve_fit

# Define la función que deseas ajustar a tus datos
def funcion_a_ajustar(x, a, b, c):
    print(x)
    return a * x**2 + b * x + c

# Genera algunos datos de ejemplo
x_datos = np.array([1, 2, 3, 4, 5])
y_datos = np.array([1.2, 2.5, 3.8, 5.2, 6.7])

# Realiza el ajuste de la función a los datos
parametros_optimos, matriz_de_covarianza = curve_fit(funcion_a_ajustar, x_datos, y_datos)

# Los parámetros óptimos se encuentran en el array 'parametros_optimos'
a_optimo, b_optimo, c_optimo = parametros_optimos

print("Parámetros óptimos:")
print("a:", a_optimo)
print("b:", b_optimo)
print("c:", c_optimo)
