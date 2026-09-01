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
import psycopg2 as pgs       # pip install psycopg2
import src.config as cnf     # file src\config.py
import src.system_log as log # file src\system_log.py
#----------------------------------------------------------#
log.system_log("SM_Processor()", "Start")
#----------------------------------------------------------#
# Connection and Cursor for PostGreSQL
#----------------------------------------------------------#
con = pgs.connect(host=cnf.postgresql["host"],
                  port=cnf.postgresql["port"],
                  database=cnf.postgresql["database"],
                  user=cnf.postgresql["user"],
                  password=cnf.postgresql["password"])
cur = con.cursor()
cur_status = ""
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
sql_prefix += "'Processor',"
sql_prefix += "'All',"

#----------------------------------------------------------#
# Create the Processors total count SQL
#----------------------------------------------------------#
sql_insert  = sql_prefix
sql_insert += str(psu.cpu_count()) + ","
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
sql_insert = ""
sql_count = len(sql_list)
#----------------------------------------------------------#
# Execute of the Inserts commands in the PostGreSQL
#----------------------------------------------------------#
try:
    for sql_index, sql_insert in enumerate(sql_list):
        cur_status = cur.execute(sql_insert)
#----------------------------------------------------------#
# Handle Errors and do the Rollback of the Inserts
#----------------------------------------------------------#
except (Exception, pgs.DatabaseError) as error:
    log.system_log("SM_Processor(Status)", cur_status)
    log.system_log("SM_Processor(Select)", sql_insert)
    log.system_log("SM_Processor(Error)", error)
    con.rollback()
#----------------------------------------------------------#
# Inserts Commit in the PostGreSQL
#----------------------------------------------------------#
finally:
    if (con is not None):
        con.commit()
#----------------------------------------------------------#
# Close the Cursor and the Connection with the PostGreSQL
#----------------------------------------------------------#
cur.close()
con.close()
#----------------------------------------------------------#
log.system_log("SM_Processor()", "Stop")
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#