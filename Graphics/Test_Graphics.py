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
import matplotlib.pyplot as plt
from graphics import *
from datetime import datetime, timedelta
from playsound import playsound
#----------------------------------------------------------#
end_date = datetime.now()
start_date = end_date - timedelta(days=1*365)
#----------------------------------------------------------#
#Inicio da geração dos graficos
print("Start at:", datetime.now())

#Configuracao do grafico com base nos parametros
col_arr=["violet","indigo","blue","green","yellow","orange","red"]
graph_title  = "Rainbow Circle"
workArea = GraphWin(graph_title, 1920, 1080) # give title and dimensions
x=workArea.getWidth()/2 # get x of middle of drawing area
y=workArea.getHeight()/2 # get y of middle of drawing area

#----------------------------------------------------------#
#Desenha o grafico com base nos parametros

for i in range(7):
    cir=Circle(Point(x, y), 10+10*i)# draw circle with center at middle of drawing area
    cir.setOutline(col_arr[i]) #get a next outline color from color array
    cir.setWidth(4) #set outline width
    cir.draw(workArea) #draw the current circle
    
#----------------------------------------------------------#
#Aguarda acao para sair do grafico
message = Text(Point(workArea.getWidth()/2, 250), 'Click to Exit')
message.draw(workArea)
workArea.getMouse()# get mouse to click on screen to exit

#----------------------------------------------------------#
#Salva o grafico para consulta
image_name = "D:\\Temp\\Rainbow.eps"
#Image.save(GraphicsObject.draw(workArea),image_name)
workArea.postscript(file = image_name)
workArea.close() # close the drawing window

#----------------------------------------------------------#
#Final da geração dos graficos
print("Ended at:", datetime.now())
#Aviso de finalizado
playsound("D:\\Temp\\Done_Sound.wav")
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#