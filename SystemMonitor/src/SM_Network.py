#----------------------------------------------------------#
#             Program: SM_Network 2025/06/04               #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Date         : 2025-06-04                                #
# Version      : 1.0                                       #
# Description  : Load Network Info in the PostgreSQL       #
#----------------------------------------------------------#
import psutil as psu         # pip install psutil
import socket as sck         # pip install socket
import src.system_log as log # file src\system_log.py
#----------------------------------------------------------#
def SM_Network(str_nic):
    #----------------------------------------------------------#
    log.system_log("SM_Network()", "Start")
    #----------------------------------------------------------#
    # Create of the Inserts commands for the PostGreSQL
    #----------------------------------------------------------#
    sql_list = [] # empty list
    sql_prefix  = "INSERT INTO tb_facility (" 
    sql_prefix += "fcl_sq_facility,"   
    sql_prefix += "fcl_ts_facility,"   
    sql_prefix += "fcl_nm_machine,"   
    sql_prefix += "fcl_tp_facility,"   
    sql_prefix += "fcl_id_facility,"   
    sql_prefix += "fcl_vl_facility,"   
    sql_prefix += "fcl_tp_unit,"
    sql_prefix += "fcl_ds_facility,"
    sql_prefix += "fcl_ds_alias"
    sql_prefix += ") VALUES ("
    sql_prefix += "NEXTVAL('sq_tb_facility'),"  
    sql_prefix += "CURRENT_TIMESTAMP,"
    sql_prefix += "'" + sck.gethostname() + "',"
    sql_prefix += "'Network',"
    sql_prefix += "'" + str_nic + "',"
    #----------------------------------------------------------#
    # Create the Network Read in MB SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.net_io_counters(pernic=True)[str_nic].bytes_sent / 2 ** 20) + ","
    sql_insert += "'MB',"
    sql_insert += "'Total sent',"
    sql_insert += "'Sent');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    # Create the Network Write in MB SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.net_io_counters(pernic=True)[str_nic].bytes_recv / 2 ** 20) + ","
    sql_insert += "'MB',"
    sql_insert += "'Total received',"
    sql_insert += "'Received');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    log.system_log("SM_Network()", "Stop")
    #----------------------------------------------------------#
    return(sql_list)
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#