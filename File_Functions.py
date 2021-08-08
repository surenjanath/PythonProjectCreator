import os
#//////////////////////////////////////////////////
#               GUI OPTIONS
#//////////////////////////////////////////////////
def createUI(f):
#Save to template.ui
    f.write('''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>320</width>
    <height>390</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QFrame#frame{
	background-color: qlineargradient(spread:pad, x1:1.072045, y1:0.124, x2:0.368, y2:1, stop:0.227273 rgba(10, 214, 255, 155), stop:0.806818 rgba(112, 32,213,191));
	border-radius:10px;
}
QPushButton#Closed{
	background-color: rgba(0, 0,0, 0);
	color:rgba(10,15,155,255);
	
	border-radius:5px;
}
QPushButton#Closed:hover{
	color:rgba(250,223,11,255);
}
QPushButton#Closed:pressed{
	padding-left:1px;
	padding-top:1px;
	background-color:rgba(150,123,111,255);
}
QLineEdit#Name{
	background-color:rgba(0,0,0,0);
	border:2px solid rgba(0,0,0,0);
	border-bottom-color: rgba(1,100,100,255);
	color:rgb(0,0,0);
	padding-bottom:7px;
}</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>260</width>
      <height>350</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>30</y>
       <width>260</width>
       <height>20</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Microsoft Yi Baiti</family>
       <pointsize>16</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>T E M P L A T E</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>80</y>
       <width>191</width>
       <height>251</height>
      </rect>
     </property>
     <property name="text">
      <string>Hello World</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QPushButton" name="Closed">
     <property name="geometry">
      <rect>
       <x>230</x>
       <y>10</y>
       <width>20</width>
       <height>20</height>
      </rect>
     </property>
     <property name="maximumSize">
      <size>
       <width>20</width>
       <height>20</height>
      </size>
     </property>
     <property name="font">
      <font>
       <pointsize>10</pointsize>
      </font>
     </property>
     <property name="text">
      <string>X</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="Name">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>140</y>
       <width>200</width>
       <height>40</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <kerning>false</kerning>
      </font>
     </property>
     <property name="mouseTracking">
      <bool>false</bool>
     </property>
     <property name="acceptDrops">
      <bool>false</bool>
     </property>
     <property name="whatsThis">
      <string notr="true">Name of GUI Project File</string>
     </property>
     <property name="styleSheet">
      <string notr="true"/>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="alignment">
      <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
     </property>
     <property name="placeholderText">
      <string>Name of Project</string>
     </property>
     <property name="clearButtonEnabled">
      <bool>true</bool>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>250</y>
       <width>191</width>
       <height>21</height>
      </rect>
     </property>
     <property name="text">
      <string>QLineEdit : </string>
     </property>
     <property name="wordWrap">
      <bool>true</bool>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>50</y>
       <width>161</width>
       <height>16</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>5</pointsize>
      </font>
     </property>
     <property name="text">
      <string>Created By Surenjanath</string>
     </property>
    </widget>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

    ''')


#//////////////////////////////////////////////////

def createGUID(f,path): #GUI Designer Option
    with open(os.path.join(path,'Template.ui'),'w') as U:
        createUI(U)
        
    f.write('''
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon, QCursor

import sys
import os

#Class
class MainWindow(QMainWindow):

    def __init__(self):
        """MainWindow constructor"""
        super(MainWindow,self).__init__()
        # Main UI code goes here
        loadUi("Template.ui",self)
        
        self.Name.returnPressed.connect(self.on_returnButton)
        
        self.Closed.clicked.connect(self.exitprogram)
        # End main UI code
        
    @QtCore.pyqtSlot()
    def on_returnButton(self):
        text = self.Name.text()
        self.label_3.setText('QLineEdit : %a ' %str(text))   

        
    # DRAGGLESS INTERFACE

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def exitprogram(self):
        sys.exit()        

# Main        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Screen = MainWindow()
    Screen.setFixedHeight(390)
    Screen.setFixedWidth(320)
    Screen.setWindowFlags(Qt.FramelessWindowHint)
    Screen.setAttribute(Qt.WA_TranslucentBackground)
    Screen.show()
    sys.exit(app.exec())
''')

#//////////////////////////////////////////////////
#              WEBSCRAPING OPTIONS
#//////////////////////////////////////////////////  
def createReqScraper(f):
    f.write('''
# Libraries
from bs4 import BeautifulSoup as bs
import requests


def main():

    # Enter your website here 
    url='<<Your Website>>'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

    # Request to website and download HTML contents
    with requests.Session() as s:
        r = s.get(url, headers = headers)
        soup = bs(r.content,'lxml')
        print(soup.title)
        print(soup.find('div',{'class':'something'}))
 
''')

def createSelScraper(f):
    f.write('''
# Libraries
from bs4 import BeautifulSoup as bs
import requests

# Request to website and download HTML contents

# Enter your website here 
url='<<Your Website>>'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }


with requests.Session() as s:
    r = s.get(url, headers = headers)
    soup = bs(r.content,'lxml')
    print(soup.title)
    print(soup.find('div',{'class':'something'}))
 
''')   
 
#//////////////////////////////////////////////////
#              NORMAL PY File OPTIONS
#//////////////////////////////////////////////////

def createNormal(f,add_fn,add_class):
    f.write('''
# Libraries

import sys
import os


''')
    if add_fn ==True:
        f.write('''
# Function
def function_1(Argument1,Argument2):
    print(Argument1,Argument2)
''')
    if add_class ==True :
        f.write('''
# Class
class IamAClass():
    def __init__(text):
        print('Hello World')
        self.text = text
    def Hi(self)
        print('Text %a' %self.text)
        ''')

    if add_fn ==True and add_class == True:
        f.write('''
# Main        
if __name__ == '__main__':
    
    function_1('Hello','World)

    text = 'My World is Amazing'
    app = IamAClass(text = text)
    app.Hi()
    
''')
    elif add_fn == True:
        f.write('''
# Main        
if __name__ == '__main__':
    text  = 'My World is Amazing'
    text2 = 'No'
    function_1(text,text2)
''')
    else : 
        f.write('''
# Main        
if __name__ == '__main__':
    print('Hello World')
''')
        
#////////////////////////////////////////////////// 
