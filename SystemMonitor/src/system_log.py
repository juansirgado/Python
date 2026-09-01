#----------------------------------------------------------#
#         Program: System Monitor System_log.py            #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Date         : 2025-06-04                                #
# Version      : 1.0                                       #
# Description  : Create the system Log files               #
#----------------------------------------------------------#
import datetime as dtm # pip install datetime
#----------------------------------------------------------#
# Write system Log
#----------------------------------------------------------#
def system_log(log_member, log_message):
    log_record = str(dtm.datetime.now()) + ", " + str(log_member) + ", " + str(log_message) + ";\n"
    try:
        log_file = open("./log/SystemMonitor_Log_" + str(dtm.date.today()) + ".txt", 'a')
        log_file.write(log_record)
        log_file.close()
    except:
        log_status = "U99"
    finally:
        log_status = 0
    return(log_status)
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#