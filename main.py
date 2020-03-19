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
        
        with open(w, 'rb') as f:
            data = f.read()
        
        iterator_i = 0
        iterator_k = 0
        definaly_text = []
        finaly_text = []
        print(data)
        
       

        while iterator_i <= len(case)-1:
            if case[iterator_i] == 1:
                
                definaly_text.append(unpack('B', data[iterator_k:iterator_k+1]))
                iterator_i+=1
                iterator_k+=1
            elif case[iterator_i] == 2:
                
                definaly_text.append(unpack('H', data[iterator_k:iterator_k+2]))
                iterator_i+=1
                iterator_k+=2
            
        for i in definaly_text:
            finaly_text.append(int(i[0]))
        

        with open('compressing.txt', 'w') as f:
            _data = decoder.decompress.decompress(finaly_text)
            f.write(_data)

       


        
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