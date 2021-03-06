# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("QLabel#Shadow{\n"
"    color: qlineargradient(spread:pad, x1:0.472045, y1:0.324, x2:0.568, y2:1, stop:0.227273 rgba(0, 104, 255, 155), stop:0.806818 rgba(2, 32, 43, 71));\n"
"}\n"
"\n"
"QLabel#Title{\n"
"    color: rgb(170, 0, 127);\n"
"}\n"
"\n"
"QFrame#MainFrame{\n"
"    border-image: url(:/Pictures/Images/Background.jpg);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QLabel#Background_shadow{\n"
"    background-color: rgba(0, 0, 0, 95);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit#Gui_Name,#Normal_Name,#Scraping_Name{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:2px solid rgba(0,0,0,0);\n"
"    border-bottom-color: rgba(1,100,100,255);\n"
"    color:rgb(255,255,0);\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton#Closed{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(10,15,155,255);\n"
"    \n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#Closed:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"\n"
"QPushButton#Closed:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#Github,#Facebook,#LinkedIn,#Instagram,#Youtube{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(120,215,255,255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Github:hover,#Facebook:hover,#LinkedIn:hover,#Instagram:hover,#Youtube:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"QPushButton#Github:pressed,#Facebook:pressed,#LinkedIn:pressed,#Instagram:pressed,#Youtube:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#GUI_btn,#Norm_btn,#Scraping_btn,#pushButton,#pushButton_2,#pushButton_3,#pushButton_4,#Project_btn,#ui_btn,#qrc_btn{\n"
"    border-radius:10px;\n"
"    background-color: rgba(190, 155, 255,255);\n"
"    color:rgba(0,0,0,255);\n"
"}\n"
"\n"
"QPushButton#GUI_btn:hover,#Norm_btn:hover,#Scraping_btn:hover,#pushButton:hover,#pushButton_2:hover,#pushButton_3:hover,#pushButton_4:hover,#Project_btn:hover,#ui_btn:hover,#qrc_btn:hover{\n"
"    color:rgba(255,255,200,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 100, 229, 255), stop:1 rgba(255, 155, 255, 255));\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton#GUI_btn:pressed,#Norm_btn:pressed,#Scraping_btn:pressed,#pushButton:pressed,#pushButton_2:pressed,#pushButton_3:pressed,#pushButton_4:pressed,#Project_btn:pressed,#ui_btn:pressed,#qrc_btn:pressed{\n"
"    border-radius:10px;\n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QLabel#label,#label_2{\n"
"    color: rgba(215, 215, 150,220);\n"
"}\n"
"\n"
"QLabel#GLabel,#SLabel,#NLabel{\n"
"    color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QPushButton#Select_Home{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(10,15,155,255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Select_Home:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"\n"
"QPushButton#Select_Home:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QCheckBox#checkBox_1,#checkBox_2,#checkBox_3,#checkBox_4{\n"
"    color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QLabel#Error{\n"
"    color:red;\n"
"}\n"
"QLabel#NInfo,#SInfo,#GInfo{\n"
"    \n"
"    color: rgb(0, 255, 255);\n"
"}\n"
"QLabel#status_convert,#Information{\n"
"color:yellow;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(20, 20, 350, 470))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.Shadow = QtWidgets.QLabel(self.MainFrame)
        self.Shadow.setGeometry(QtCore.QRect(0, 30, 350, 101))
        font = QtGui.QFont()
        font.setFamily("Quickier Demo")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.Shadow.setFont(font)
        self.Shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.Shadow.setObjectName("Shadow")
        self.Title = QtWidgets.QLabel(self.MainFrame)
        self.Title.setGeometry(QtCore.QRect(0, 25, 351, 101))
        font = QtGui.QFont()
        font.setFamily("Quickier Demo")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Background_shadow = QtWidgets.QLabel(self.MainFrame)
        self.Background_shadow.setGeometry(QtCore.QRect(0, 0, 350, 470))
        self.Background_shadow.setText("")
        self.Background_shadow.setObjectName("Background_shadow")
        self.frame = QtWidgets.QFrame(self.MainFrame)
        self.frame.setGeometry(QtCore.QRect(10, 130, 331, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 330, 311))
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(0, 30, 330, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Home)
        self.label_2.setGeometry(QtCore.QRect(0, 220, 330, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Home)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 331, 151))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GUI_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.GUI_btn.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.GUI_btn.setFont(font)
        self.GUI_btn.setFlat(False)
        self.GUI_btn.setObjectName("GUI_btn")
        self.verticalLayout.addWidget(self.GUI_btn)
        self.Scraping_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Scraping_btn.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Scraping_btn.setFont(font)
        self.Scraping_btn.setFlat(False)
        self.Scraping_btn.setObjectName("Scraping_btn")
        self.verticalLayout.addWidget(self.Scraping_btn)
        self.Norm_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Norm_btn.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Norm_btn.setFont(font)
        self.Norm_btn.setFlat(False)
        self.Norm_btn.setObjectName("Norm_btn")
        self.verticalLayout.addWidget(self.Norm_btn)
        self.Project_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Project_btn.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Project_btn.setFont(font)
        self.Project_btn.setFlat(False)
        self.Project_btn.setObjectName("Project_btn")
        self.verticalLayout.addWidget(self.Project_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Home)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 250, 331, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Facebook = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Facebook.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(17)
        self.Facebook.setFont(font)
        self.Facebook.setObjectName("Facebook")
        self.horizontalLayout_3.addWidget(self.Facebook)
        self.Instagram = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Instagram.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(17)
        self.Instagram.setFont(font)
        self.Instagram.setObjectName("Instagram")
        self.horizontalLayout_3.addWidget(self.Instagram)
        self.LinkedIn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LinkedIn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(17)
        self.LinkedIn.setFont(font)
        self.LinkedIn.setObjectName("LinkedIn")
        self.horizontalLayout_3.addWidget(self.LinkedIn)
        self.Youtube = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Youtube.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(17)
        self.Youtube.setFont(font)
        self.Youtube.setObjectName("Youtube")
        self.horizontalLayout_3.addWidget(self.Youtube)
        self.Github = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Github.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(17)
        self.Github.setFont(font)
        self.Github.setObjectName("Github")
        self.horizontalLayout_3.addWidget(self.Github)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.Home)
        self.GUI_page = QtWidgets.QWidget()
        self.GUI_page.setObjectName("GUI_page")
        self.Gui_Name = QtWidgets.QLineEdit(self.GUI_page)
        self.Gui_Name.setGeometry(QtCore.QRect(70, 30, 200, 40))
        font = QtGui.QFont()
        font.setKerning(False)
        self.Gui_Name.setFont(font)
        self.Gui_Name.setMouseTracking(False)
        self.Gui_Name.setAcceptDrops(False)
        self.Gui_Name.setWhatsThis("Name of GUI Project File")
        self.Gui_Name.setStyleSheet("")
        self.Gui_Name.setText("")
        self.Gui_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Gui_Name.setClearButtonEnabled(True)
        self.Gui_Name.setObjectName("Gui_Name")
        self.GLabel = QtWidgets.QLabel(self.GUI_page)
        self.GLabel.setGeometry(QtCore.QRect(70, 70, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.GLabel.setFont(font)
        self.GLabel.setObjectName("GLabel")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.GUI_page)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 170, 333, 91))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.GInfo = QtWidgets.QLabel(self.GUI_page)
        self.GInfo.setGeometry(QtCore.QRect(20, 100, 291, 61))
        self.GInfo.setWordWrap(True)
        self.GInfo.setObjectName("GInfo")
        self.stackedWidget.addWidget(self.GUI_page)
        self.Scraping_page = QtWidgets.QWidget()
        self.Scraping_page.setObjectName("Scraping_page")
        self.Scraping_Name = QtWidgets.QLineEdit(self.Scraping_page)
        self.Scraping_Name.setGeometry(QtCore.QRect(65, 30, 200, 40))
        self.Scraping_Name.setStyleSheet("")
        self.Scraping_Name.setText("")
        self.Scraping_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Scraping_Name.setClearButtonEnabled(True)
        self.Scraping_Name.setObjectName("Scraping_Name")
        self.SLabel = QtWidgets.QLabel(self.Scraping_page)
        self.SLabel.setGeometry(QtCore.QRect(70, 70, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.SLabel.setFont(font)
        self.SLabel.setObjectName("SLabel")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.Scraping_page)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 200, 335, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(102, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_7)
        self.checkBox_1.setMaximumSize(QtCore.QSize(155, 20))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setTristate(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_3.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_7)
        self.checkBox_2.setMaximumSize(QtCore.QSize(155, 20))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.SInfo = QtWidgets.QLabel(self.Scraping_page)
        self.SInfo.setGeometry(QtCore.QRect(20, 100, 290, 81))
        self.SInfo.setWordWrap(True)
        self.SInfo.setObjectName("SInfo")
        self.stackedWidget.addWidget(self.Scraping_page)
        self.Normal_page = QtWidgets.QWidget()
        self.Normal_page.setObjectName("Normal_page")
        self.Normal_Name = QtWidgets.QLineEdit(self.Normal_page)
        self.Normal_Name.setGeometry(QtCore.QRect(70, 30, 200, 40))
        self.Normal_Name.setStyleSheet("")
        self.Normal_Name.setText("")
        self.Normal_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Normal_Name.setClearButtonEnabled(True)
        self.Normal_Name.setObjectName("Normal_Name")
        self.NLabel = QtWidgets.QLabel(self.Normal_page)
        self.NLabel.setGeometry(QtCore.QRect(70, 70, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.NLabel.setFont(font)
        self.NLabel.setObjectName("NLabel")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.Normal_page)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 190, 333, 82))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        self.checkBox_3.setMaximumSize(QtCore.QSize(155, 20))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        self.checkBox_4.setMaximumSize(QtCore.QSize(155, 20))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setTristate(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.NInfo = QtWidgets.QLabel(self.Normal_page)
        self.NInfo.setGeometry(QtCore.QRect(20, 100, 291, 61))
        self.NInfo.setWordWrap(True)
        self.NInfo.setObjectName("NInfo")
        self.stackedWidget.addWidget(self.Normal_page)
        self.Convert_page = QtWidgets.QWidget()
        self.Convert_page.setObjectName("Convert_page")
        self.ui_btn = QtWidgets.QPushButton(self.Convert_page)
        self.ui_btn.setGeometry(QtCore.QRect(90, 210, 150, 28))
        self.ui_btn.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ui_btn.setFont(font)
        self.ui_btn.setFlat(False)
        self.ui_btn.setObjectName("ui_btn")
        self.qrc_btn = QtWidgets.QPushButton(self.Convert_page)
        self.qrc_btn.setGeometry(QtCore.QRect(90, 250, 150, 28))
        self.qrc_btn.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.qrc_btn.setFont(font)
        self.qrc_btn.setFlat(False)
        self.qrc_btn.setObjectName("qrc_btn")
        self.Error = QtWidgets.QLabel(self.Convert_page)
        self.Error.setGeometry(QtCore.QRect(70, 20, 200, 21))
        self.Error.setText("")
        self.Error.setObjectName("Error")
        self.status_convert = QtWidgets.QLabel(self.Convert_page)
        self.status_convert.setGeometry(QtCore.QRect(90, 150, 151, 31))
        self.status_convert.setText("")
        self.status_convert.setAlignment(QtCore.Qt.AlignCenter)
        self.status_convert.setObjectName("status_convert")
        self.Information = QtWidgets.QLabel(self.Convert_page)
        self.Information.setGeometry(QtCore.QRect(20, 10, 291, 141))
        self.Information.setWordWrap(True)
        self.Information.setObjectName("Information")
        self.stackedWidget.addWidget(self.Convert_page)
        self.Closed = QtWidgets.QPushButton(self.MainFrame)
        self.Closed.setGeometry(QtCore.QRect(323, 6, 20, 20))
        self.Closed.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Closed.setFont(font)
        self.Closed.setObjectName("Closed")
        self.Python = QtWidgets.QLabel(self.MainFrame)
        self.Python.setGeometry(QtCore.QRect(0, 19, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(11)
        self.Python.setFont(font)
        self.Python.setAlignment(QtCore.Qt.AlignCenter)
        self.Python.setObjectName("Python")
        self.status = QtWidgets.QLabel(self.MainFrame)
        self.status.setGeometry(QtCore.QRect(0, 446, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(8)
        self.status.setFont(font)
        self.status.setLineWidth(0)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.Select_Home = QtWidgets.QPushButton(self.MainFrame)
        self.Select_Home.setGeometry(QtCore.QRect(30, 15, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(11)
        self.Select_Home.setFont(font)
        self.Select_Home.setObjectName("Select_Home")
        self.Background_shadow.raise_()
        self.Title.raise_()
        self.Shadow.raise_()
        self.frame.raise_()
        self.Closed.raise_()
        self.Python.raise_()
        self.status.raise_()
        self.Select_Home.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Shadow.setText(_translate("MainWindow", "Project Creator"))
        self.Title.setText(_translate("MainWindow", "Project Creator"))
        self.label.setText(_translate("MainWindow", "Choose Project Type"))
        self.label_2.setText(_translate("MainWindow", "Follow me on"))
        self.GUI_btn.setText(_translate("MainWindow", "GUI Project"))
        self.Scraping_btn.setText(_translate("MainWindow", "Webscraping Project"))
        self.Norm_btn.setText(_translate("MainWindow", "Normal Project"))
        self.Project_btn.setText(_translate("MainWindow", "Change Project Directory"))
        self.Facebook.setText(_translate("MainWindow", "E"))
        self.Instagram.setText(_translate("MainWindow", "Q"))
        self.LinkedIn.setText(_translate("MainWindow", "C"))
        self.Youtube.setText(_translate("MainWindow", "M"))
        self.Github.setText(_translate("MainWindow", ")"))
        self.Gui_Name.setPlaceholderText(_translate("MainWindow", "Name of Project"))
        self.GLabel.setText(_translate("MainWindow", "Name of UI Project"))
        self.pushButton_3.setText(_translate("MainWindow", "Open Project Template"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert ui or qrc to py"))
        self.pushButton.setText(_translate("MainWindow", "Run Project Code"))
        self.GInfo.setText(_translate("MainWindow", "<html><head/><body><p>This section creates a pyqt5 python file and it\'s ui file. It also contains options to convert the ui file or qrc file to py so you can easily import it into your program. <br/>See Help for more Information</p></body></html>"))
        self.Scraping_Name.setWhatsThis(_translate("MainWindow", "Webscraping Project File"))
        self.Scraping_Name.setPlaceholderText(_translate("MainWindow", "Name of Project"))
        self.SLabel.setText(_translate("MainWindow", "Name of Webscraping Project"))
        self.checkBox_1.setText(_translate("MainWindow", "Using Requests"))
        self.checkBox_2.setText(_translate("MainWindow", "Using Selenium"))
        self.SInfo.setText(_translate("MainWindow", "<html><head/><body><p>This section creates a webscraping python file. It includes requests headers and sessions.<br/>Using the selenium method would create a folder and necessary information for this scraping method</p><p>See Help for more Information</p></body></html>"))
        self.Normal_Name.setWhatsThis(_translate("MainWindow", "Normal Project Files"))
        self.Normal_Name.setPlaceholderText(_translate("MainWindow", "Name of Project"))
        self.NLabel.setText(_translate("MainWindow", "Name of Normal Project"))
        self.checkBox_3.setText(_translate("MainWindow", "Include Function"))
        self.checkBox_4.setText(_translate("MainWindow", "Include Class"))
        self.NInfo.setText(_translate("MainWindow", "This just creates a python file and you can start your project right away"))
        self.ui_btn.setText(_translate("MainWindow", "Convert ui to py"))
        self.qrc_btn.setText(_translate("MainWindow", "Convert qrc to py"))
        self.Information.setText(_translate("MainWindow", "<html><head/><body><p>Using these Functions below can greatly help with converting your UI files and QRC files to py if you want to distribute ur application.<br/><br/>Please when converting qrc . Have your images/Icons in same folder</p></body></html>"))
        self.Closed.setText(_translate("MainWindow", "X"))
        self.Python.setText(_translate("MainWindow", "P y t h o n"))
        self.status.setText(_translate("MainWindow", "test"))
        self.Select_Home.setText(_translate("MainWindow", "P y t h o n"))
import Background


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
