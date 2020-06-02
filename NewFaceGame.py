# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import random

class Head(QWidget):
    def __init__(self):
        super().__init__() 
 
        self.width=400
        self.height=500
        self.x=random.randint(10, 310)
        self.y=random.randint(40, 140)
        self.size=80
        
        self.dx=0
        self.dy=0
        
        self.setWindowTitle("NewFaceGame")
        self.resize(self.width, self.height)

        self.setMinimumHeight(self.height)
        self.setMinimumWidth(self.width)
        self.setMaximumHeight(self.height)
        self.setMaximumWidth(self.width)
        
        self.score = 0
        self.scorelabel = QLabel("")
        layout= QHBoxLayout()
        layout.addWidget(self.scorelabel)
        self.setLayout(layout)
        
        self.admit = 0
        
        self.timer= QTimer()
        self.timer.timeout.connect(self.move)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("#74A82A"))
        painter.setPen(Qt.white)
        painter.drawRect(0,0,self.width,self.height)

        painter.setPen(Qt.black)
        #lefth
        painter.setBrush(QColor(242, 39, 39))
        painter.drawRect(150, 380, 20, 60)
        painter.setBrush(Qt.yellow)
        painter.drawRect(150, 420, 20, 20)
        #righth
        painter.setBrush(QColor(242, 39, 39))
        painter.drawRect(230, 380, 20, 60)
        painter.setBrush(Qt.yellow)
        painter.drawRect(230, 420, 20, 20)
        #leftl
        painter.setBrush(QColor(242, 39, 39))
        painter.drawRect(205, 460, 25, 40)
        painter.setBrush(Qt.yellow)
        painter.drawRect(205, 480, 25, 20)
        #rightl
        painter.setBrush(QColor(242, 39, 39))
        painter.drawRect(170, 460, 25, 40)
        painter.setBrush(Qt.yellow)
        painter.drawRect(170, 480, 25, 20)
        #body
        painter.setBrush(QColor(242, 39, 39))
        painter.drawRect(170, 380, 60, 80)
        painter.setBrush(Qt.yellow)
        painter.drawRect(170, 440, 60, 10)
        painter.drawEllipse(192, 405, 16, 16)
        
        painter.setBrush(QColor(242, 182, 148))       
        painter.drawEllipse(self.x, self.y, self.size, self.size)
        painter.setBrush(QColor(242, 72, 34))       
        painter.drawEllipse(self.x, self.y+25, self.size-50, self.size-50)
        painter.drawEllipse(self.x+50, self.y+25, self.size-50, self.size-50)
        painter.setBrush(QColor(242, 39, 39))  
        painter.drawEllipse(self.x+25, self.y+25, self.size-50, self.size-50)
        
        self.Hit()
        
    def move(self):
        self.x= self.x+self.dx
        if(self.x>self.width-self.size):
            self.x= 2*(self.width-self.size)-self.x
            self.dx= -self.dx
        elif(self.x<0):
            self.x= -self.x
            self.dx= -self.dx
 
        self.y= self.y+self.dy
        if(self.y>self.height-self.size):
            self.y= 2*(self.height-self.size)-self.y
            self.dy= -self.dy
        elif(self.y<0):
            self.y= -self.y
            self.dy= -self.dy
        
        self.update()
        
    def score(self):
         pass
        
    def mousePressEvent(self, event):
        self.x_p = int(event.x())
        self.y_p = int(event.y())

    
    def mouseReleaseEvent(self, event):
        if self.admit==0:
            self.x_r = int(event.x())
            self.y_r = int(event.y())
            self.dx = (self.x_p - self.x_r)/10
            self.dy = (self.y_p - self.y_r)/10
            
            self.timer.start(10)
        else:
            self.x=random.randint(10, 310)
            self.y=random.randint(40, 140)
            self.dx = 0
            self.dy = 0
            self.admit = 0
            self.score = 0
            self.scorelabel.setText("")
            self.timer.start(10)
        
    def Hit(self):
        if self.x>110 and self.x<210 and self.y>300 and self.y<320:
            self.timer.stop()
            self.admit = 1
            self.score = int(50000//((160-self.x)**2+(310-self.y)**2))
            self.scorelabel.setText("{0} POINT!".format(self.score))
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainw = Head()
    mainw.show()
    sys.exit(app.exec())
