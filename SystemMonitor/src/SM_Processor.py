#----------------------------------------------------------#
#           Program: SM_Processor 2025/06/04               #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Date         : 2025-06-04                                #
# Version      : 1.0                                       #
# Description  : Load Processor Info in the PostgreSQL     #
#----------------------------------------------------------#
import psutil as psu         # pip install psutil
import socket as sck         # pip install socket
import src.system_log as log # file src\system_log.py
#----------------------------------------------------------#
def SM_Processor(bln_logical=True):
    #----------------------------------------------------------#
    log.system_log("SM_Processor()", "Start")
    #----------------------------------------------------------#
    sql_list = [] # empty list
    #----------------------------------------------------------#
    # Create of the Inserts commands for the PostGreSQL
    #----------------------------------------------------------# 
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
    sql_prefix += "'Processor',"
    sql_prefix += "'All',"
    #----------------------------------------------------------#
    # Create the Processors total count SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.cpu_count(logical=bln_logical)) + ","
    sql_insert += "'Count',"
    sql_insert += "'Total Threads',"
    sql_insert += "'Total');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    # Create the Processor current frequence SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.cpu_freq().current) + ","
    sql_insert += "'Mhz',"
    sql_insert += "'Current frequence',"
    sql_insert += "'Current');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    # Create the Processor minimum frequence SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.cpu_freq().min) + ","
    sql_insert += "'Mhz',"
    sql_insert += "'Minimun frequence',"
    sql_insert += "'Minimun');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    # Create the Processor maximum frequence SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.cpu_freq().max) + ","
    sql_insert += "'Mhz',"
    sql_insert += "'Maximum frequence',"
    sql_insert += "'Maximum');"
    sql_list.append(sql_insert)
    #----------------------------------------------------------#
    # Create the Processor usage percent SQL
    #----------------------------------------------------------#
    sql_insert  = sql_prefix
    sql_insert += str(psu.cpu_percent(0.1)) + ","
    sql_insert += "'%',"
    sql_insert += "'Used percent',"
    sql_insert += "'Used');"
    sql_list.append(sql_insert)
#----------------------------------------------------------#
    log.system_log("SM_Processor()", "Stop")
    return(sql_list)
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#