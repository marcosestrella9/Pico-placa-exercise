# -*- coding: utf-8 -*-
#IMPORT REQUIRED LIBRARIES
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QLineEdit,QApplication, QMainWindow, QMessageBox)
import sys
import datetime

#MODIFY THE WINDOW
class MyWindow (QMainWindow):
    def __init__ (self):
        super(MyWindow,self).__init__()
        self.setGeometry(400,200,450,200)
        self.setWindowTitle("PICO & PLACA CHECKING")
        self.initUI()
        self.setWindowIcon(QtGui.QIcon("picoyplaca.png"))
        
    def initUI(self):
        
        self.lblnumber = QtWidgets.QLabel(self)
        self.lblnumber.setText("License plate number")
        self.lblnumber.move(50,25)
        self.lblnumber.adjustSize()
        
        self.lbldate = QtWidgets.QLabel(self)
        self.lbldate.setText("Date")
        self.lbldate.move(200,25)
        self.lbldate.adjustSize()
        
        self.lbltime = QtWidgets.QLabel(self)
        self.lbltime.setText("Time")
        self.lbltime.move(325,25)
        self.lbltime.adjustSize()
        
        self.tbxnumber=QLineEdit(self)
        self.tbxnumber.move(50,50)
        self.tbxnumber.setPlaceholderText("PBD-8032")
        self.tbxnumber.setMaxLength(8)
        
        self.tbxdate=QLineEdit(self)
        self.tbxdate.move(175,50)
        self.tbxdate.setPlaceholderText("dd/mm/yy")        
        self.tbxdate.setMaxLength(10)
        
        self.tbxtime=QLineEdit(self)
        self.tbxtime.move(300,50)
        self.tbxtime.setPlaceholderText("hh:mm")
        self.tbxtime.setMaxLength(5)
        
        self.btncheck=QtWidgets.QPushButton(self)
        self.btncheck.setText("Check")
        self.btncheck.clicked.connect(self.check)
        self.btncheck.setGeometry(350,100,75,50)
    
    def checknumber(self,number):
        nnumber=number.split("-")
        try:
            onlynumber=int(nnumber[1])
            booleann= True
        except:
            booleann= False
            self.msgenumber=QMessageBox()
            self.msgenumber.setWindowTitle("Invalid character")
            self.msgenumber.setText("Please check License plate number")
            self.msgenumber.setIcon(QMessageBox.Warning)
            self.msgenumber.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            self.msgenumber.setDefaultButton(QMessageBox.Ok)
            self.msgenumber.exec_()
        return booleann

    def checkdate(self,date):
        ndate=date.split("/")
        try:
            day=int(ndate[0])
            month=int(ndate[1]) 
            year=int(ndate[2])
            if (day<32 and day>0 and month>0 and month<13 and year>0):
                booleand= True
            else:
                self.msgedatef=QMessageBox()
                self.msgedatef.setWindowTitle("Error in date")
                self.msgedatef.setText("Please check the day(1-31), month(1-12) and year>0")
                self.msgedatef.setIcon(QMessageBox.Warning)
                self.msgedatef.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                self.msgedatef.setDefaultButton(QMessageBox.Ok)
                self.msgedatef.exec_() 
                booleand=False  
        except:
            booleand= False
            self.msgedate=QMessageBox()
            self.msgedate.setWindowTitle("Invalid character")
            self.msgedate.setText("Please check the date")
            self.msgedate.setIcon(QMessageBox.Warning)
            self.msgedate.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            self.msgedate.setDefaultButton(QMessageBox.Ok)
            self.msgedate.exec_()
        return booleand
    
    def checktime(self,time):
        ntime=time.split(":")
        try:
            hour=int(ntime[0])
            minutes=int(ntime[1]) 
            if (hour<24 and hour>=0 and minutes>=0 and minutes<60):
                booleant= True
            else:
                self.msgetimef=QMessageBox()
                self.msgetimef.setWindowTitle("Error in time number")
                self.msgetimef.setText("Please check the hour(0-23) and minutes(0-59)")
                self.msgetimef.setIcon(QMessageBox.Warning)
                self.msgetimef.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                self.msgetimef.setDefaultButton(QMessageBox.Ok)
                self.msgetimef.exec_() 
                booleant=False                
        except:
            booleant= False
            self.msgetime=QMessageBox()
            self.msgetime.setWindowTitle("Invalid character")
            self.msgetime.setText("Please check the time")
            self.msgetime.setIcon(QMessageBox.Warning)
            self.msgetime.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            self.msgetime.setDefaultButton(QMessageBox.Ok)
            self.msgetime.exec_() 
        return booleant
    
    def checkhourpyp(self,hh,mm):
        pypmorning=False
        pypafternoon=False
        if (hh>=7):
            if (hh<9):
                pypmorning= True
            elif (hh==9):
                if(mm<=30):
                    pypmorning= True
                else:
                    pypmorning= False
            else:
                pypmorning= False
                
        if (hh>=16):
            if (hh<19):
                pypafternoon= True
            elif (hh==19):
                if(mm<=30):
                    pypafternoon= True
                else:
                    pypafternoon= False
            else:
                pypafternoon= False
        if pypafternoon or pypmorning:
            return True
        else:
            return False
     
    def checkdayandnumberpyp(self,daynumberinw,lastdigit):
        daysinpyp=[(0,1),(0,2),
                   (1,3),(1,4),
                   (2,5),(2,6),
                   (3,7),(3,8),
                   (4,9),(4,0),]
        x=(daynumberinw,lastdigit)
        if x in daysinpyp:
            return True
        else:
            return False
        
        
    
    def checkpyp(self,daynumberinw,hour,minute,lastdigit):
        self.infractor=False
        if self.checkhourpyp(hour,minute) and self.checkdayandnumberpyp(daynumberinw, lastdigit):
            self.infractor=True
        else:
            self.infractor=False
        return self.infractor
    
    def check(self):    
        if (self.checknumber(self.tbxnumber.text()) and self.checkdate(self.tbxdate.text()) and self.checktime(self.tbxtime.text())):
            self.msgccheck=QMessageBox()
            self.msgccheck.setWindowTitle("Check?")
            self.msgccheck.setText("Are you sure to check License plate number:"+self.tbxnumber.text()+" ,date: "+self.tbxdate.text()+" ,time: "+self.tbxtime.text())
            self.msgccheck.setIcon(QMessageBox.Question)
            self.msgccheck.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            self.msgccheck.setDefaultButton(QMessageBox.Ok)
            self.execmsgccheck= self.msgccheck.exec_()
            if self.execmsgccheck==1024:
                self.licensenumber=self.tbxnumber.text().split("-")
                self.lastdigitnumber=self.licensenumber[1][-1]
                #day 0-6:monday-sunday
                self.daynumberinweek=datetime.datetime.strptime(self.tbxdate.text(),'%d/%m/%Y').weekday()
                self.thetime=self.tbxtime.text().split(":")
                self.hourn=self.thetime[0]
                self.minn=self.thetime[1]
                #check
                self.resultcheck=self.checkpyp(int(self.daynumberinweek),int(self.hourn),int(self.minn),int(self.lastdigitnumber))
                if (self.resultcheck):
                    self.msgresulti=QMessageBox()
                    self.msgresulti.setWindowTitle("Infractor")
                    self.msgresulti.setText("The car with the license plate number:"+self.tbxnumber.text()+ " cannot be on the road at date: "+self.tbxdate.text()+" ,time: "+self.tbxtime.text())
                    self.msgresulti.setIcon(QMessageBox.Warning)
                    self.msgresulti.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                    self.msgresulti.setDefaultButton(QMessageBox.Ok)
                    self.msgresulti.exec_() 
                else:
                    self.msgresultni=QMessageBox()
                    self.msgresultni.setWindowTitle("NO Infractor")
                    self.msgresultni.setText("The car with the license plate number:"+self.tbxnumber.text()+ " can be on the road at date: "+self.tbxdate.text()+" ,time: "+self.tbxtime.text())
                    self.msgresultni.setIcon(QMessageBox.Warning)
                    self.msgresultni.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                    self.msgresultni.setDefaultButton(QMessageBox.Ok)
                    self.msgresultni.exec_()
                    
                self.tbxdate.clear()
                self.tbxtime.clear()
                self.tbxnumber.clear()

#CREATE AND DISPLAY THE WINDOW 
def window():
    app = QApplication(sys.argv)
    principal_window=MyWindow()
    principal_window.show()
    sys.exit(app.exec())
    
window()
