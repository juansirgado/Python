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
import sympy as sp
#----------------------------------------------------------#
# Constants
m0 = 9.11e-28  # Rest mass of the electron (grams)
# m = 0.001  # Desired relativistic mass (kg)
m = m0  # Desired relativistic mass (kg)
c = 3e8  # Speed of light (m/s)
n = 100 # number of terms (n)
f = 3e7 # factor of term

# Relativistic mass equation
for l in range(n, 0, -1):
    v = c - (l / f)
    mv = m / sp.sqrt(1 - (v**2 / c**2))
    print(f'{mv:10.40f}')
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#