#----------------------------------------------------------#
#               Program: System Monitor                    #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com.br        #
#----------------------------------------------------------#
# Date         : 2025-06-04                                #
# Version      : 1.0                                       #
# Description  : System Monitor for Servers/Computers      #
#----------------------------------------------------------#
import os
import psutil
import socket
#----------------------------------------------------------#
print("Processor Count", psutil.cpu_count())
print("Processor Frequence Cur", psutil.cpu_freq().current)
print("Processor Frequence Min", psutil.cpu_freq().min)
print("Processor Frequence Max", psutil.cpu_freq().max)
print("Processor Usage %", psutil.cpu_percent(0.1))
print("\n")
#----------------------------------------------------------#
print("Memory Used GB", "{:.2f}".format(psutil.virtual_memory().used / 2 ** 30))
print("Memory Free GB", "{:.2f}".format(psutil.virtual_memory().free / 2 ** 30))
print("Memory Total GB", "{:.2f}".format(psutil.virtual_memory().total / 2 ** 30))
print("Memory Used %", psutil.virtual_memory().percent)
print("\n")
#----------------------------------------------------------#
print("Storage Root", os.sep)
print("Storage Used GB", "{:.2f}".format(psutil.disk_usage(os.sep).used / 2 ** 30))
print("Storage Free GB", "{:.2f}".format(psutil.disk_usage(os.sep).free / 2 ** 30))
print("Storage Total GB", "{:.2f}".format(psutil.disk_usage(os.sep).total / 2 ** 30))
print("Storage Used %", psutil.disk_usage(os.sep).percent)
print("\n")
#----------------------------------------------------------#
print("Storage Read MB", "{:.2f}".format(psutil.disk_io_counters().read_bytes / 2 ** 20))
print("Storage Write MB", "{:.2f}".format(psutil.disk_io_counters().write_bytes / 2 ** 20))
print("\n")
#----------------------------------------------------------#
print("Network Sent MB", "{:.2f}".format(psutil.net_io_counters().bytes_sent / 2 ** 20))
print("Network Receive MB", "{:.2f}".format(psutil.net_io_counters().bytes_recv / 2 ** 20))
print("\n")
#----------------------------------------------------------#
print("Total Process", len(psutil.pids()))
print("\n")
#----------------------------------------------------------#
print("Battery Charge %", psutil.sensors_battery()) # .percent)
print("\n")
#----------------------------------------------------------#
print("Operational System", os.name.upper())
print("Host", socket.gethostname())
print("User", psutil.users()[0].name)
print("\n")
#----------------------------------------------------------#
print("001 - ", psutil.boot_time())
print("002 - ", psutil.cpu_times())
tmp_index = len(psutil.disk_partitions())
for tmp_part in range(0, tmp_index, 1):
    print("003 - ", psutil.disk_partitions()[tmp_part])
print("004 - ", psutil.disk_io_counters())
print("005 - ", psutil.sensors_battery())
print("006 - ", psutil.net_if_stats().keys())
tmp_index = len(psutil.users())
for tmp_user in range(0, tmp_index, 1):
    print("007 - ", psutil.users()[tmp_user])
#----------------------------------------------------------#
# That is all Folks!
#----------------------------------------------------------#