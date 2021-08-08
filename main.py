import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QStackedWidget, QFileDialog
from PyQt5.QtGui import QIcon, QCursor 
from PyQt5.QtCore import Qt , QThread, pyqtSignal,QPropertyAnimation, QPoint, QEasingCurve, pyqtSlot, QTimer

from Background import *

import File_Functions as ff

import os
import subprocess as sp
import webbrowser


class runQTDESIGNER(QThread):
   
    def __init__(self, MClass, parent = None):
        QThread.__init__(self, parent)
        self.main = MClass

    def run(self):
        os.chdir(os.path.dirname(self.main.FILEPATH))
        os.system('pyqt5-tools designer Template.ui')

class runCODE(QThread):
   
    def __init__(self, MClass, parent = None):
        QThread.__init__(self, parent)
        self.main = MClass

    def run(self):
        os.chdir(os.path.dirname(self.main.FILEPATH))
        Name = os.path.basename(self.main.FILEPATH)
        
        os.system(f'python {Name}')


class CreateFileAndFolder(QThread):
    FILEPATH = pyqtSignal(object)

    def __init__(self, File, MClass, Type, parent = None):
        QThread.__init__(self, parent)

        self.Type = Type
        self.File = File
        self.MClass = MClass
        
        #Check if Python Folder Exists in Username Document
        self.ProjectFolder = self.PythonFolder()
        
    def run(self):
        self.createFILE(self.File, self.ProjectFolder, self.Type)
    
    def createFILE(self,Name, Project_path,Proj_Type):
        programName = "explorer"
        directories = os.listdir(Project_path)
        New = Name
        file_name = New + '.py'
        if New in directories :
            NewPath = os.path.join(Project_path,New)
            filepath = os.path.join(NewPath,file_name)
            
            sp.Popen([programName, NewPath])
        else:
            NewPath = os.path.join(Project_path,New)
            
            try :
                os.mkdir(NewPath)
                

                filepath = os.path.join(NewPath,file_name)
                
                with open(filepath,'w') as f:
                    if Proj_Type == 0 :
                        ff.createGUID(f,NewPath)
                        
                    elif Proj_Type == 1:
                        
                        if self.MClass.C1 : 
                            ff.createReqScraper(f)
                        elif self.MClass.C2:
                            ff.createSelScraper(f)
                    else:
                       
                        ff.createNormal(f,self.MClass.C3,self.MClass.C4)
               
                sp.Popen([programName, NewPath])
                
                
                
            except FileExistsError:
                self.MClass.status.setText('File Exists')

        self.FILEPATH.emit(filepath)
            
                               
    def PythonFolder(self):
        if self.MClass.FolderPath == '' :
            self.MainDir = os.path.expanduser('~')
            ProjectFolder     = os.path.join(self.MainDir,'Documents','Python','My Projects')
            try:
                os.makedirs(ProjectFolder)
            except FileExistsError:
                try :
                    os.makedirs(os.path.join(self.MainDir,'Documents','Python'))
                except FileExistsError:
                    try :
                        os.makedirs(os.path.join(self.MainDir,'Documents','Python','My Projects'))
                    except FileExistsError:
                        self.MClass.status.setText('Folder Created')
            except :
                self.MClass.status.setText('Something Wrong !!!')
                        
            return ProjectFolder
        else:          
            os.chdir(self.MClass.FolderPath)
            return os.getcwd()
    

    
class MScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.C1 = False
        self.C2 = False        
        self.C3 = False
        self.C4 = False
        
        loadUi("Project_Interface.ui",self)
        
        self.FILEPATH   = ''
        self.FolderPath = self.CheckDir()
   
        self.Select_Home.clicked.connect(self.gotoHome)

        #/////      btns    /////
        
        #Home
        self.GUI_btn.clicked.connect(self.gotoGUI)
        self.Norm_btn.clicked.connect(self.gotoNormal)
        self.Scraping_btn.clicked.connect(self.gotoWebscraping)
        self.Project_btn.clicked.connect(self.pick_new)

        #GUI
        
        self.pushButton_3.setEnabled(False) #Open PYQT5 Designer with template
        self.pushButton.setEnabled(False)   # Run Code
        
        #Webscraping

        #Convert
        self.qrc_btn.clicked.connect(self.getQRC)
        self.ui_btn.clicked.connect(self.getUI)

        
        #Exit
        self.Closed.clicked.connect(self.exitprogram)
        
        #Social Media Btns
        self.Github.clicked.connect(self.gbrowser)
        self.Facebook.clicked.connect(self.fbrowser)
        self.LinkedIn.clicked.connect(self.lbrowser)
        self.Instagram.clicked.connect(self.ibrowser)
        self.Youtube.clicked.connect(self.ybrowser)

        #/////      Blurr    /////
        self.MainFrame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=2,yOffset=2))
        self.Title.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        
    #/////      FUNCTIONS    /////
    def gbrowser(self):
        webbrowser.open('https://github.com/surenjanath')
    def fbrowser(self):
        webbrowser.open('https://www.facebook.com/surenjanath.singh/')
    def lbrowser(self):
        webbrowser.open('https://www.linkedin.com/in/surenjanath/')
    def ibrowser(self):
        webbrowser.open('https://www.instagram.com/Surenjanath/')
    def ybrowser(self):
        webbrowser.open('https://www.youtube.com/c/SurenjanathSinghLC')

        
    def CheckDir(self):
        
        self.MainDir          = os.path.expanduser('~')
        self.UserDataPath     = os.path.join(self.MainDir,'Documents')
        self.UserDataFile     = os.path.join(self.UserDataPath,'PPCUserdata.txt')
        try:
            os.path.isfile(self.UserDataFile)
            
            with open(self.UserDataFile,'r') as r:
                path = r.readline().strip()
            return path
        except:
            return ''


    def getQRC(self):
        QRC = list(QFileDialog.getOpenFileName(None, 'Open QRC file',''
                                            , "QRC Files (*.qrc)"))[0]
        
        if len(QRC)>1 :
            os.chdir(os.path.dirname(QRC))
            
            
            self.status_convert.setText('QRC File Selected')
            
            Name = os.path.basename(QRC)
            
            PName = Name.split('.')[0]
            
            os.system(f'pyrcc5 -o {PName}.py {Name}')
            
            self.status_convert.setText('QRC File Converted')
        else:
            pass
        
    def getUI(self):
        UI = list(QFileDialog.getOpenFileName(None, 'Navigate to UI file',''
                                            , "UI Files (*.ui)"))[0]
        
        if len(UI)>1 :
            os.chdir(os.path.dirname(UI))
            
            self.status_convert.setText('UI File Selected')
            
            Name = os.path.basename(UI)
            PName = Name.split('.')[0]
          
            os.system(f'pyuic5 -x {Name} -o {PName}.py ')
               
            self.status_convert.setText('UI File Converted')
        else:
            pass
                    
    def pick_new(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Project Folder")
        self.FolderPath = folder_path

                    #Create File to save Userdata

        with open(self.UserDataFile,'w') as f:
            f.write(self.FolderPath)
            
       
    def gotoConvert(self):
        self.stackedWidget.setCurrentIndex(4)
     
    def gotoGUI(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
     
        self.Gui_Name.keyReleaseEvent = self.check_GText
        text = self.Gui_Name.text()
       
                #GUI
        self.pushButton_2.clicked.connect(self.gotoConvert)
        self.pushButton_3.clicked.connect(self.OpenTemplate) #Open PYQT5 Designer with template
        self.pushButton.clicked.connect(self.runCode)   # Run Code
        
    def gotoWebscraping(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 2)
                
        self.checkBox_1.stateChanged.connect(self.uncheck_1)
        self.checkBox_2.stateChanged.connect(self.uncheck_1)

        self.Scraping_Name.keyReleaseEvent = self.check_WSText
        text = self.Scraping_Name.text()
       
        
    def gotoNormal(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 3)
        
        self.checkBox_3.clicked.connect(self.uncheck_2)
        self.checkBox_4.clicked.connect(self.uncheck_2)
        
        self.Normal_Name.keyReleaseEvent = self.check_NText
        text = self.Normal_Name.text()
        
        
    def gotoHome(self):
        self.stackedWidget.setCurrentIndex(0)
        
    #/////      Animation    /////                  
    def ShowFrame(self):
        self.animation = QPropertyAnimation(self.Scroll, b"size")
        self.animation.setDuration(1200)
        self.animation.setEndValue(QtCore.QSize(360,221))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()
        
    #/////      MAIN FUNCTIONS    /////
        
    def createGUI(self):
        self.thread = CreateFileAndFolder(File = self.Gui_Name.text(), MClass = self, Type = 0)
        self.thread.FILEPATH.connect(self.FILESIGNAL)
        self.thread.start()

    def createWebscraping(self):
        self.thread = CreateFileAndFolder(File = self.Scraping_Name.text(), MClass = self, Type = 1)
        self.thread.FILEPATH.connect(self.FILESIGNAL)
        self.thread.start()

    def createNormal(self):
        self.thread = CreateFileAndFolder(File = self.Normal_Name.text(), MClass = self, Type = 2)
        self.thread.FILEPATH.connect(self.FILESIGNAL)
       
        self.thread.start()
        
    def FILESIGNAL(self,path):
        self.FILEPATH = path
        
    def OpenTemplate(self):
        self.run = runQTDESIGNER(MClass = self)
        self.run.start()
        
    def runCode(self):

        self.runCode = runCODE(MClass = self)
        self.runCode.start()   
        
    def uncheck_1(self, state):
        
        # checking if state is checked
        if state == Qt.Checked:
            
        # if first check box is selected
            if self.sender() == self.checkBox_1:
                

                # making other check box to uncheck
                self.checkBox_2.setChecked(False)
                
                self.C1 = self.checkBox_1.isChecked()      
                self.C2 = False
            # if second check box is selected
            elif self.sender() == self.checkBox_2:

                # making other check box to uncheck
                self.checkBox_1.setChecked(False)
                self.C2 = self.checkBox_2.isChecked()     
                self.C1 = False

    @pyqtSlot()
    def uncheck_2(self):
        self.C3 = self.checkBox_3.isChecked()
        self.C4 = self.checkBox_4.isChecked()

    # DRAGGLESS INTERFACE

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ClosedHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(QMouseEvent.globalPos() - self.m_DragPosition)
                QMouseEvent.accept()
        except AttributeError:
            self.status.setText('Attribute Error in Dragging')
        except:
            self.status.clear()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def exitprogram(self):
        sys.exit()
        
    # Text
    # ///////////////////////////////////////////////////////////////
    def check_GText(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            text = self.Gui_Name.text()
            
            if len(text.split(' ')) > 1 :
                self.Accept = False
                self.Gui_Name.setStyleSheet("#GUI_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: Red;\
                                            color: Red;\
                                            padding-bottom:7px;}")
                self.Error.setText('Please Omit Spaces !')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.shake_window()
                
            elif len(text) < 1 :
                self.Accept = False
                self.Gui_Name.setStyleSheet("#GUI_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: Red;\
                                            color: Red;\
                                            padding-bottom:7px;}")
                self.Error.setText('Please Enter Name of Project !')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.shake_window()
                
            elif len(text) >= 1 and len(text) < 3 :
                self.Accept = False
                self.Gui_Name.setStyleSheet("#GUI_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: Red;\
                                            color: Red;\
                                            padding-bottom:7px;}")
                self.Error.setText('Please Give a long Name !')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.shake_window()                    
            else:
                self.Error.clear()
                self.Accept = True
                self.Gui_Name.setStyleSheet("#GUI_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: rgb(0, 255, 0);\
                                            color: rgb(0, 255, 0);\
                                            padding-bottom:7px;}")
                self.createGUI()
                self.pushButton_3.setEnabled(True) #Open PYQT5 Designer with template
                self.pushButton.setEnabled(True)   # Run Code

    # Text
    # ///////////////////////////////////////////////////////////////
    def check_WSText(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            text = self.Scraping_Name.text()
            if self.checkBox_1.isChecked() or self.checkBox_2.isChecked() :
                if len(text.split(' ')) > 1 :
                    self.Accept = False
                    self.Scraping_Name.setStyleSheet("#Scraping_Name:focus { background-color:rgba(0,0,0,0);\
                                                border-bottom-color: Red;\
                                                color: Red;\
                                                padding-bottom:7px;}")
                    self.Error.setText('Please Omit Spaces !')
                    self.Error.setStyleSheet("#Error:focus {color:red;}")
                    self.shake_window()
                    
                elif len(text) < 1 :
                    self.Accept = False
                    self.Scraping_Name.setStyleSheet("#Scraping_Name:focus { background-color:rgba(0,0,0,0);\
                                                border-bottom-color: Red;\
                                                color: Red;\
                                                padding-bottom:7px;}")
                    self.Error.setText('Please Enter Name of Project !')
                    self.Error.setStyleSheet("#Error:focus {color:red;}")
                    self.shake_window()
                    
                elif len(text) >= 1 and len(text) < 3 :
                    self.Accept = False
                    self.Scraping_Name.setStyleSheet("#Scraping_Name:focus { background-color:rgba(0,0,0,0);\
                                                border-bottom-color: Red;\
                                                color: Red;\
                                                padding-bottom:7px;}")
                    self.Error.setText('Please Give a long Name !')
                    self.Error.setStyleSheet("#Error:focus {color:red;}")
                    self.shake_window()                    
                else:
                    self.Error.clear()
                    self.Accept = True
                    self.Scraping_Name.setStyleSheet("#Scraping_Name:focus { background-color:rgba(0,0,0,0);\
                                                border-bottom-color: rgb(0, 255, 0);\
                                                color: rgb(0, 255, 0);\
                                                padding-bottom:7px;}")
                    self.createWebscraping()
            else:
                self.Error.setText('Please Select a Template Below!')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.Scraping_Name.setStyleSheet("#Scraping_Name:focus { background-color:rgba(0,0,0,0);\
                                                border-bottom-color: Red;\
                                                color:Red;\
                                                padding-bottom:7px;}")
                self.shake_window()

    # Text
    # ///////////////////////////////////////////////////////////////
    def check_NText(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            text = self.Normal_Name.text()
            
            if len(text.split(' ')) > 1 :
                self.Accept = False
                self.Normal_Name.setStyleSheet("#Normal_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: Red;\
                                            color: Red;\
                                            padding-bottom:7px;}")
                self.Error.setText('Please Omit Spaces !')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.shake_window()
                
            elif len(text) < 1 :
                self.Accept = False
                self.Normal_Name.setStyleSheet("#Normal_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: Red;\
                                            color: Red;\
                                            padding-bottom:7px;}")
                self.Error.setText('Please Enter Name of Project !')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.shake_window()
                
            elif len(text) >= 1 and len(text) < 3 :
                self.Accept = False
                self.Normal_Name.setStyleSheet("#Normal_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: Red;\
                                            color: Red;\
                                            padding-bottom:7px;}")
                self.Error.setText('Please Give a long Name !')
                self.Error.setStyleSheet("#Error:focus {color:red;}")
                self.shake_window()                    
            else:
                self.Error.clear()
                self.Accept = True
                self.Normal_Name.setStyleSheet("#Normal_Name:focus { background-color:rgba(0,0,0,0);\
                                            border-bottom-color: rgb(0, 255, 0);\
                                            color: rgb(0, 255, 0);\
                                            padding-bottom:7px;}")
                self.createNormal()


    def shake_window(self):
        # shake WINDOW
        
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))
        
# main
if __name__=="__main__":

    app = QApplication(sys.argv)
    widget = MScreen()
    widget.setFixedHeight(500)
    widget.setFixedWidth(400)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        pass
