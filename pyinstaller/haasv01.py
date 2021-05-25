#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import subprocess
from haasv01ui import Ui_MainWindow
class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Example, self).__init__()
        #uic.loadUi('/home/haasm/scripts/haasv01.ui', self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.scanButton.clicked.connect(self.onClick)
        self.playButton.clicked.connect(self.onClickPlay)
    
    def onClick(self):
        adb = os.popen('adb devices').read().strip()   
        adb_devices = os.popen('adb devices | grep -v List | awk \'{print $1}\'').read().strip()  
        self.textEdit.setPlainText(adb) 
        if adb_devices:
            self.lineEdit.setText(adb_devices)
        if not adb_devices:
            self.lineEdit.setText('Error')

    def onClickPlay(self): 
        adb_devices = os.popen('adb devices | grep -v List | awk \'{print $1}\'').read().strip().split('\n') 
        #os.popen('scrcpy -m 720 -b 1M &').read().strip() 
        os.system(f'scrcpy -s {adb_devices[0]} -m 720 -b 1M')
        #self.textEdit.setPlainText(scrcpy) 

       

app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
