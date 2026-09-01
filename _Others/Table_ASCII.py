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
for x in range(0, 16, 1):
   for y in range(0, 16, 1):
       v = chr((x*16)+y)
       print(v + "  " ,end="")
   print(";")
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#