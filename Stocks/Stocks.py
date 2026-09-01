#----------------------------------------------------------#
#           Program: Load tb_acao 2021/07/01               #
#               All rights reserved 2021                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Description:                                             # 
# Carrega dados dos arquivos da bovespa no db_bovespa      #
#----------------------------------------------------------#
import yfinance as yfn
from datetime import datetime, timedelta
import dateutil
from playsound import playsound
#----------------------------------------------------------#
end_date = datetime.now()
start_date = end_date - timedelta(days=1*365)
#----------------------------------------------------------#
#Inicio da geração dos graficos
print("Start at:", datetime.now())
count = 0
mt_stock = ["IBM","AAPL","EMBR3.SA"]
#----------------------------------------------------------#
for cr_stock in mt_stock:
    count = +1
    #Obtem os dados via servico Yahoo
    df_stocks = yfn.download(cr_stock, start = start_date, end = end_date)
    #Colunas e Titulo do grafico
    print(df_stocks)

    graph_title  = "{:03}".format(count) + cr_stock + " - Stocks Graphic - Close"
    #Desenha o grafico com base nos parametros
    graph = df_stocks["Close"].plot(figsize=(16, 9), grid=True, title=graph_title)
    dir_name = str(int(start_date.year)) + "-" + "{:02}".format(start_date.month)
    image_name = "D:\\Temp\\" + "{:03}".format(count) + cr_stock + ".png"
    #Salva o grafico para consulta
    graph.figure.savefig(image_name)
    graph.clear()
#----------------------------------------------------------#
#Final da geração dos graficos
print("Ended at:", datetime.now())
#Aviso de finalizado
playsound("D:\\Temp\\Done_Sound.wav")
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#