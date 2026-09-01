#!/bin/bash
#
#==========================================================#
# crontab schedule command: crontab -e 
# add line: minute hour day-month month week-day command
# */5 * * * * /home/juan/SystemMonitor/SystemMonitor.sh
#==========================================================#
#
#==========================================================#
# System Monitor Start
#==========================================================#
# echo "Hello World:" `date`
#
cd /home/juan/SystemMonitor
/bin/python3 ./SystemMonitor.py
#
# echo "Bye Bye:" `date`
#==========================================================#
# That is all Folks!
#==========================================================#
