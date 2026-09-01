#----------------------------------------------------------#
#          Program: Load tb_capital 2020/06/30             #
#               All rights reserved 2020                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Description:                                             # 
# Carrega dados dos arquivos da bovespa no db_bovespa      #
#----------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt

# Constants
m0 = 9.11e-31  # Rest mass of the electron (kg)
c = 3e8  # Speed of light (m/s)

# Generate speeds from 0 to just below c
v = np.linspace(0, 0.999999999 * c, 1000)

# Compute relativistic mass
relativistic_mass = m0 / np.sqrt(1 - (v**2 / c**2))

# Convert mass to grams
relativistic_mass_grams = relativistic_mass * 1000

import sympy as sp
#----------------------------------------------------------#
# Constants
m0 = 9.11e-28  # Rest mass of the electron (grams)
# m = 0.001  # Desired relativistic mass (kg)
m = m0  # Desired relativistic mass (kg)
c = 3e8  # Speed of light (m/s)
n = 100 # number of terms (n)
f = 1000 # factor of term

vl = list()
ml = list()

# Relativistic mass equation
for l in range(n, 0, -1):
    v = c - (l / f)
    mv = m / sp.sqrt(1 - (v**2 / c**2))
    vl.append(v)
    ml.append(mv)
    print(f'{mv:10.40f}')


# Plot
plt.figure(figsize=(10, 6))
plt.plot(vl, ml)
plt.axhline(1, color='red', linestyle='--', label='1 gram')
plt.xlabel('Speed (% of speed of light)')
plt.ylabel('Relativistic Mass (grams)')
plt.title('Relativistic Mass of an Electron vs. Speed')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#