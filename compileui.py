from PyQt5 import uic

with open("mdleditgui.py","w",encoding="utf-8") as f:
    uic.compileUi("mdledit.ui",f)