'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   l1 = QLabel()
   l1.setPixmap(QPixmap("python.jpg"))
	
   vbox = QVBoxLayout()
   vbox.addWidget(l1)
   #win.setLayout(vbox)
   #win.setWindowTitle("QPixmap Demo")
   win.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
'''

import os
import sys
from PyQt4.QtGui import *
 
# Create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("PyQT4 Pixmap @ pythonspot.com ") 
 
# Create widget
label = QLabel(w)
picfile='python.jpg'
logo = picfile
print logo
if os.path.isfile(logo):
	pixmap = QPixmap(logo)
	label.setPixmap(pixmap)
	w.resize(pixmap.width(),pixmap.height())
 
	# Draw window
	w.show()
	app.exec_()
else:
	print "I expected to find a png picture called logo.png in "+ os.getcwd()
