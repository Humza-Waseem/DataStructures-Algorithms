import sys
import csv
from PyQt5 import Qt
from PyQt5.uic import loadUi
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        loadUi("epayPunjab.ui",self)
        self.NextButton.clicked.connect(self.AddData)
        self.ResetButton.clicked.connect(self.resetValues)

    def AddData(self):
        district = self.DistrictName.text()
        tehsil = self.TehsilName.text()
        stampPaperType = self.StampPaperType.text()
        deedName = self.DeedName.text()
        Name = self.Name.text()
        CNIC = self.CNIC.text()
        Contact  = self.Contact.text()
        Email = self.Email.text()
        captcha = self.Password.text()
        if(captcha == "JWEW" and district != None and tehsil != None and stampPaperType != None and deedName != None and Name != None and CNIC != None and Contact != None and Email != None):
                UserData = [district,tehsil,stampPaperType,deedName,Name,CNIC,Contact,Email]

                with open('Data.csv', 'a+',encoding="utf-8",newline="") as fileInput:
                    writer = csv.writer(fileInput)
                    writer.writerows([UserData])
                self.resetValues()

    def resetValues(self):
            self.DistrictName.setText("")
            self.TehsilName.setText("")
            self.StampPaperType.setText("")
            self.DeedName.setText("")
            self.Name.setText("")
            self.CNIC.setText("")
            self.Contact.setText("")
            self.Email.setText("")
            self.Password.selfText()
            

app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
