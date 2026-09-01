#----------------------------------------------------------#
#      Program: Yahoo Finance tb_acao 2021/07/01           #
#               All rights reserved 2021                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Description:                                             # 
# Obtem cotacao historica de acoes                         #
#----------------------------------------------------------#
import yfinance as yfn
import datetime as dtm
import playsound as psd
#----------------------------------------------------------#
end_date = dtm.datetime.now()
start_date = end_date - dtm.timedelta(days=1*365)
#----------------------------------------------------------#
#Inicio da geração dos graficos
print("Start at:", dtm.datetime.now())
count = 0

mt_stock = ["IBM","PTBL3.SA"]

for cr_stock in mt_stock:
    print("Step_001")
    count = +1
    print("Step_002")
    #Obtem os dados via servico Yahoo
    print("Step_003")
    df_stocks = yfn.download(cr_stock, interval = "1d", start = start_date, end = end_date, show_errors = True)
    print("Step_004")
    #Colunas e Titulo do grafico
    #print(df_stocks)

    print("Step_005")
    columns = ["Close"]
    print("Step_006")
    graph_title  = "{:03}".format(count) + " - " + cr_stock + " - Stocks Graphic - Close"
    print("Step_007")
    #Desenha o grafico com base nos parametros
    print("Step_008")
    graph = df_stocks[columns].plot(figsize=(16, 9), grid=True, title=graph_title)
    print("Step_009")
    dir_name = str(int(start_date.year)) + "-" + "{:02}".format(start_date.month)
    print("Step_010")
    image_name = "D:\\Temp\\" + "{:03}".format(count) + "_" + cr_stock + ".png"
    print("Step_011")
    #Salva o grafico para consulta
    print("Step_012")
    graph.figure.savefig(image_name)
    print("Step_013")
#----------------------------------------------------------#
#Final da geração dos graficos
print("Ended at:", dtm.datetime.now())
#Aviso de finalizado
print("Step_014")
psd.playsound("D:\\Temp\\Done_Sound.wav")
print("Step_015")
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#