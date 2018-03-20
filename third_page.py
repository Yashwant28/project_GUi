import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

balconies = bathroom = opensides = overlooking = ownership = projectname = roadfaceing = age = totalfloor = ""
output = ""

class Window(QtGui.QMainWindow):
	
	def __init__(self):
		super(Window,self).__init__()
		self.home()
	
	def home(self):
		self.setGeometry(0,0,1500,1500)
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
		ll1 = QtGui.QLabel(self)
		l11 = QtGui.QLabel(self)
		l122 = QtGui.QLabel(self)
		l13 = QtGui.QLabel(self)
		l14 = QtGui.QLabel(self)
		l2 = QtGui.QLabel(self)
		l3 = QtGui.QLabel(self)
		
		l11.setText("The Real ")
		l11.move(100,20)
		
		l122.setText("Estate Price ")
		l122.move(165,20)
		
		l13.setText("Prediction ")
		l13.move(250,20)
		
		l14.setText("System.!!")
		l14.move(325,20)
		
		l1.setText("Select")
		l1.move(100,40)
		
		ll1.setText("Features:")
		ll1.move(145,40)
		
   		l3.setText("balconies: ")
   		l3.move(75,150)
		self.comboBox1 = QtGui.QComboBox(self)
		self.comboBox1.addItems(['0','1','2','3','4','5','6','7','8'])
		self.comboBox1.move(160,150)
		self.comboBox1.resize(300,30)
		self.comboBox1.currentIndexChanged.connect(self.balconies_menu)
		
		l4 = QtGui.QLabel(self) 
   		l4.setText("bathroom: ")
   		l4.move(75,200)
		self.comboBox2 = QtGui.QComboBox(self)
		self.comboBox2.addItems(['0','1','2','3','4','5','6','7','8','9','10'])
		self.comboBox2.move(160,200)
		self.comboBox2.resize(300,30)
		self.comboBox2.currentIndexChanged.connect(self.bathroom_menu)
		
		l5 = QtGui.QLabel(self)
		l5.setText("opensides:")
   		l5.move(75,250)
		self.comboBox3 = QtGui.QComboBox(self)
		self.comboBox3.addItems(['1','2','3','4','5'])
		self.comboBox3.move(160,250)
		self.comboBox3.resize(300,30)
		self.comboBox3.currentIndexChanged.connect(self.opensides_menu)
		
		l6 = QtGui.QLabel(self)
		l6.setText("overlooking: ")
   		l6.move(75,300)
		self.comboBox4 = QtGui.QComboBox(self)
		self.comboBox4.addItems(['Corner', 'Corner, Garden View', 'Corner, Garden View, Pool View', 'Corner, Garden View, Pool View, Road View', 'Corner, Garden View, Road View', 'Corner, Pool View, Road View', 'Garden View', 'Garden View, Pool View, Road View', 'Pool View', 'Pool View, Corner', 'Pool View, Garden View', 'Road View', 'Road View, Corner', 'Road View, Garden View', 'Road View, Pool View', 'overlooking'])
		self.comboBox4.move(160,300)
		self.comboBox4.resize(300,30)
		self.comboBox4.currentIndexChanged.connect(self.overlooking_menu)
		
		l7 = QtGui.QLabel(self)
		l7.setText("ownership: ")
   		l7.move(75,350)
		self.comboBox5 = QtGui.QComboBox(self)
		self.comboBox5.addItems(['Co-Operative Society', 'Freehold', 'Leasehol', 'Power of Attorney'])
		self.comboBox5.move(160,350)
		self.comboBox5.resize(300,30)
		self.comboBox5.currentIndexChanged.connect(self.ownership_menu)
		
		l9 = QtGui.QLabel(self)
		l9.setText("projectname: ")
   		l9.move(75,400)
		self.comboBox6 = QtGui.QComboBox(self)
		self.comboBox6.addItems(['55','66','77'])
		self.comboBox6.move(160,400)
		self.comboBox6.resize(300,30)
		self.comboBox6.currentIndexChanged.connect(self.projectname_menu)
		
		l10 = QtGui.QLabel(self)
		l10.setText("roadfacing: ")
   		l10.move(75,450)
		self.comboBox7 = QtGui.QComboBox(self)
		self.comboBox7.addItems(['1 feet', '10 feet', '100 feet', '1000 feet', '11 feet', '110 feet', '114 feet', '12 feet', '120 feet', '13 feet', '131 feet', '14 feet', '15 feet', '150 feet', '16 feet', '160 feet', '164 feet', '17 feet', '170 feet', '18 feet', '180 feet', '19 feet', '190 feet', '196 feet', '2 feet', '20 feet', '200 feet', '209 feet', '219 feet', '22 feet', '23 feet', '24 feet', '25 feet', '250 feet', '26 feet', '262 feet', '27 feet', '271 feet', '29 feet', '295 feet', '30 feet', '300 feet', '32 feet', '328 feet', '34 feet', '35 feet', '350 feet', '36 feet', '38 feet', '39 feet', '40 feet', '400 feet', '42 feet', '45 feet', '48 feet', '49 feet', '492 feet', '5 feet', '50 feet', '500 feet', '52 feet', '54 feet', '55 feet', '59 feet', '6 feet', '60 feet', '65 feet', '656 feet', '6561 feet', '66 feet', '68 feet', '7 feet', '70 feet', '72 feet', '780 feet', '8 feet', '80 feet', '82 feet', '85 feet', '9 feet', '90 feet', '98 feet', '984 feet'])
		self.comboBox7.move(160,450)
		self.comboBox7.resize(300,30)
		self.comboBox7.currentIndexChanged.connect(self.roadfaceing_menu)
		
		l11 = QtGui.QLabel(self)
		l11.setText("age: ")
   		l11.move(75,500)
		self.comboBox8 = QtGui.QComboBox(self)
		self.comboBox8.addItems(['2 - 3 years','0 - 1 year','1 - 2 years','6 - 7 years','2 years','3 - 4 years','10 - 11 years','7 - 8 years','4 - 5 years','5 - 6 years','12 - 13 years','11 - 12 years','1 year','17 years','6 years','12 years','7 years','20 years','20 - 21 years','9 - 10 years','13 - 14 years','19 - 20 years','14 - 15 years','15 years','17 - 18 years','8 - 9 years','19 years','25 years','30 years','3 years','18 - 19 years','26 - 27 years','11 years','21 - 22 years','16 - 17 years','15 - 16 years','30 - 31 years','28 - 29 years','5 years','4 years','9 years','10 years','8 years','13 years','22 - 23 years','18 years','21 years','22 years','14 years','16 years','27 - 28 years','28 years','24 - 25 years','25 - 26 years','40 years','37 - 38 years','35 - 36 years','35 years','41 - 42 years','29 - 30 years','27 years','31 - 32 years','42 years','33 - 34 years','23 years','32 - 33 years','26 years','23 - 24 years'])
		self.comboBox8.move(160,500)
		self.comboBox8.resize(300,30)
		self.comboBox8.currentIndexChanged.connect(self.age_menu)
		
		
		l12 = QtGui.QLabel(self)
		l12.setText("totalfloor: ")
   		l12.move(75,550)
   		self.name_line = QtGui.QLineEdit(self)
		self.name_line.textChanged.connect(self.totalfloor_text)
		self.name_line.move(160,550)
		self.name_line.resize(300,30)		
		
		flo = QtGui.QFormLayout()

		btn = QtGui.QPushButton("Next", self)
		btn.clicked.connect(self.next_page)
		btn.resize(100,50)
		btn.move(50,700)
		
		btn2 = QtGui.QPushButton("Predict", self)
		btn2.clicked.connect(self.predict_page)
		btn2.resize(100,50)
		btn2.move(200,700)
		
		btn1 = QtGui.QPushButton("Quit", self)
		btn1.clicked.connect(self.close_application)
		btn1.resize(100,50)
		btn1.move(350,700)
		self.show()
	
	def balconies_menu(self):
		global balconies
		balconies = self.comboBox1.currentText() 
		    
        					
	def bathroom_menu(self):
		global bathroom
		bathroom = self.comboBox2.currentText()
	
	def opensides_menu(self):
	    global opensides
	    opensides = self.comboBox3.currentText()
	
	def overlooking_menu(self):
	    global overlooking
	    overlooking = self.comboBox4.currentText()
	    
	def ownership_menu(self):
	    global ownership
	    ownership = self.comboBox5.currentText()
	    
	def projectname_menu(self):
	    global projectname
	    projectname = self.comboBox6.currentText()
	
	def roadfaceing_menu(self):
	    global roadfaceing
	    roadfaceing = self.comboBox7.currentText()
	
	def age_menu(self):
	    global age
	    age = self.comboBox8.currentText()
	    
	def totalfloor_text(self):
	    global totalfloor
	    totalfloor = self.name_line.text()
		
	def next_page(self):	
		print("opening next page")
		os.system("python fourth_page.py")
		global balconies,bathroom,opensides,overlooking,ownership,projectname,roadfaceing,age,totalfloor
		print(balconies)
		print(bathroom)
		print(opensides)
		print(overlooking)
		print(ownership)
		print(projectname)
		print(roadfaceing)
		print(age)
		print(totalfloor)
		global output
		output = [str(balconies),str(bathroom),str(opensides),str(overlooking),str(ownership),str(projectname),str(roadfaceing),str(age),str(totalfloor)]
		print(output)
		sys.exit()
	
	def predict_page(self):	
		print("opening next page")
		os.system("python output_page.py")
		global output
		output = [str(balconies),str(bathroom),str(opensides),str(overlooking),str(ownership),str(projectname),str(roadfaceing),str(age),str(totalfloor)]
		print(output)
		sys.exit()
		
	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Warning!!', "Do You Really Want To Close this App ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)		
		if choice == QtGui.QMessageBox.Yes:
			print ("Babye!!!!")
			sys.exit()
		else:
			pass
		 		
   
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
	
#
run()



