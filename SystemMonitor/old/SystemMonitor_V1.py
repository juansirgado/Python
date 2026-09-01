# Python
import os
import psutil
import socket

print("CPU Count", psutil.cpu_count())
print("CPU Frequence Cur", psutil.cpu_freq().current)
print("CPU Frequence Min", psutil.cpu_freq().min)
print("CPU Frequence Max", psutil.cpu_freq().max)
print("CPU Usage %", psutil.cpu_percent(0.1))
print("\n")

print("Memory Used GB", "{:.2f}".format(psutil.virtual_memory().used / 2 ** 30))
print("Memory Free GB", "{:.2f}".format(psutil.virtual_memory().free / 2 ** 30))
print("Memory Total GB", "{:.2f}".format(psutil.virtual_memory().total / 2 ** 30))
print("Memory Used %", psutil.virtual_memory().percent)
print("\n")

print("Disk Root", os.sep)
print("Disk Used GB", "{:.2f}".format(psutil.disk_usage(os.sep).used / 2 ** 30))
print("Disk Free GB", "{:.2f}".format(psutil.disk_usage(os.sep).free / 2 ** 30))
print("Disk Total GB", "{:.2f}".format(psutil.disk_usage(os.sep).total / 2 ** 30))
print("Disk Used %", psutil.disk_usage(os.sep).percent)
print("\n")

print("Disk Read MB", "{:.2f}".format(psutil.disk_io_counters().read_bytes / 2 ** 30))
print("Disk Write MB", "{:.2f}".format(psutil.disk_io_counters().write_bytes / 2 ** 30))
print("\n")

print("Net Sent MB", "{:.2f}".format(psutil.net_io_counters().bytes_sent / 2 ** 20))
print("Net Receive MB", "{:.2f}".format(psutil.net_io_counters().bytes_recv / 2 ** 20))
print("\n")

print("Total Process", len(psutil.pids()))
print("\n")

print("Battery Charge %", psutil.sensors_battery()) # .percent)
print("\n")

print("Operational System", os.name.upper())
print("Host", socket.gethostname())
print("User", psutil.users()[0].name)
print("\n")

print("001 - ", psutil.boot_time())
print("002 - ", psutil.cpu_times())
print("004 - ", psutil.disk_partitions()[0])
print("005 - ", psutil.disk_io_counters())
print("007 - ", psutil.sensors_battery())
print("008 - ", psutil.net_if_stats().keys())
print("009 - ", psutil.users()[0])
