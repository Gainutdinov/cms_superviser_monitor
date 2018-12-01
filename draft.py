# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from shell_ui import Ui_MainWindow
import os
import sys
from playsound import playsound
import threading



class MyWin(QtWidgets.QMainWindow):    
    def __init__(self, parent=None):
        super().__init__()
        #QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# threading.Timer(60.0, hello_world).start()
# mp3FileName = 'Notification.mp3'

# if os.path.isfile(QtCore.QDir.current().absoluteFilePath('report.txt')):
#     if os.name=='posix' or os.name=='Linux':
#         os.system('cp report.txt report2.txt')
#     else:
#         os.system('copy report.txt report2.txt')
#     with open("report2.txt", 'r', encoding='cp1251') as file_handler:
#         waitingTime = list(filter(str.isdigit, file_handler.readlines()[4]))
#         if (int(''.join(waitingTime))>=30): # how much person waiting on the telephone line
#             print(int(''.join(waitingTime)))
#             if os.path.isfile(QtCore.QDir.current().absoluteFilePath(mp3FileName)):
#                 playsound(QtCore.QDir.current().absoluteFilePath(mp3FileName))
#                 print('>=30 seconds')
#             else:
#                 print('ALERT Notificaion.mp3')
#         else:
#             print(int(''.join(waitingTime)))
#             print('Fine')
#     # remove files after checking the attribute 'Вызовы в очереди'
#     os.remove(QtCore.QDir.current().absoluteFilePath('report.txt'))
#     os.remove(QtCore.QDir.current().absoluteFilePath('report2.txt'))
# else:
#     print('report.txt file was not found :(')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec())
