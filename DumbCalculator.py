import sys
from PyQt4 import QtCore, QtGui
import traceback

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
		#Main Window Settings
		self.setGeometry(50,50,520,300)
		self.setWindowTitle("Dumb Calculator - Created For Fun !")
		self.setWindowIcon(QtGui.QIcon('python.png'))

		#Close Action
		exitAction = QtGui.QAction(QtGui.QIcon('python.png'),"Close Now !", self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.setStatusTip('Leave the Application')
		exitAction.triggered.connect(self.close_application)
		self.statusBar()

		#Menubar
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(exitAction)
		

		# Create textboxs
		self.number_1 = QtGui.QLineEdit(self)
		self.number_1.move(50, 50)
		self.number_1.resize(380,40)
		
		self.number_2 = QtGui.QLineEdit(self)
		self.number_2.move(50, 100)
		self.number_2.resize(380,40)
		
		self.result_label = QtGui.QLabel(self)
		self.result_label.move(180, 150)
		self.result_label.setText("Result Will Be Here !")

		self.fun_label = QtGui.QLabel(self)
		self.fun_label.resize(450, 25)
		self.fun_label.move(90, 170)
		self.fun_label.setText("This is the dumbest thing I've ever coded just for fun !!!")

		#Main Home Proccess
		quiteBtn = QtGui.QPushButton("Quite", self)
		quiteBtn.resize(100, 50)
		quiteBtn.move(10,220)
		quiteBtn.clicked.connect(self.close_application)

		addBtn = QtGui.QPushButton("+", self)
		addBtn.resize(100, 50)
		addBtn.move(110,220)
		addBtn.clicked.connect(self.addNumbers)

		minusButton = QtGui.QPushButton('-', self)
		minusButton.resize(100,50)
		minusButton.move(210,220)
		minusButton.clicked.connect(self.minusNumbers)

		darbButton = QtGui.QPushButton('*', self)
		darbButton.resize(100,50)
		darbButton.move(310,220)
		darbButton.clicked.connect(self.darbNumbers)

		kesmaButton = QtGui.QPushButton('/', self)
		kesmaButton.resize(100,50)
		kesmaButton.move(410,220)
		kesmaButton.clicked.connect(self.kesmaNumbers)

		self.show()	

	def addNumbers(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		numara1 = float(self.number_1.text())
		numara2 = float(self.number_2.text())
		if numara1 != 0 or numara1 != "":
			result = numara1 + numara2			
		msg.setText("The Result is " + str(result))
		self.result_label.setText("The Result is " + str(result))
		msg.setWindowTitle("The Result")
		retval = msg.exec_()

	def minusNumbers(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		numara1 = float(self.number_1.text())
		numara2 = float(self.number_2.text())
		if numara1 != 0 or numara1 != "":
			result = numara1 - numara2
		msg.setText("The Result is " + str(result))
		self.result_label.setText("The Result is " + str(result))
		msg.setWindowTitle("The Result")
		retval = msg.exec_()

	def darbNumbers(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		numara1 = float(self.number_1.text())
		numara2 = float(self.number_2.text())
		if numara1 != 0 or numara1 != "":
			result = numara1 * numara2
		msg.setText("The Result is " + str(result))
		self.result_label.setText("The Result is " + str(result))
		msg.setWindowTitle("The Result")
		retval = msg.exec_()

	def kesmaNumbers(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		numara1 = float(self.number_1.text())
		numara2 = float(self.number_2.text())
		if numara1 != 0 or numara1 != "":
			result = numara1 / numara2
		msg.setText("The Result is " + str(result))
		self.result_label.setText("The Result is " + str(result))
		msg.setWindowTitle("The Result")
		retval = msg.exec_()


	#Close The Whole Application
	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Exit !', 'Are you sure you wanna exit?',
			QtGui.QMessageBox.Yes | QtGui.QMessageBox.No
			)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass


#Main Program Function
def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())
try:
	main()
except:
	traceback.print_exc()


