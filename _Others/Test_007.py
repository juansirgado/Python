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
#----------------------------------------------------------#
print("============================================================")
dic_drives = psu.disk_io_counters(perdisk=True).keys()
for int_drive, str_drive in enumerate(dic_drives):
    if (str_drive[0:4] != "loop"):
        print(int_drive, str_drive)

print("============================================================")
dic_partitions = psu.disk_partitions(all=False)
for int_partition, str_partition in enumerate(dic_partitions):
    str_filesystem = str_partition.fstype
    if (str_filesystem != "squashfs"):
        print(int_partition, str_filesystem)

# str_device = psu.disk_partitions()[int_device].device

#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#