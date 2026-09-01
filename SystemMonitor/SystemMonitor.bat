@echo off
::========================================================::
:: crontab schedule command:
:: crontab */5 * * * * D:\_Work\__Diversos\Python\SystemMonitor\SystemMonitor.bat
::========================================================::
::
::========================================================::
:: System Monitor Start
::========================================================::
@echo "Hello World:" %date%-%time%
:: 
D:
cd \_Work\__Diversos\Python\SystemMonitor
echo C:\Program Files\Python313\python.exe SystemMonitor.py
:: 
@echo "Bye Bye:" %date%-%time%
::========================================================::
:: That is all Folks!
::========================================================::
