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
from graphics import *
import time
#----------------------------------------------------------#
win = GraphWin('Back and Forth', 300, 300)
#win.yUp() # make right side up coordinates!
#----------------------------------------------------------#
rect = Rectangle(Point(200, 90), Point(220, 100))
rect.setFill("blue")
rect.draw(win)
#----------------------------------------------------------#
cir1 = Circle(Point(40,100), 25)
cir1.setFill("yellow")
cir1.draw(win)
#----------------------------------------------------------#
cir2 = Circle(Point(150,125), 25)
cir2.setFill("red")
cir2.draw(win)
#----------------------------------------------------------#
for i in range(46):
    cir1.move(5, 0)
    time.sleep(.05)
#----------------------------------------------------------#
for i in range(46):
    cir1.move(-5, 0)
    time.sleep(.05)
#----------------------------------------------------------#
win.promptClose(win.getWidth()/2, 20)
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#