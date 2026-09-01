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
import secrets as sc
#----------------------------------------------------------#
# new parword create
new_token = sc.token_hex(8)
# new password print
print(new_token)
#new_text = bytes.fromhex(new_token).decode('utf-8')
#print(new_text)
#----------------------------------------------------------#
for i in range(0, len(new_token), 2):
   pair = new_token[i:i+2]
   char = chr(int(pair, 16))
   print(char,end="")
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#