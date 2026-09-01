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
import os, os.path
import win32com.client
#----------------------------------------------------------#
if os.path.exists("excelsheet.xlsm"):
    file_xlsm=win32com.client.Dispatch("Excel.Application")
    file_xlsm.Workbooks.Open(os.path.abspath("excelsheet.xlsm"))
    file_xlsm.Application.Run("excelsheet.xlsm!modulename.macroname")
    file_xlsm.Application.Save()
    file_xlsm.Application.Quit()
    del file_xlsm
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#