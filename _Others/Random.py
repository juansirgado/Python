#==========================================================#
#              Program: Random 2021/06/24                  #
#               All rights reserved 2021                   #
#==========================================================#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#==========================================================#
# Description:                                             # 
# Gerador de sequencias pseudo randomicas                  #
#==========================================================#
import random
#==========================================================#
random.seed(19670924,2)
for x in range(1, 81, 1):
   print("{:03.0f}".format(x) + 
         ": 01=" + "{:02.0f}".format(random.randint(0,60)) +
         ": 02=" + "{:02.0f}".format(random.randint(0,60)) +
         ": 03=" + "{:02.0f}".format(random.randint(0,60)) +
         ": 04=" + "{:02.0f}".format(random.randint(0,60)) +
         ": 05=" + "{:02.0f}".format(random.randint(0,60)) +
         ": 06=" + "{:02.0f}".format(random.randint(0,60)))
#==========================================================#
# That is all folks!                                       #
#==========================================================#