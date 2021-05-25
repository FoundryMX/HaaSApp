#!/usr/bin/env python3

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import subprocess

class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('/home/haasm/scripts/haas_file/haasv01.ui', self)
        self.scanButton.clicked.connect(self.onClick)
        self.playbutton_1.clicked.connect(self.onClickPlay1)
        self.playbutton_2.clicked.connect(self.onClickPlay2)
        self.playbutton_3.clicked.connect(self.onClickPlay3)
        self.rebootbutton_1.clicked.connect(self.onreboot1)
        self.rebootbutton_2.clicked.connect(self.onreboot2)
        self.rebootbutton_3.clicked.connect(self.onreboot3)

    
    def onClick(self):
        adb = os.popen('adb devices').read().strip()   
        adb_devices = os.popen('adb devices | grep -v List | awk \'{print $1}\'').read().strip()
        self.devices = os.popen('adb devices | grep -v List | grep -v list | awk \'{print $1}\'').read().strip().split('\n') 
        self.devices_message.setPlainText(adb)      
        self.device1_text.setText('')
        self.device2_text.setText('')
        self.device3_text.setText('')
        if adb_devices:
            try:
                self.device1_text.setText(self.devices[0])
                self.device2_text.setText(self.devices[1])
                self.device3_text.setText(self.devices[2])
            except:
                pass
        if not adb_devices:
            self.lineEdit.setText('Error')

    def onClickPlay1(self): 
        #adb_devices = os.popen('adb devices | grep -v list | grep -v list | awk \'{print $1}\'').read().strip().split('\n') 
        try:
            #os.popen('scrcpy -m 720 -b 1m &').read().strip() 
            os.system(f'scrcpy -m 720 -b 1m -s {self.devices[0]} &')
            #self.textedit.setplaintext(scrcpy) 
        except:
            pass
    
    def onClickPlay2(self): 
        #adb_devices = os.popen('adb devices | grep -v list | grep -v list | awk \'{print $1}\'').read().strip().split('\n') 
        try:
            #os.popen('scrcpy -m 720 -b 1m &').read().strip() 
            os.system(f'scrcpy -m 720 -b 1m -s {self.devices[1]} &')
            #self.textedit.setplaintext(scrcpy) 
        except:
            pass
    
    def onClickPlay3(self): 
        #adb_devices = os.popen('adb devices | grep -v list | grep -v list | awk \'{print $1}\'').read().strip().split('\n') 
        try:
            #os.popen('scrcpy -m 720 -b 1m &').read().strip() 
            os.system(f'scrcpy -m 720 -b 1m -s {self.devices[2]} &')
            #self.textedit.setplaintext(scrcpy) 
        except:
            pass

    def onreboot1(self):
        try:
            os.system(f'adb -s {self.devices[0]} reboot')

        except:
            pass

    def onreboot2(self):
        try:
            os.system(f'adb -s {self.devices[1]} reboot')

        except:
            pass

    def onreboot3(self):
        try:
            os.system(f'adb -s {self.devices[2]} reboot')

        except:
            pass

app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
