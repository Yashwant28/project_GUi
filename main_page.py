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
		self.setWindowIcon(QtGui.QIcon('1.jpg'))
		
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
		
		l1.setText("Welcome To !!!!")
		l1.move(100,50)
		
		l11.setText("The Real ")
		l11.move(100,70)
		
		l12.setText("Estate Price ")
		l12.move(165,70)
		
		l13.setText("Prediction ")
		l13.move(250,70)
		
		l14.setText("System.!!")
		l14.move(325,70)
		
   		l2.setText("Name : ")
   		l2.move(75,150)
		
   		l3.setText("Email ID : ")
   		l3.move(75,200)
		
		flo = QtGui.QFormLayout()

		self.name_line = QtGui.QLineEdit(self)
		self.name_line.textChanged.connect(self.name_text)
		self.name_line.move(150,150)
		self.name_line.resize(300,30)
		
		self.email_line = QtGui.QLineEdit(self)
		self.email_line.textChanged.connect(self.email_text)
		self.email_line.move(150,200)
		self.email_line.resize(300,30)

		btn = QtGui.QPushButton("Next", self)
		btn.clicked.connect(self.next_page)
		btn.resize(100,50)
		btn.move(50,300)
		
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(100,50)
		btn.move(200,300)
		self.show()
	
	def name_text(self):
		global noy
		noy = self.name_line.text()
					
	def email_text(self):
		global eoy
		eoy = self.email_line.text()
		
		
	def next_page(self):	
		print("opening next page")
		os.system("python second_page.py")
		global noy
		global eoy
		print(noy)
		print(eoy)
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



