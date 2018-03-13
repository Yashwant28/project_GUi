import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("C")
      self.cb.addItem("C++")
      self.cb.addItems(["Java", "C#", "Python"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
		
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setWindowTitle("combo box demo")
      self.setGeometry(50,50,900,900)

   def selectionchange(self):
      print "selection is ",self.cb.currentText()
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
