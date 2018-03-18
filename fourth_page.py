import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

Lift_Available = Car_Parking = Power_Backup = Security = Childrens_play_area = Club_House = Gymnasium = Swimming_Pool = Sports_Facility = ""
Indoor_Games = Jogging_Track = Maintenance_Staff = Rain_Water_Harvesting = Intercom = Golf_Course = Cafeteria = Staff_Quarter = Multipurpose_Room = ""
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
		l111 = QtGui.QLabel(self)
		l122 = QtGui.QLabel(self)
		l13 = QtGui.QLabel(self)
		l14 = QtGui.QLabel(self)
		l2 = QtGui.QLabel(self)
		l3 = QtGui.QLabel(self)
		
		l111.setText("The Real ")
		l111.move(100,20)
		
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
		
   		l3.setText("Lift Available: ")
   		l3.move(75,150)
		self.comboBox1 = QtGui.QComboBox(self)
		self.comboBox1.addItems(['Yes','No'])
		self.comboBox1.move(200,150)
		self.comboBox1.resize(150,30)
		self.comboBox1.currentIndexChanged.connect(self.Lift_Available_menu)
		
		l4 = QtGui.QLabel(self) 
   		l4.setText("Car Parking: ")
   		l4.move(75,200) 
		self.comboBox2 = QtGui.QComboBox(self)
		self.comboBox2.addItems(['Yes','No'])
		self.comboBox2.move(200,200)
		self.comboBox2.resize(150,30)
		self.comboBox2.currentIndexChanged.connect(self.Car_Parking_menu)
		
		l5 = QtGui.QLabel(self)
		l5.setText("Power Backup:")
   		l5.move(75,250)
		self.comboBox3 = QtGui.QComboBox(self)
		self.comboBox3.addItems(['Yes','No'])
		self.comboBox3.move(200,250)
		self.comboBox3.resize(150,30)
		self.comboBox3.currentIndexChanged.connect(self.Power_Backup_menu)
		
		l6 = QtGui.QLabel(self)
		l6.setText("24 X 7 Security: ")
   		l6.move(75,300)
		self.comboBox4 = QtGui.QComboBox(self)
		self.comboBox4.addItems(['Yes','No'])
		self.comboBox4.move(200,300)
		self.comboBox4.resize(150,30)
		self.comboBox4.currentIndexChanged.connect(self.Security_menu)
		
		l7 = QtGui.QLabel(self)
		l7.setText("Children's play area: ")
   		l7.move(75,350)
		self.comboBox5 = QtGui.QComboBox(self)
		self.comboBox5.addItems(['Yes','No'])
		self.comboBox5.move(200,350)
		self.comboBox5.resize(150,30)
		self.comboBox5.currentIndexChanged.connect(self.Childrens_play_area_menu)
		
		l9 = QtGui.QLabel(self)
		l9.setText("Club House: ")
   		l9.move(75,400)
		self.comboBox6 = QtGui.QComboBox(self)
		self.comboBox6.addItems(['Yes','No'])
		self.comboBox6.move(200,400)
		self.comboBox6.resize(150,30)
		self.comboBox6.currentIndexChanged.connect(self.Club_House_menu)
		
		l10 = QtGui.QLabel(self)
		l10.setText("Gymnasium: ")
   		l10.move(75,450)
		self.comboBox7 = QtGui.QComboBox(self)
		self.comboBox7.addItems(['Yes','No'])
		self.comboBox7.move(200,450)
		self.comboBox7.resize(150,30)
		self.comboBox7.currentIndexChanged.connect(self.Gymnasium_menu)
		
		l11 = QtGui.QLabel(self)
		l11.setText("Swimming Pool: ")
   		l11.move(75,500)
		self.comboBox8 = QtGui.QComboBox(self)
		self.comboBox8.addItems(['Yes','No'])
		self.comboBox8.move(200,500)
		self.comboBox8.resize(150,30)
		self.comboBox8.currentIndexChanged.connect(self.Swimming_Pool_menu)
		
		l12 = QtGui.QLabel(self)
		l12.setText("Sports Facility: ")
   		l12.move(75,550)
		self.comboBox9 = QtGui.QComboBox(self)
		self.comboBox9.addItems(['Yes','No'])
		self.comboBox9.move(200,550)
		self.comboBox9.resize(150,30)
		self.comboBox9.currentIndexChanged.connect(self.Sports_Facility_menu)
		
		l13 = QtGui.QLabel(self)
		l13.setText("Indoor Games: ")
   		l13.move(75,600)
		self.comboBox10 = QtGui.QComboBox(self)
		self.comboBox10.addItems(['Yes','No'])
		self.comboBox10.move(200,600)
		self.comboBox10.resize(150,30)
		self.comboBox10.currentIndexChanged.connect(self.Indoor_Games_menu)
		
		l14 = QtGui.QLabel(self)
		l14.setText("Jogging Track: ")
   		l14.move(75,650)
		self.comboBox11 = QtGui.QComboBox(self)
		self.comboBox11.addItems(['Yes','No'])
		self.comboBox11.move(200,650)
		self.comboBox11.resize(150,30)
		self.comboBox11.currentIndexChanged.connect(self.Jogging_Track_menu)
		
		l15 = QtGui.QLabel(self)
		l15.setText("Maintenance Staff: ")
   		l15.move(75,700)
		self.comboBox12 = QtGui.QComboBox(self)
		self.comboBox12.addItems(['Yes','No'])
		self.comboBox12.move(200,700)
		self.comboBox12.resize(150,30)
		self.comboBox12.currentIndexChanged.connect(self.Maintenance_Staff_menu)
		
		l16 = QtGui.QLabel(self)
		l16.setText("Intercom: ")
   		l16.move(75,750)
		self.comboBox13 = QtGui.QComboBox(self)
		self.comboBox13.addItems(['Yes','No'])
		self.comboBox13.move(200,750)
		self.comboBox13.resize(150,30)
		self.comboBox13.currentIndexChanged.connect(self.Intercom_menu)
		
		l17 = QtGui.QLabel(self)
		l17.setText("Golf Course: ")
   		l17.move(75,800)
		self.comboBox14 = QtGui.QComboBox(self)
		self.comboBox14.addItems(['Yes','No'])
		self.comboBox14.move(200,800)
		self.comboBox14.resize(150,30)
		self.comboBox14.currentIndexChanged.connect(self.Golf_Course_menu)
		
		l18 = QtGui.QLabel(self)
		l18.setText("Cafeteria: ")
   		l18.move(400,150)
		self.comboBox15 = QtGui.QComboBox(self)
		self.comboBox15.addItems(['Yes','No'])
		self.comboBox15.move(550,150)
		self.comboBox15.resize(150,30)
		self.comboBox15.currentIndexChanged.connect(self.Cafeteria_menu)
		
		l19 = QtGui.QLabel(self)
		l19.setText("Rain Water Harvesting: ")
   		l19.move(400,200)
		self.comboBox16 = QtGui.QComboBox(self)
		self.comboBox16.addItems(['Yes','No'])
		self.comboBox16.move(550,200)
		self.comboBox16.resize(150,30)
		self.comboBox16.currentIndexChanged.connect(self.Rain_Water_Harvesting_menu)
		
		l20 = QtGui.QLabel(self)
		l20.setText("Staff Quarter: ")
   		l20.move(400,250)
		self.comboBox17 = QtGui.QComboBox(self)
		self.comboBox17.addItems(['Yes','No'])
		self.comboBox17.move(550,250)
		self.comboBox17.resize(150,30)
		self.comboBox17.currentIndexChanged.connect(self.Staff_Quarter_menu)
		
		l21 = QtGui.QLabel(self)
		l21.setText("Multipurpose Room: ")
   		l21.move(400,300)
		self.comboBox18 = QtGui.QComboBox(self)
		self.comboBox18.addItems(['Yes','No'])
		self.comboBox18.move(550,300)
		self.comboBox18.resize(150,30)
		self.comboBox18.currentIndexChanged.connect(self.Multipurpose_Room_menu)
        
        l22 = QtGui.QLabel(self)
        l22.setText("Landscaped Gardens: ")
        l22.move(400,350)
        self.comboBox19 = QtGui.QComboBox(self)
        self.comboBox19.addItems(['Yes','No'])
        self.comboBox19.move(550,350)
        self.comboBox19.resize(150,30)
        self.comboBox19.currentIndexChanged.connect(self.Landscaped_Gardens_menu)	

        l23 = QtGui.QLabel(self)
        l23.setText("Shopping Mall: ")
        l23.move(400,400)
        self.comboBox20 = QtGui.QComboBox(self)
        self.comboBox20.addItems(['Yes','No'])
        self.comboBox20.move(550,400)
        self.comboBox20.resize(150,30)
        self.comboBox20.currentIndexChanged.connect(self.Shopping_Mall_menu)

        l24 = QtGui.QLabel(self)
        l24.setText("School: ")
        l24.move(400,450)
        self.comboBox21 = QtGui.QComboBox(self)
        self.comboBox21.addItems(['Yes','No'])
        self.comboBox21.move(550,450)
        self.comboBox21.resize(150,30)
        self.comboBox21.currentIndexChanged.connect(self.School_menu)

        l25 = QtGui.QLabel(self)
        l25.setText("Hospital: ")
        l25.move(400,500)
        self.comboBox22 = QtGui.QComboBox(self)
        self.comboBox22.addItems(['Yes','No'])
        self.comboBox22.move(550,500)
        self.comboBox22.resize(150,30)
        self.comboBox22.currentIndexChanged.connect(self.Hospital_menu)

        l26 = QtGui.QLabel(self)
        l26.setText("ATM: ")
        l26.move(400,550)
        self.comboBox23 = QtGui.QComboBox(self)
        self.comboBox23.addItems(['Yes','No'])
        self.comboBox23.move(550,550)
        self.comboBox23.resize(150,30)
        self.comboBox23.currentIndexChanged.connect(self.ATM_menu)

        l27 = QtGui.QLabel(self)
        l27.setText("AC: ")
        l27.move(400,600)
        self.comboBox24 = QtGui.QComboBox(self)
        self.comboBox24.addItems(['Yes','No'])
        self.comboBox24.move(550,600)
        self.comboBox24.resize(150,30)
        self.comboBox24.currentIndexChanged.connect(self.AC_menu)

        l28 = QtGui.QLabel(self)
        l28.setText("Wardrobe: ")
        l28.move(400,650)
        self.comboBox25 = QtGui.QComboBox(self)
        self.comboBox25.addItems(['Yes','No'])
        self.comboBox25.move(550,650)
        self.comboBox25.resize(150,30)
        self.comboBox25.currentIndexChanged.connect(self.Wardrobe_menu)

        l29 = QtGui.QLabel(self)
        l29.setText("TV: ")
        l29.move(400,700)
        self.comboBox26 = QtGui.QComboBox(self)
        self.comboBox26.addItems(['Yes','No'])
        self.comboBox26.move(550,700)
        self.comboBox26.resize(150,30)
        self.comboBox26.currentIndexChanged.connect(self.TV_menu)

        l30 = QtGui.QLabel(self)
        l30.setText("Refrigerator: ")
        l30.move(400,750)
        self.comboBox27 = QtGui.QComboBox(self)
        self.comboBox27.addItems(['Yes','No'])
        self.comboBox27.move(550,750)
        self.comboBox27.resize(150,30)
        self.comboBox27.currentIndexChanged.connect(self.Refrigerator_menu)

        l31 = QtGui.QLabel(self)
        l31.setText(": ")
        l31.move(400,800)
        self.comboBox28 = QtGui.QComboBox(self)
        self.comboBox28.addItems(['Yes','No'])
        self.comboBox28.move(550,800)
        self.comboBox28.resize(150,30)
        self.comboBox28.currentIndexChanged.connect(self._menu)

        l30 = QtGui.QLabel(self)
        l30.setText("Refrigerator: ")
        l30.move(400,750)
        self.comboBox27 = QtGui.QComboBox(self)
        self.comboBox27.addItems(['Yes','No'])
        self.comboBox27.move(550,750)
        self.comboBox27.resize(150,30)
        self.comboBox27.currentIndexChanged.connect(self.Refrigerator_menu)

        l30 = QtGui.QLabel(self)
        l30.setText("Refrigerator: ")
        l30.move(400,750)
        self.comboBox28 = QtGui.QComboBox(self)
        self.comboBox28.addItems(['Yes','No'])
        self.comboBox28.move(550,750)
        self.comboBox28.resize(150,30)
        self.comboBox28.currentIndexChanged.connect(self.Refrigerator_menu)

        l31 = QtGui.QLabel(self)
        l31.setText("Sofa: ")
        l31.move(400,800)
        self.comboBox29 = QtGui.QComboBox(self)
        self.comboBox29.addItems(['Yes','No'])
        self.comboBox29.move(550,800)
        self.comboBox29.resize(150,30)
        self.comboBox29.currentIndexChanged.connect(self.Sofa_menu)

        l32 = QtGui.QLabel(self)
        l32.setText("Washing Machine: ")
        l32.move(800,150)
        self.comboBox30 = QtGui.QComboBox(self)
        self.comboBox30.addItems(['Yes','No'])
        self.comboBox30.move(950,150)
        self.comboBox30.resize(150,30)
        self.comboBox30.currentIndexChanged.connect(self.Washing_Machine_menu)

        l33 = QtGui.QLabel(self)
        l33.setText("Wifi: ")
        l33.move(800,200)
        self.comboBox31 = QtGui.QComboBox(self)
        self.comboBox31.addItems(['Yes','No'])
        self.comboBox31.move(950,200)
        self.comboBox31.resize(150,30)
        self.comboBox31.currentIndexChanged.connect(self.Wifi_menu)

        l34 = QtGui.QLabel(self)
        l34.setText("Microwave: ")
        l34.move(800,250)
        self.comboBox32 = QtGui.QComboBox(self)
        self.comboBox32.addItems(['Yes','No'])
        self.comboBox32.move(950,250)
        self.comboBox32.resize(150,30)
        self.comboBox32.currentIndexChanged.connect(self.Microwave_menu)
		
        flo = QtGui.QFormLayout()

        btn = QtGui.QPushButton("Next", self)
        btn.clicked.connect(self.next_page)
        btn.resize(100,50)
        btn.move(50,850)

        btn2 = QtGui.QPushButton("Predict", self)
        btn2.clicked.connect(self.predict_page)
        btn2.resize(100,50)
        btn2.move(200,850)

        btn1 = QtGui.QPushButton("Quit", self)
        btn1.clicked.connect(self.close_application)
        btn1.resize(100,50)
        btn1.move(350,850)
        self.show()
	
    def Lift_Available_menu(self):
        global Lift_Available
        Lift_Available = self.comboBox1.currentText() 
	        
        					
    def Car_Parking_menu(self):
	    global Car_Parking
	    Car_Parking = self.comboBox2.currentText()

    def Power_Backup_menu(self):
        global Power_Backup
        Power_Backup = self.comboBox3.currentText()

    def Security_menu(self):
        global Security
        Security = self.comboBox4.currentText()
        
    def Childrens_play_area_menu(self):
        global Childrens_play_area
        Childrens_play_area = self.comboBox5.currentText()
        
    def Club_House_menu(self):
        global Club_House
        Club_House = self.comboBox6.currentText()

    def Gymnasium_menu(self):
        global Gymnasium
        Gymnasium = self.comboBox7.currentText()

    def Swimming_Pool_menu(self):
        global Swimming_Pool
        Swimming_Pool = self.comboBox8.currentText()

    def Sports_Facility_menu(self):
        global Sports_Facility
        Sports_Facility = self.comboBox9.currentText()

    def Indoor_Games_menu(self):
        global Indoor_Games
        Indoor_Games = self.comboBox10.currentText()
         
    def Jogging_Track_menu(self):
        global Jogging_Track 
        Jogging_Track = self.comboBox11.currentText()
        
    def Maintenance_Staff_menu(self):
        global Maintenance_Staff
        Maintenance_Staff = self.comboBox12.currentText()
	
    def Intercom_menu(self):
        global Intercom
        Intercom = self.comboBox13.currentText()

    def Golf_Course_menu(self):
        global Golf_Course
        Golf_Course = self.comboBox14.currentText()

    def Cafeteria_menu(self):
        global Cafeteria
        Cafeteria = self.comboBox15.currentText()

    def Rain_Water_Harvesting_menu(self):
        global Rain_Water_Harvesting
        Rain_Water_Harvesting = self.comboBox16.currentText()

    def Staff_Quarter_menu(self):
        global Staff_Quarter
        Staff_Quarter = self.comboBox17.currentText()

    def Multipurpose_Room_menu(self):
        global Multipurpose_Room
        Multipurpose_Room = self.comboBox18.currentText()
        
    def Landscaped_Gardens_menu(self):
        global Landscaped_Gardens
        Landscaped_Gardens = self.comboBox19.currentText()

    def Shopping_Mall_menu(self):
        global Shopping_Mall
        Shopping_Mall = self.comboBox20.currentText()

    def School_menu(self):
        global School
        School = self.comboBox21.currentText()

    def Hospital_menu(self):
        global Hospital
        Hospital = self.comboBox22.currentText()

    def ATM_menu(self):
        global ATM
        ATM = self.comboBox23.currentText()

    def AC_menu(self):
        global AC
        AC = self.comboBox24.currentText()

    def Wardrobe_menu(self):
        global Wardrobe
        Wardrobe = self.comboBox25.currentText()    

    def TV_menu(self):
        global TV
        TV = self.comboBox26.currentText()    
            
    def Refrigerator_menu(self):
        global Refrigerator
        Refrigerator = self.comboBox27.currentText()	

    def Refrigerator_menu(self):
        global Refrigerator
        Refrigerator = self.comboBox28.currentText()

    def Sofa_menu(self):
        global Sofa
        sofa = self.comboBox29.currentText()
        
    def Washing_Machine_menu(self):
        global Washing_Machine
        Washing_Machine = self.comboBox30.currentText()
        
    def Wifi_menu(self):
        global wifi
        wifi = self.comboBox31.currentText()
    
    def Microwave(self):
        global Microwave
        Microwave = self.comboBox32.currentText()

    def next_page(self):	
	    print("opening next page")
	    global Lift_Available,Car_Parking,Power_Backup,Security,Childrens_play_area,Club_House,Gymnasium,Swimming_Pool,Sports_Facility,Indoor_Games
	    global Golf_Course, Cafeteria, Rain_Water_Harvesting, Staff_Quarter, Multipurpose_Room
	    print(Lift_Available)
	    print(Car_Parking)
	    print(Power_Backup)
	    print(Security)
	    print(Childrens_play_area)
	    print(Club_House)
	    print(Gymnasium)
	    print(Swimming_Pool)
	    print(Sports_Facility)
	    print(Indoor_Games)
	    print(Jogging_Track)
	    print(Maintenance_Staff)
	    print(Intercom)
	    print(Golf_Course)
	    print(Cafeteria)
	    print(Rain_Water_Harvesting)
	    print(Staff_Quarter)
	    print(Multipurpose_Room)
	    print(Shopping_Mall)
	    print(School)
	    print(Hospital)
	    print(AC)
	    print(Wardrobe)
	    print(TV)
	    print(Refrigerator)
	    print(Sofa)
	    print(Washing_Machine)
	    print(Wifi)
	    print(Microwave)
	    global output
	    output = [str(Lift_Available),str(Car_Parking),str(Power_Backup),str(Security),str(Childrens_play_area),str(Club_House),str(Gymnasium),str(Swimming_Pool),str(Sports_Facility),str(Indoor_Games),str(Jogging_Track),str(Maintenance_Staff),str(Intercom),str(Golf_Course),str(Cafeteria),str(Rain_Water_Harvesting),str(Staff_Quarter),str(Multipurpose_Room),str(Shopping_Mall),str(school),str(Hospital),str(AC),str(Wardrobe),str(TV),str(Refrigerator),str(Sofa),str(Washing_Machine),str(Wifi),str(Microwave)]
	    print(output)
	    sys.exit()

    def predict_page(self):	
	    print("opening next page")
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



