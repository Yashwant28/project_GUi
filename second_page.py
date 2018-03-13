import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

area = bhk = facing = carpetarea = pricepersquare = Vaastu_Compliant = neworold = locality = floor = additionalrooms = possesiondate = status = ""
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
		l12 = QtGui.QLabel(self)
		l13 = QtGui.QLabel(self)
		l14 = QtGui.QLabel(self)
		l2 = QtGui.QLabel(self)
		l3 = QtGui.QLabel(self)
		
		l11.setText("The Real ")
		l11.move(100,20)
		
		l12.setText("Estate Price ")
		l12.move(165,20)
		
		l13.setText("Prediction ")
		l13.move(250,20)
		
		l14.setText("System.!!")
		l14.move(325,20)
		
		l1.setText("Select")
		l1.move(100,40)
		
		ll1.setText("Features:")
		ll1.move(145,40)
		
   		l2.setText("Area: ")
   		l2.move(75,100)
   		self.name_line = QtGui.QLineEdit(self)
		self.name_line.textChanged.connect(self.Area_text)
		self.name_line.move(160,100)
		self.name_line.resize(300,30)
		l21 = QtGui.QLabel(self)
		l21.setText("in sq.ft.")
   		l21.move(350,100)
		
		
   		l3.setText("No of BHK: ")
   		l3.move(75,150)
		self.comboBox1 = QtGui.QComboBox(self)
		self.comboBox1.addItems([' Residential Plot ', '0 BHK Villa ', '1 BHK Apartment ', '1 BHK Independent Floor ', '1 BHK Independent House ', '1 BHK Villa ', '1 BHK studio apartment ', '1 RK Apartment ', '1 RK Independent Floor ', '1 RK Independent House ', '2 BHK Apartment ', '2 BHK Independent Floor ', '2 BHK Independent House ', '2 BHK Villa ', '2 BHK penthouse ', '3 BHK Apartment ', '3 BHK Independent Floor ', '3 BHK Independent House ', '3 BHK Other Residential ', '3 BHK Villa ', '3 BHK penthouse ', '4 BHK Apartment ', '4 BHK Independent Floor ', '4 BHK Independent House ', '4 BHK Other Residential ', '4 BHK Villa ', '4 BHK penthouse ', '5 BHK Apartment ', '5 BHK Independent Floor ', '5 BHK Independent House ', '5 BHK Villa ', '5 BHK penthouse ', '6 BHK Apartment ', '6 BHK Independent Floor ', '6 BHK Villa ', '6 BHK penthouse ', '7 BHK Apartment ', '7 BHK Independent House ', '8 BHK Villa '])
		self.comboBox1.move(160,150)
		self.comboBox1.resize(300,30)
		self.comboBox1.currentIndexChanged.connect(self.bhk)
		
		l4 = QtGui.QLabel(self)
		l4.setText("Facing :")
   		l4.move(75,200)
		self.comboBox2 = QtGui.QComboBox(self)
		self.comboBox2.addItems(['East', 'North', 'NorthEast', 'NorthWest', 'South', 'SouthEast', 'SouthWest', 'West'])
		self.comboBox2.move(160,200)
		self.comboBox2.resize(300,30)
		self.comboBox2.currentIndexChanged.connect(self.facing)
		
		l5 = QtGui.QLabel(self)
		l5.setText("Carpet area:")
   		l5.move(75,250)
   		self.name_line1 = QtGui.QLineEdit(self)
		self.name_line1.textChanged.connect(self.carpetarea_text)
		self.name_line1.move(160,250)
		self.name_line1.resize(300,30)
		l51 = QtGui.QLabel(self)
		l51.setText("in sq.ft.")
   		l51.move(350,250)
   		
   		l6 = QtGui.QLabel(self)
		l6.setText("price/square:")
   		l6.move(75,300)
   		self.name_line2 = QtGui.QLineEdit(self)
		self.name_line2.textChanged.connect(self.pricepersquare_text)
		self.name_line2.move(160,300)
		self.name_line2.resize(300,30)
		l61 = QtGui.QLabel(self)
		l61.setText("in sq.ft.")
   		l61.move(350,300)
		
		l7 = QtGui.QLabel(self)
		l7.setText("Vaastu : ")
   		l7.move(75,350)
		self.comboBox3 = QtGui.QComboBox(self)
		self.comboBox3.addItems(['yes','no'])
		self.comboBox3.move(160,350)
		self.comboBox3.resize(300,30)
		self.comboBox3.currentIndexChanged.connect(self.Vaastu_Compliant_menu)
		
		l8 = QtGui.QLabel(self)
		l8.setText("New/Old : ")
   		l8.move(75,400)
		self.comboBox4 = QtGui.QComboBox(self)
		self.comboBox4.addItems(['New','Old'])
		self.comboBox4.move(160,400)
		self.comboBox4.resize(300,30)
		self.comboBox4.currentIndexChanged.connect(self.new_old)
		
		l9 = QtGui.QLabel(self)
		l9.setText("locality : ")
   		l9.move(75,450)
		self.comboBox5 = QtGui.QComboBox(self)
		self.comboBox5.addItems(['Aditya Birla Hospital Marg', 'Airport Road', 'Ajmera colony', 'Akurdi', 'Alandi', 'Alandi Road', 'Amanora Park Town', 'Ambe Gaon', 'Ambedkar Nagar', 'Ambegaon Bk', 'Ambegaon Budruk', 'Ambegaon Khurd', 'Ambegaon Pathar', 'Ambegaon Road', 'Anand Nagar', 'Anand Park', 'Ashok Nagar', 'Askarwadi', 'Aundh', 'Aundh Annexe', 'Aundh Baner Link Road', 'Aundh Gaon', 'Aundh Road', 'BT Kawade Road', 'BT Kawde', 'Badhan Nagar', 'Baif Road', 'Bakhori', 'Bakori Road', 'Balaji Nagar', 'Balewadi', 'Balewadi High Street', 'Balewadi Road', 'Baner', 'Baner Balewadi road', 'Baner Gaon', 'Baner Highway Side Road', 'Baner Pashan Link Road', 'Baner Road', 'Baramati', 'Bavdhan', 'Bavdhan Khurd', 'Bebadohal', 'Benkar Nagar', 'Bhairav Nagar', 'Bhandarkar Road', 'Bharati Vidyapeeth', 'Bhatewara Nagar Chinchwad', 'Bhau Patil Road', 'Bhavani Peth', 'Bhawani Peth', 'Bhor', 'Bhosari', 'Bhosle Nagar', 'Bhoslenagar', 'Bhugaon', 'Bhujbal Vasti', 'Bhukum', 'Bhumkar Bridge', 'Bhumkar Nagar', 'Bhusari colony left', 'Bhusari colony right', 'Bibwewadi', 'Bibwewadi Kondhwa Road', 'Bijali Nagar PimpriChinchwad', 'Boat Club Road', 'Bopkhel', 'Bopodi', 'Bund Garden', 'Bund Garden Road', 'Burhani Colony Road', 'Camp', 'Chakan', 'Chakan Talegaon Road', 'Chandkhed', 'Charholi Budruk', 'Chikali Road', 'Chikhali', 'Chikhali Pimpri Chinchwad New Town Development Authority', 'Chikhali Road', 'Chincholi Dehu Road', 'Chinchwad', 'Chinchwad Gaon Road', 'Chinchwad Station Road', 'Chintamani nagar', 'DSK Road', 'DSK Vishwa Road', 'DY Patil Road', 'Dange Chowk Road', 'Dapodi', 'Dattanagar', 'Dattavadi', 'Daund', 'Deccan Gymkhana', 'Deep Bunglow chawk', 'Dehu', 'Dehu Road', 'Devachi Urli', 'Dhanakwadi', 'Dhankawadi Road', 'Dhanori', 'Dhanori Road', 'DhanoriLohegaon Road', 'Dhanukar Colony', 'Dhayari', 'Dhayari Ganesh Nagar', 'Dhayari Phata', 'Dhole Patil Road', 'Dighi', 'Dombewadi Road', 'EON Free Zone', 'Erandwane', 'Fatima Nagar', 'Fergusson College Road', 'Gadital', 'Gahunje', 'Gajanan Nagar', 'Ganesh Nagar', 'Ganeshkhind Road', 'Gera Emerald City Road', 'Ghodegaon', 'Ghole Road', 'Ghorpadi', 'Giridhar Nagar', 'Gokul Nagar', 'Gujarat Colony Road', 'Gulab Nagar Pune', 'Gultekdi', 'Guru Nanak Nagar', 'Guruwar Peth', 'Hadapsar', 'Hadapsar Fursungi Road', 'Hadapsar Gaon', 'Hadapsar Handewadi road', 'Hadapsar Saswad Jejuri Road', 'Hadapsar Tukai Nagar', 'Handewadi', 'Handewadi Road', 'Hanuman Nagar', 'Happy Colony Lane', 'Hinjawadi Phase 3', 'Hinjewadi', 'Hinjewadi Marunji Road', 'Hinjewadi Phase 1', 'Hinjewadi Phase 2', 'Hinjewadi Phase 2 Road', 'ITI road', 'Indira Nagar', 'Indrayani Nagar Sector 2', 'Ingawale Nagar', 'JM Road', 'Jambhul', 'Jambhulwadi', 'Jambhulwadi Road', 'Jejuri', 'Jejuri Saswad Hadapsar Road', 'Kad Nagar', 'Kalas', 'Kale Padal', 'Kalewadi', 'Kalewadi Main', 'Kalwad Area', 'Kalyani Nagar', 'Kalyani Nagar Annexe', 'Kambre Kd Deshmukhwadi Road', 'Kamgar Nagar PimpriChinchwad', 'Kamshet', 'Kanhe', 'Kanhephata', 'Karjat Kashele Khandas Road', 'Karve Nagar', 'Karve Road', 'Kasar Amboli', 'Kasarsai', 'Kasarwadi', 'Kaspate Vasti', 'Katarkhadak', 'Katraj', 'Kedagaon', 'Kedari Nagar', 'Kedgaon Station Road', 'Kendriya Vihar Road PimpriChinchwad', 'Keshav Nagar', 'Keshav Nagar Road', 'Khandala', 'Khandve Nagar', 'Kharabwadi', 'Kharadi', 'Khed Shivapur', 'Kirkatwadi', 'Kirti Nagar', 'Kiwale', 'Kolhewadi', 'Kolwadi', 'Kondhawe Dhawade', 'Kondhwa', 'Kondhwa Bk', 'Kondhwa Budruk', 'Kondhwa Khurd', 'Kondwa khurd road', 'Koregaon Bhima', 'Koregaon Park', 'Koregaon Park Annexe', 'Kothrud', 'Kothrud Bus Stand Road', 'Kothrud Depot Road', 'Krishnanagar Road', 'Kudale Baug', 'Kumar aangan society opposite shah hospital Yerwada Pune 411006', 'Kunal Icon Road', 'Kurkum MIDC', 'Lavasa', 'Law College Rd', 'Law collage Road', 'Laxman Nagar', 'Laxmi Nagar', 'Lohegaon', 'Lohegaon Road', 'Lokmanya Nagar', 'Lonavala Road', 'Loni', 'Loni Kalbhor', 'Loni Raiway Station Road', 'Lonikand', 'Lulla Nagar', 'MIT College Road', 'Madhav Nagar', 'Magarpatta', 'Magarpatta City', 'Magarpatta Road', 'Mahabaleshwar', 'Mahadev Nagar', 'Mahalunge', 'Mahatma Society', 'Malwadi', 'Malwadi Hadapsar', 'Mamurdi', 'Manchar', 'Mangal Nagar', 'Mangaldas Road', 'Mangaon', 'Mangdewadi', 'Manik Bagh', 'Manik Baug', 'Manjari', 'Manjari Budruk', 'Manjari Khurd', 'Manjri Village Road', 'Manohar Nagar', 'Market yard', 'Marunji', 'Marunji Road', 'Maval', 'Mayur Colony', 'Mayureshwar', 'Medankarwadi', 'Meeta Nagar', 'Model Colony', 'Mohamadwadi', 'Mohammed wadi', 'Mohan Nagar', 'Moraya Ganapati Mandir Road', 'Morewadi', 'Moshi', 'Moshi Pradhikaran PimpriChinchwad', 'Mukund Nagar', 'Mulshi', 'MulshiPaud Road', 'Mumbai Pune Highway', 'Mundhwa', 'Mundhwa Manjari Road', 'NDA Pashan Road', 'NIBM', 'NIBM Annex Mohammadwadi', 'NIBM Annexe', 'NIBM Junction', 'NIBM Post Office Road', 'NIBM Road', 'Nagpur Chal', 'Naigaon Peth Road', 'Nana Peth', 'Nanded', 'Nanded City Sinhgad Road', 'Nanded Phata', 'Nandel Fata Pune', 'Narhe', 'Narhe Gaon', 'Narhe Road', 'Nasrapur', 'National Highway 48', 'Navi Peth', 'Nehru Nagar', 'Nere', 'New DP Road', 'New Sangavi', 'New Sanghvi', 'Nigdi', 'Nigdi Sector 21', 'Nighoje', 'Nilanjali Society', 'Nilgiri Lane', 'Old Mumbai Pune Highway', 'Old Mumbai Road', 'Old Sanghvi', 'Omkar Colony Road', 'Padmavati', 'Pan Card Road', 'Pancard Club Road', 'Panchgani Wai Road', 'Panshet', 'Panshet Ghol Road', 'Papde Wasti', 'Parandwadi Road', 'Pargaon', 'Parihar Chowk', 'Parkhe Vasti', 'Parvati', 'Parvati Darshan', 'Parvati Gaon', 'Pashan', 'Pashan Sus Road', 'Pathare Vasti Road', 'Patwardhan Baug Road', 'Paud Rd', 'Perugate', 'Phaltan', 'Phase 3 Pune', 'Phursungi', 'Pimple Gurav', 'Pimple Nilakh', 'Pimple Nilakh Road', 'Pimple Saudagar', 'Pimpri', 'Pimpri Chinchwad', 'Pimpri Kalewadi Link Road', 'Pingale Wasti', 'Pirangut', 'Pisoli', 'Porwal Road', 'Prabhat Road', 'Pradhikaran Nigdi', 'Pragati Nagar', 'Pratik Nagar', 'Punawale', 'Pune Bengaluru Highway', 'Pune Link Road', 'Pune Mumbai Expressway', 'Pune Mumbai Highway', 'Pune Mumbai Road', 'Pune Nagar Road', 'Pune Pandharpur Road', 'Pune Satara Road', 'Pune Solapur Road', 'Pune Station', 'PuneSatara Road', 'PuneSolapur Highway', 'Purnanagar', 'Rahatani', 'Rahatani Rajgad Colony', 'Raigad District', 'Raikar Mala Road', 'Raje Shivaji Nagar PimpriChinchwad', 'Ram Nagar', 'Ranjangaon', 'Rasikwadi', 'Rasta Peth', 'Ravet', 'Rihe', 'SHIVAJI HSG SOC', 'Sadashiv Peth', 'Sahakar Nagar', 'Sahakar Nagar II', 'Sakore Nagar', 'Salisbury Park', 'Salunke Vihar', 'Samarth Colony', 'Sanaswadi', 'Sanewadi', 'Sangamvadi', 'Sanjay Park', 'Sant Nagar Lohegoan', 'Sasane Nagar', 'Saswad', 'Saswad Road', 'Satar Nagar', 'Satara road', 'Satavwadi', 'Sathe Wasti', 'Sector No1 Bhosari', 'Senapati Bapat Road', 'Shahunagar', 'Shankar Kalat Nagar', 'Shankar Sheth Road', 'Shankarseth Road', 'Shastri Nagar', 'Shedge Vasti PimpriChinchwad', 'Shewalewadi', 'Shikrapur', 'Shirur', 'Shirwal', 'Shiv Colony', 'Shivaji Nagar', 'Shivane', 'Shivapur', 'Sholapur Road', 'Shukrawar Peth', 'Siddharth nagar', 'Sinhagad Fort', 'Sinhgad Road', 'Somatane Phata', 'Someshwarwadi', 'Somwar Peth', 'Sopan Baug', 'Sukhsagar Nagar', 'Sun City', 'Sun City Road', 'Sunita Nagar', 'Sus', 'Sus Gaon', 'Sus Road', 'Swaraj Nagari', 'Swargate', 'Tadiwala Road', 'Talegaon', 'Talegaon Dabhade', 'Talegaon Dhamdhere', 'Talwade', 'Tanaji Nagar', 'Tathawade', 'Thergaon', 'Theur', 'Thite Nagar', 'Tingre Nagar', 'Trimurti Vihar', 'Tukai Darshan', 'Tukaram Nagar', 'Tulaja Bhawani Nagar', 'Tungarli', 'Ubale Nagar', 'Uday Baug', 'Undri', 'Undri Hadapsar Road', 'Upper Indira Nagar', 'Urbangram Kirkatwadi Road', 'Uruli Devachi', 'Uruli Kanchan', 'VIT College Road', 'Vadgaon Budruk', 'Vadgaon Maval', 'Vadgaon Sheri', 'Varale', 'Varanasi Society Internal Road', 'Vastu Udyog Road', 'Veerbhadra Nagar', 'Vighnaharta Nagar', 'Vijay Nagar', 'Viman Nagar', 'Vishal Nagar', 'Vishrantwadi', 'Wadagaon Road', 'Wadgaon Budruk', 'Wadgaon Sheri', 'Wadgaon Shinde Road', 'Wadki', 'Wagholi', 'Wakad', 'Wakad Chowk Road', 'Wakad Hinjewadi Road', 'Wakad road', 'Wakadkar Wasti', 'Walha Railway StationSukalwadi Road', 'Walvekar Nagar', 'Wanowrie', 'Wanwadi', 'Warje', 'Warje Malwadi', 'Yashwant nagar', 'Yavat', 'Yerawada', 'Yewalewadi', 'bavdhan patil nagar', 'bhekarai nagar', 'bhusari colony', 'bibvewadi', 'charholi Khurd', 'hingne Khurd', 'hinjawadi', 'karvenagar', 'katraj kondhwa road', 'kesnand', 'khamboli', 'khese park', 'konark avenue 9', 'north hadapsar', 'panchwati', 'paud', 'pimprigaon', 'pune saswad road', 'shahu nagar', 'sinhagad road', 'wadebolhai', 'wanwari'])
		self.comboBox5.move(160,450)
		self.comboBox5.resize(300,30)
		self.comboBox5.currentIndexChanged.connect(self.locality_menu)
		
		l10 = QtGui.QLabel(self)
		l10.setText("Floor:")
   		l10.move(75,500)
   		self.name_line3 = QtGui.QLineEdit(self)
		self.name_line3.textChanged.connect(self.floor_text)
		self.name_line3.move(160,500)
		self.name_line3.resize(300,30)
		
		l11 = QtGui.QLabel(self)
		l11.setText("additionalrooms: ")
   		l11.move(75,550)
		self.comboBox6 = QtGui.QComboBox(self)
		self.comboBox6.addItems(['1 rooms( pooja room )', '1 rooms( servant room )', '1 rooms( study room )', '2 rooms( servant room, pooja room )', '2 rooms( study room, pooja room )', '2 rooms( study room, servant room )', '3 rooms( study room, servant room, pooja room )'])
		self.comboBox6.move(160,550)
		self.comboBox6.resize(300,30)
		self.comboBox6.currentIndexChanged.connect(self.additionalrooms_menu)
		
		l12 = QtGui.QLabel(self)
		l12.setText("possesiondate: ")
   		l12.move(75,600)
		self.comboBox7 = QtGui.QComboBox(self)
		self.comboBox7.addItems(['Apr 2018', 'Apr 2019', 'Aug 2018', 'Aug 2019', 'Aug 2020', 'Aug 2021', 'Dec 2018', 'Dec 2019', 'Dec 2020', 'Dec 2021', 'Dec 2022', 'Dec 2023', 'Dec 2025', 'Feb 2018', 'Feb 2019', 'Feb 2020', 'Feb 2021', 'Feb 2022', 'Jan 2018', 'Jan 2019', 'Jan 2020', 'Jul 2018', 'Jul 2019', 'Jul 2020', 'Jul 2021', 'Jun 2018', 'Jun 2019', 'Jun 2020', 'Jun 2021', 'Mar 2018', 'Mar 2019', 'Mar 2020', 'Mar 2021', 'Mar 2022', 'May 2018', 'May 2019', 'May 2020', 'May 2021', 'Nov 2018', 'Nov 2019', 'Nov 2020', 'Nov 2021', 'Oct 2018', 'Oct 2019', 'Oct 2021', 'Oct 2022', 'Sep 2018', 'Sep 2019', 'Sep 2020', 'Sep 2021', 'Sep 2022'])
		self.comboBox7.move(160,600)
		self.comboBox7.resize(300,30)
		self.comboBox7.currentIndexChanged.connect(self.month_menu)
		
		l13 = QtGui.QLabel(self)
		l13.setText("status : ")
   		l13.move(75,650)
		self.comboBox8 = QtGui.QComboBox(self)
		self.comboBox8.addItems(['Furnished', 'Ready to move', 'Ready to move,Furnished', 'Ready to move,Semi-Furnished', 'Ready to move,Unfurnished', 'Semi-Furnished', 'Under Construction', 'Under Construction,Furnished', 'Under Construction,Semi-Furnished', 'Under Construction,Unfurnished', 'Unfurnished'])
		self.comboBox8.move(160,650)
		self.comboBox8.resize(300,30)
		self.comboBox8.currentIndexChanged.connect(self.status_menu)
		
		
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
	
	def Area_text(self):
		global area
		area = self.name_line.text() 
		    
        					
	def bhk(self):
		global bhk
		bhk = self.comboBox1.currentText()
	
	def facing(self):
	    global facing
	    facing = self.comboBox2.currentText()
	
	def carpetarea_text(self):
	    global carpetarea
	    carpetarea = self.name_line1.text()
	
	def pricepersquare_text(self):
	    global pricepersquare
	    pricepersquare = self.name_line2.text()
	
	def Vaastu_Compliant_menu(self):
	    global Vaastu_Compliant
	    Vaastu_Compliant = self.comboBox3.currentText()
	    
	def new_old(self):
	    global neworold
	    neworold = self.comboBox4.currentText()
	    
	def locality_menu(self):
	    global locality
	    locality = self.comboBox5.currentText()
	
	def floor_text(self):
	    global floor
	    floor = self.name_line3.text()
	    
	def month_menu(self):
	    global possesiondate
	    possesiondate = self.comboBox7.currentText()
	 
	
	def additionalrooms_menu(self):
	    global additionalrooms
	    additionalrooms = self.comboBox6.currentText()
	
	def status_menu(self):
	    global status
	    status = self.comboBox8.currentText()
		
	def next_page(self):	
		print("opening next page")
		os.system("python third_page.py")
		global area,bhk,facing,carpetarea,pricepersquare,Vaastu_Compliant,neworold,locality,floor,additionalrooms,possesiondate,status
		print(area)
		print(bhk)
		print(facing)
		print(carpetarea)
		print(pricepersquare)
		print(Vaastu_Compliant)
		print(neworold)
		print(locality)
		print(floor)
		print(additionalrooms)
		print(possesiondate)
		print(status)
		global output
		output = [str(area),str(bhk),str(facing),str(carpetarea),str(pricepersquare),str(Vaastu_Compliant),str(neworold),str(locality),str(floor),str(additionalrooms),str(possesiondate),str(status)]
		print(output)
		sys.exit()
	
	def predict_page(self):	
		print("opening next page")
		os.system("python third_page.py")
		global area,bhk,facing,carpetarea,pricepersquare,Vaastu_Compliant,neworold,locality,floor,additionalrooms,possesiondate,status
		print(area)
		print(bhk)
		print(facing)
		print(carpetarea)
		print(pricepersquare)
		print(Vaastu_Compliant)
		print(neworold)
		print(locality)
		print(floor)
		print(additionalrooms)
		print(possesiondate)
		print(status)
		global output
		output = [str(area),str(bhk),str(facing),str(carpetarea),str(pricepersquare),str(Vaastu_Compliant),str(neworold),str(locality),str(floor),str(additionalrooms),str(possesiondate),str(status)]
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



