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
import psycopg2 as pgs       # pip install psycopg2
#----------------------------------------------------------#
import src.config as cnf       # file src\config.py
import src.system_log as log   # file src\system_log.py
import src.SM_Processor as prc # file src\SM_Processor.py
import src.SM_Memory as mem    # file src\SM_Memory.py
import src.SM_Drive as drv     # file src\SM_Drive.py
import src.SM_Partition as prt # file src\SM_Partition.py
import src.SM_Network as net   # file src\SM_Network.py
import src.SM_Machine as mch   # file src\SM_Machine.py
#----------------------------------------------------------#
log.system_log("SystemMonitor()", "Start")
#----------------------------------------------------------#
# Connection and Cursor for PostGreSQL
#----------------------------------------------------------#
con = pgs.connect(host=cnf.postgresql["host"],
                  port=cnf.postgresql["port"],
                  database=cnf.postgresql["database"],
                  user=cnf.postgresql["user"],
                  password=cnf.postgresql["password"])
cur = con.cursor()
#----------------------------------------------------------#
sql_insert = "" # empty insert
sql_list = [] # empty list
#----------------------------------------------------------#
# Create of the Inserts Processor for the PostGreSQL
#----------------------------------------------------------#
sql_processor = prc.SM_Processor(bln_logical=True)
for sql_measure in sql_processor:
    sql_list.append(sql_measure)
#----------------------------------------------------------#
# Create of the Inserts Memory for the PostGreSQL
#----------------------------------------------------------#
sql_memory = mem.SM_Memory()
for sql_measure in sql_memory:
    sql_list.append(sql_measure)
#----------------------------------------------------------#
# Create of the Inserts Drive for the PostGreSQL
#----------------------------------------------------------#
dic_drives = psu.disk_io_counters(perdisk=True).keys()
for int_drive, str_drive in enumerate(dic_drives):
    sql_drive = drv.SM_Drive(str_drive=str_drive) 
    if (str_drive[0:4] != "loop"):
        for sql_measure in sql_drive:
            sql_list.append(sql_measure)
#----------------------------------------------------------#
# Create of the Inserts Partition for the PostGreSQL
#----------------------------------------------------------#
dic_partitions = psu.disk_partitions(all=False)
for int_partition, str_partition in enumerate(dic_partitions):
    str_filesystem = str_partition.fstype
    if (str_filesystem != "squashfs" and str_filesystem != ""):
        sql_partition = prt.SM_Partition(int_partition=int_partition)
        for sql_measure in sql_partition:
            sql_list.append(sql_measure)
#----------------------------------------------------------#
# Create of the Inserts Network for the PostGreSQL
#----------------------------------------------------------#
dic_nics = psu.net_io_counters(pernic=True).keys()
for str_nic in dic_nics:
    sql_network = net.SM_Network(str_nic=str_nic)
    for sql_measure in sql_network:
        sql_list.append(sql_measure)
#----------------------------------------------------------#
# Create of the Inserts Machine for the PostGreSQL
#----------------------------------------------------------#
sql_machine = mch.SM_Machine()
for sql_measure in sql_machine:
    sql_list.append(sql_measure) 
#----------------------------------------------------------#
# for str_sql in sql_list:
#     print(str_sql)
#----------------------------------------------------------#
# Execute of the Inserts commands in the PostGreSQL
#----------------------------------------------------------#
try:
    for sql_insert in sql_list:
        cur_status = cur.execute(sql_insert)
#----------------------------------------------------------#
# Handle Errors and do the Rollback of the Inserts
#----------------------------------------------------------#
except (Exception, pgs.DatabaseError) as error:
    log.system_log("SystemMonitor(Status)", cur_status)
    log.system_log("SystemMonitor(Select)", sql_insert)
    log.system_log("SystemMonitor(Error)", error)
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
log.system_log("SystemMonitor()", "Stop")
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#