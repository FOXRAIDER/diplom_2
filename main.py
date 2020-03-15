from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton, QLabel
from main_window import Ui_MainWindow  # импорт нашего сгенерированного файла
from struct import *
import sys, os
import encoder, decoder
 
 
class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.button()

    def button(self):
        btn1 = self.ui.compress
        btn2 = self.ui.decompress
        btn1.clicked.connect(self.button_compress)
        btn2.clicked.connect(self.button_decompress)
    
    def button_compress(self):
        w = QFileDialog.getOpenFileName(self, 'Open file')[0]
        lab = QLabel(self)
        lab.setGeometry(60,280,230,40)
        lab.setText(w)        
        but = QPushButton(self)
        but.setGeometry(70,350,180,40)
        but.setText('Архивировать')
        but.clicked.connect(lambda: self.compress(w))        
        lab.show()
        but.show()


    def compress(self,w):
        with open(w, 'r') as f:
            p = f.read()
            temp = encoder.coder.compress(p)
            print(temp)
            mywindow.save_bin_file(self, temp)

    def decompress(self, w):
        with open('case.txt', 'r') as f:
            case = []
            for i in f.read():
                case.append(int(i))
            print(case)
        



        # output = []
        # with open(w, 'rb') as f:
        #     data = f.read()
        #     while i <= len(case)-1:
        #         if i == 1:
        #             print('True')
        #         elif i == 2:
        #             print('False')

                    

        # case_b = []
        # k,i = 0,0
        # with open(w, 'rb') as f:
        #     while i <= len(case)-1:
        #         data = f.read()
        #         if case[i] == 1:
        #            case_b.append(data[i:i+1]) 
        #            i+=1
        #         elif case[i] == 2:
        #             if k < i:
        #                 k = i
        #                 case_b.append(data[k:k+2])
        #                 i+=1
        #                 k+=2
        #             elif k>=i:
        #                 case_b.append(data[k:k+2])
        #                 i+=1
        #                 k+=2
        #         else:
        #             pass
        
        # print(case_b)
        
        


        
    def save_bin_file(self, temp):
        case = []
        with open('compressing.bin', 'wb') as f:
            for i in temp:
                if i < 256:
                    f.write(pack('B', i))
                    case.append(1)
                else:
                    f.write(pack('H', i))
                    case.append(2)

        with open('case.txt', 'w') as f:
            for i in case:
                i = str(i)
                f.write(i)
    
    def button_decompress(self):
        w = QFileDialog.getOpenFileName(self, 'Open file', filter = '*.bin')[0]
        lab = QLabel(self)
        lab.setGeometry(60,280,230,40)
        lab.setText(w)        
        but = QPushButton(self)
        but.setGeometry(70,350,180,40)
        but.setText('Разархивировать')
        but.clicked.connect(lambda: self.decompress(w))        
        lab.show()
        but.show()

        

    
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())