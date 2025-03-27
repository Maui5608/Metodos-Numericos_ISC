# -*- coding: utf-8 -*-
"""Tarea 1.1_Calculo de errorres_Métodos Numéricos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_5C48oYoKldLjkbSx8XiQZR7GgatnaaJ

**Ejercicio 1**
"""

#   Codigo que implementa un esquema numerico
#   para determinar la precision de una maquina

#   David Ezequiel Caballero González

import numpy as np

iteraciones = []
precisiones = []

epsilon = 1.0
iteracion = 0
while 1.0 + epsilon != 1.0:
     epsilon /= 2
     iteracion = iteracion + 1
     iteraciones.append(iteracion)
     precisiones.append(epsilon)
     print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")

plt.plot(iteraciones, precisiones, marker='d')
plt.xlabel('Iteración')
plt.ylabel('Precisión de máquina')
plt.title('Precisión de máquina vs. Iteración')
plt.grid(True)
plt.show()

"""**Ejercicio 2**"""

from logging import error
#   Codigo que implementa un esquema numerico
#   para determinar la aproximacion de Leibniz

#   David Ezequiel Caballero González

import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = np.pi
N_values = [10, 100, 1000, 10000]
errors_abs = []
errors_rel = []
errors_cuad = []

for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    error_cuad = error_abs**2
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cuad.append(error_cuad)
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}, Error cuadrático={error_cuad}")

plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.plot(N_values, errors_cuad, label='Error cuadrático', marker='p')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de pi')
plt.show()

"""**Ejercicio 3**"""

#   Codigo que implementa el calculo de errores
#   en operaciones numericas

#   David Ezequiel Caballero González

import matplotlib.pyplot as plt
import numpy as np

def calcular_errores(x, y, valor_real):
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    error_cuad = error_abs**2
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    print(f"Error cuadrático: {error_abs}")
    return error_abs, error_rel

valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)]

errores_abs = []
errores_rel = []
errores_pct = []
errores_cuad = []

for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    # The following line was incorrectly indented, causing the IndentationError.
    # It has been corrected to align with the for loop block.
    error_abs, error_rel = calcular_errores(x, y, real)
    errores_abs.append(error_abs)
    errores_rel.append(error_rel)
    errores_pct.append(error_abs / abs(real) *100) #Calculating error_pct and error_cuad inline
    errores_cuad.append(error_abs**2)

# Crear la figura con subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Gráfica de barras para el error absoluto
axs[0, 0].bar([1, 2], errores_abs, label='Error absoluto')
axs[0, 0].set_xticks([1, 2])
axs[0, 0].set_xticklabels(['Caso 1', 'Caso 2'])
axs[0, 0].set_ylabel('Error')
axs[0, 0].set_title('Error Absoluto')
axs[0, 0].grid(True)

# Gráfica de líneas para el error relativo
axs[0, 1].plot([1, 2], errores_rel, marker='o', color='red', label='Error relativo')
axs[0, 1].set_xticks([1, 2])
axs[0, 1].set_xticklabels(['Caso 1', 'Caso 2'])
axs[0, 1].set_ylabel('Error')
axs[0, 1].set_title('Error Relativo')
axs[0, 1].grid(True)

# Gráfica de barras para el error porcentual
axs[1, 0].bar([1, 2], errores_pct, label='Error porcentual', color='green')
axs[1, 0].set_xticks([1, 2])
axs[1, 0].set_xticklabels(['Caso 1', 'Caso 2'])
axs[1, 0].set_ylabel('Error (%)')
axs[1, 0].set_title('Error Porcentual')
axs[1, 0].grid(True)

# Gráfica de líneas para el error cuadrático
axs[1, 1].plot([1, 2], errores_cuad, marker='s', color='purple', label='Error cuadrático')
axs[1, 1].set_xticks([1, 2])
axs[1, 1].set_xticklabels(['Caso 1', 'Caso 2'])
axs[1, 1].set_ylabel('Error')
axs[1, 1].set_title('Error Cuadrático')
axs[1, 1].grid(True)

plt.tight_layout() # Ajusta el espaciado entre subplots
plt.show()