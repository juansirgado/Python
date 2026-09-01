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
import psycopg2 as pgs       # pip install psycopg2
import src.config as cnf     # file src\config.py
import src.system_log as log # file src\system_log.py
#----------------------------------------------------------#
log.system_log("SM_Network()", "Start")
#----------------------------------------------------------#
# Connection and Cursor for PostGreSQL
#----------------------------------------------------------#
con = pgs.connect(host=cnf.postgresql['host'],
                  port=cnf.postgresql['port'],
                  database=cnf.postgresql['database'],
                  user=cnf.postgresql['user'],
                  password=cnf.postgresql['password'])
cur = con.cursor()
#----------------------------------------------------------#
# Create of the Inserts commands for the PostGreSQL
#----------------------------------------------------------#
sql_list = [] # empty list
sql_prefix  = "INSERT INTO tb_network (" 
sql_prefix += "net_ts_facility,"   
sql_prefix += "net_nm_machine,"   
sql_prefix += "net_vl_facility,"   
sql_prefix += "net_tp_unit,"
sql_prefix += "net_ds_facility"
sql_prefix += ") VALUES ("
sql_prefix += "CURRENT_TIMESTAMP,"
sql_prefix += "'" + sck.gethostname() + "',"
#----------------------------------------------------------#
# Create the Network Read in MB SQL
#----------------------------------------------------------#
sql_insert  = sql_prefix
sql_insert += str(psu.net_io_counters().bytes_sent / 2 ** 20) + ","
sql_insert += "'MB',"
sql_insert += "'Network Sent');"
sql_list.append(sql_insert)
#----------------------------------------------------------#
# Create the Network Write in MB SQL
#----------------------------------------------------------#
sql_insert  = sql_prefix
sql_insert += str(psu.net_io_counters().bytes_recv / 2 ** 20) + ","
sql_insert += "'MB',"
sql_insert += "'Network Received');"
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
    log.system_log("SM_Network(Status)", cur_status)
    log.system_log("SM_Network(Select)", sql_insert)
    log.system_log("SM_Network(Error)", error)
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
log.system_log("SM_Network()", "Stop")
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#