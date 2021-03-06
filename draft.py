#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from shell_ui import Ui_MainWindow
import os
import sys
from playsound import playsound
import re



class MyThread(QtCore.QThread):
    mySignal = QtCore.pyqtSignal(str)
    customSignal = QtCore.pyqtSignal(str)
    playMusic = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        #super(MyThread, self).__init(parent)
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.mp3FileName = 'Notification.mp3'

    def run(self):
        self.running = True
        #os.system('copy report.txt report2.txt')
        while self.running:
            if os.path.isfile(QtCore.QDir.current().absoluteFilePath('report.txt')) and os.path.isfile(QtCore.QDir.current().absoluteFilePath('scripted_report.acsup')):
                #if os.name=='posix' or os.name=='Linux':
                #    os.system('cp report.txt report2.txt')
                #else:
                #    os.system('copy report.txt report2.txt')
                with open("report.txt", 'r', encoding='cp1251') as file_handler:
                    self.listOfLines = file_handler.readlines()
                    self.peopleInQueue = re.findall('\d+', self.listOfLines[4])
                    self.waitingTime = re.findall('\d+', self.listOfLines[6])
                    print(self.waitingTime)
                    if (int((self.waitingTime)[0])>=420 or int((self.peopleInQueue)[0])>=7): # how much person waiting on the telephone line
                        print((self.waitingTime))
                        if os.path.isfile(QtCore.QDir.current().absoluteFilePath(self.mp3FileName)): # if >= 30 seconds then play Notification.mp3
                            self.playMusic.emit()
                            #os.system('cvlc --play-and-exit Notificaion.mp3') for linux
                            #os.system('vlc --play-and-exit -I dummy --dummy-quiet ./Notificaion.mp3')
                            print('>=420 seconds')
                        else:
                            print('There is no ALERT Notificaion.mp3') # nothing to play
                # remove files after checking the attribute 'Вызовы в очереди'
                os.remove(QtCore.QDir.current().absoluteFilePath('report.txt'))
                os.system('start "" "scripted_report.acsup"')
                self.sleep(5)
                os.system('taskkill /IM acsRep.exe')
                self.mySignal.emit(str(self.waitingTime[0]))
                print('Thread started!')
                self.sleep(30)
            else:
                self.sleep(60)
                os.system('taskkill /IM acsRep.exe')
                self.sleep(5)
                os.system('start "" "scripted_report.acsup"')
                self.customSignal.emit('Error - File report.txt or scripted_report.acsauto were not found')
                print('self.running = False')
                datetime=QtCore.QDateTime.currentDateTime()
                print(datetime.toString())


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        #super().__init__()
        #QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myThread = MyThread()     # create mytThread instance

        self.ui.pushButton_2.clicked.connect(self.startMonitoring)
        self.ui.pushButton.clicked.connect(self.stopMonitoring)
        self.myThread.mySignal.connect(self.updateLCD, QtCore.Qt.QueuedConnection)
        self.myThread.customSignal.connect(self.stopMonitoring, QtCore.Qt.QueuedConnection)
        self.myThread.playMusic.connect(self.playMusicFile, QtCore.Qt.QueuedConnection)

    def startMonitoring(self):
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.secWaiting.setEnabled(True)
            self.myThread.start()          # Start the thread

    def updateLCD(self, s):
        self.ui.secWaiting.display(int(s))
        # print(type(s),'---',s)

    def playMusicFile(self):
        playsound(QtCore.QDir.current().absoluteFilePath('Notification.mp3'))

    def stopMonitoring(self, s=None):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.secWaiting.setEnabled(False)
        self.myThread.running = False
        if s!=None:
            self.ui.statusbar.showMessage(str(s), 20000)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ico = QtWidgets.QWidget().style().standardIcon(QtWidgets.QStyle.SP_MediaVolume)
    app.setWindowIcon(ico)
    w = MyWin()
    w.show()
    sys.exit(app.exec())
