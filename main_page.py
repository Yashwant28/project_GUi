import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

noy = ""
eoy = ""

class Window(QtGui.QMainWindow):
	
	def __init__(self):
		super(Window,self).__init__()
		self.home()
	
	def home(self):
		self.setGeometry(50,50,800,600)
		self.setWindowTitle("The Prediction System")
		self.setWindowIcon(QtGui.QIcon('logo.jpg'))
		
		extractAction1 = QtGui.QAction("&New Window",self)
		extractAction1.setShortcut("Ctrl+N")
		extractAction1.setStatusTip('Open New Window')
		extractAction1.triggered.connect(self.__init__)
		
		extractAction2 = QtGui.QAction("&Close",self)
		extractAction2.setShortcut("Ctrl+Q")
		extractAction2.setStatusTip('Leave The App')
		extractAction2.triggered.connect(self.close_application)
		
		
		self.statusBar()
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction1)
		fileMenu.addAction(extractAction2)
		
			
		l1 = QtGui.QLabel(self)
		l11 = QtGui.QLabel(self)
		l12 = QtGui.QLabel(self)
		l13 = QtGui.QLabel(self)
		l14 = QtGui.QLabel(self)
		l2 = QtGui.QLabel(self)
		l3 = QtGui.QLabel(self)
		
		lable_main = QtGui.QLabel(self)
		lable_main.setPixmap(QPixmap("main_page.jpg"))
		lable_main.resize(500,200)
		lable_main.move(50,50)
		
   		l2.setText("Name : ")
   		l2.move(50,250)
		
   		l3.setText("Email ID : ")
   		l3.move(50,300)
		
		flo = QtGui.QFormLayout()

		self.name_line = QtGui.QLineEdit(self)
		self.name_line.textChanged.connect(self.name_text)
		self.name_line.move(150,250)
		self.name_line.resize(300,30)
		
		self.email_line = QtGui.QLineEdit(self)
		self.email_line.textChanged.connect(self.email_text)
		self.email_line.move(150,300)
		self.email_line.resize(300,30)

		btn = QtGui.QPushButton("Next", self)
		btn.clicked.connect(self.next_page)
		btn.resize(100,50)
		btn.move(50,400)
		
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(100,50)
		btn.move(200,400)
		self.show()
	
	def name_text(self):
		global noy
		noy = self.name_line.text()
					
	def email_text(self):
		global eoy
		eoy = self.email_line.text()
		
		
	def next_page(self):	
		print("opening next page")
		global noy
		global eoy
		print "name : ",str(noy)
		print "email : ",str(eoy)
		os.system("python second_page.py")
		sys.exit()
		
	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Warning!!', "Are You Really Want To Close this App ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)		
		if choice == QtGui.QMessageBox.Yes:
			print ("Babye!!!!")
			sys.exit()
		else:
			pass
		 		
   
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
	
run()



