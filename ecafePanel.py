from PyQt5 import QtCore, QtGui, QtWidgets
from ecafeDb import topSelling, leastSelling, dateAndTime


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(467, 315)
        Main.setStyleSheet("QMainWindow {\n"
                           "color: \n"
                           "    color: rgb(255, 146, 232);\n"
                           "\n"
                           "}")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "background-color: \n"
                                         "    color: rgb(147, 255, 101);\n"
                                         "\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.Least = QtWidgets.QPushButton(self.centralwidget)
        self.Least.setGeometry(QtCore.QRect(190, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.Least.setFont(font)
        self.Least.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Least.setStyleSheet("QPushButton {\n"
                                 "border-radius: 25px;\n"
                                 "color: white;\n"
                                 "    background-color: rgb(34, 34, 91);\n"
                                 "}")
        self.Least.setObjectName("Least")
        self.Top = QtWidgets.QPushButton(self.centralwidget)
        self.Top.setGeometry(QtCore.QRect(40, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.Top.setFont(font)
        self.Top.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Top.setStyleSheet("QPushButton {\n"
                               "border-radius: 25px;\n"
                               "color: white;\n"
                               "    background-color: rgb(34, 34, 91);\n"
                               "}")
        self.Top.setObjectName("Top")
        self.Time = QtWidgets.QPushButton(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(340, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.Time.setFont(font)
        self.Time.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Time.setStyleSheet("QPushButton {\n"
                                "border-radius: 25px;\n"
                                "color: white;\n"
                                "    background-color: rgb(34, 34, 91);\n"
                                "}")
        self.Time.setObjectName("Time")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 20, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setScaledContents(False)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 120, 391, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 160, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 230, 91, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(190, 230, 91, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(340, 230, 91, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.Top.clicked.connect(topSelling)
        self.Least.clicked.connect(leastSelling)
        self.Time.clicked.connect(dateAndTime)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Panel"))
        self.Least.setText(_translate("Main", "LEAST SELLING"))
        self.Top.setText(_translate("Main", "TOP SELLING"))
        self.Time.setText(_translate("Main", "ACTIVE TIME"))
        self.title.setText(_translate("Main", "TUPC E-CAFETERIA"))
        self.label.setText(_translate("Main", "Requirement 1"))
        self.label_2.setText(_translate("Main", "Control panel"))
        self.label_3.setText(_translate("Main", "Requirement 2"))
        self.label_4.setText(_translate("Main", "Requirement 3"))
        self.label_5.setText(_translate(
            "Main", "Press buttons to show output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
