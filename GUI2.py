
import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import MySQLdb as mdb


notecards = [""]
definition = []
word_lists = []

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 1000
        self.top = 1000
        self.width = 350
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
    
        # Create word textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 40)
        self.textbox.resize(250,40)
        label = QLabel('Vocabulary', self)
        label.move(138,10)
        label2 = QLabel('Definition', self)
        label2.move(138,90)
        label3 = QLabel('notecards', self)
        label3.move(443,22)
        #create a definition textbox
        self.textBox2 = QLineEdit(self)
        self.textBox2.move(50, 130)
        self.textBox2.resize(250,40)

        # Create a button in the window
        self.button = QPushButton('Create notecards', self)
        
        #show the user that all the notecards he just created
        self.button2 = QPushButton("show all the notecards",self)
        
        self.button3 = QPushButton("Quiz myself!",self)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.button.resize(180,25)
        self.button.move((self.width/2 - 90),190)

        self.button2.clicked.connect(self.on_click2)
        self.button2.resize(180,25)
        self.button2.move((self.width/2 - 90),230)

        self.button3.clicked.connect(self.on_click3)
        self.dialog = Second(self)
        self.button3.resize(180,25)
        self.button3.move((self.width/2 - 90),270)
        notecards.remove(notecards[0])
        # self.button3.clicked.connect(self.on_click3)
        self.show()


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        textboxvalue2 = self.textBox2.text()

        global notecards
        notecards.append(textboxValue)
        definition.append(textboxvalue2)

        QMessageBox.question(self, 'Message - pythonspot.com', "The notecard you just created: " + textboxValue + ":" + textboxvalue2, QMessageBox.Ok, QMessageBox.Ok)

        self.textbox.setText("")
        self.textBox2.setText("")
        for i in range(len(notecards)):
            word_list = []
            word_list.append(i)
            word_list.append(notecards[i])
            word_list.append(definition[i])
            word_list.append(random.randint(1, 5))
            word_list.append(random.randint(1, 5))

            word_lists.append(word_list)

    
    def on_click2(self):
        str2 = ''
        length = len(notecards)

        for i in range(length):

            str2 += str(i + 1) 
            str2 += '.'
            str2 += " "
            str2 += notecards[i]
            str2 += ':'
            str2 += definition[i]
            str2 += "\n"

        QMessageBox.question(self, 'Message - pythonspot.com', "The notecard you created: " + "\n" + str2, QMessageBox.Ok, QMessageBox.Ok)
    
    def on_click3(self):
        self.dialog.show()


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.title = 'Quizing time'
        self.left = 1000
        self.top = 1000
        self.width = 350
        self.height = 400
        self.initUI2()
        
    
    def initUI2(self):
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel('please give the definiton of the word given', self)
        label.resize(300,20)
        label.move(20,10)

        
        # testword_num = random.randint(1,(l.word_lists)+1))
        # label2 = QLabel(ex1.word_lists[1][testword_num], self)
        # label2.resize(500,30)
        # label2.move(40,40)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(50, 130)
        self.textbox3.resize(250,40)

        # self.button = QPushButton("check", self)
        # self.button.clicked.connect(self.on_click4)
        # self.button.resize(180,25)
        # self.button.move((self.width/2 - 90),190)

    #     self.button2 = QPushButton("next one", self)
    #     self.button2.clicked.connect(self.on_click5)
    #     self.button2.resize(180,25)
    #     self.button2.move((self.width/2 - 90),230)

    # @pyqtSlot()
    # def on_click4(self):
    #     num = notecards.index(testwords)

    #     if textbox3.text == definition[num]:
    #         QMessageBox.question(self, 'Message - pythonspot.com', "you good", QMessageBox.Ok, QMessageBox.Ok)
    #     else:
    #         QMessageBox.question(self, 'Message - pythonspot.com', "no" + str2, QMessageBox.Ok, QMessageBox.Ok)
    
    # def on_click5(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())