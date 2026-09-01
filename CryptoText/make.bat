@echo on
set path_py=%path%
set path=%path%;C:\Users\Juan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts
cd \
D:
cd D:\_Work\__Diversos\Python\CryptoText
pyinstaller --console --noconfirm --onefile CryptoText.py
set path=%path_py%
pause 