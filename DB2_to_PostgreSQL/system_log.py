#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
import config                 # file config.py
from datetime import date     # pip install datetime
from datetime import datetime # pip install datetime
#-------------------------------------------------------------------------------
# Grava log do systema
#-------------------------------------------------------------------------------
def system_log(log_member, log_message):
    # print("Author: ", config.author)
    log_record = str(datetime.now()) + ", " + log_member + ", " + log_message + ";\n"
    try:
        log_file = open(".\\log\\FIS_Workload_Log_" + str(date.today()) + ".txt", 'a')
        log_file.write(log_record)
        log_file.close()
    except:
        log_status = "U99"
    finally:
        log_status = 0
    return(log_status)
#-------------------------------------------------------------------------------
# log_status = system_log("system_log()", "Test")
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------