from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton, QLabel
from main_window import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import encoder
 
 
class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.compress()    
        self.open_file()

    def open_file(self):
        w = self.ui.open_file
        w.clicked.connect(self.button_open_file)
    
    def compress(self):
        w = self.ui.compress
        w.clicked.connect(self.button_clicked)
        
    
    

    def button_open_file(self):
        w = QFileDialog.getOpenFileName(self, 'Open file')[0]

        e = self.ui.label_8
        e.setText(w)

        f = open(w, 'r')
        with f:
            global data
            data = f.read()
            
        #qwe = encoder.coder.compress(data)
        
        print(data)

    def button_clicked(self):

        qwe = encoder.coder.compress(data)
        print(qwe)    
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())