#----------------------------------------------------------#
#             Program: SM_Machine 2025/06/04               #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Date         : 2025-06-04                                #
# Version      : 1.0                                       #
# Description  : Load Machine Info in the PostgreSQL       #
#----------------------------------------------------------#
import os
import psutil as psu         # pip install psutil
import socket as sck         # pip install socket
import src.system_log as log # file src\system_log.py
#----------------------------------------------------------#
def SM_Machine():
    #----------------------------------------------------------#
    log.system_log("SM_Machine()", "Start")
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
    sql_prefix += "'Machine',"
    sql_prefix += "'" + os.name.upper() + "',"
    #----------------------------------------------------------#
    # Create the Machine Read in MB SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(len(psu.pids())) + ","
    sql_insert += "'Count',"
    sql_insert += "'Total tasks',"
    sql_insert += "'Tasks');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    # Create the Machine Write in MB SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(len(psu.users())) + ","
    sql_insert += "'Count',"
    sql_insert += "'Total users',"
    sql_insert += "'Users');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    log.system_log("SM_Machine()", "Stop")
    #----------------------------------------------------------#
    return(sql_list)
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#