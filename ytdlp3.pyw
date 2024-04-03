
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 80))
        Form.setMaximumSize(QtCore.QSize(400, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(304, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.download)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 50, 291, 23))
        self.progressBar.setAccessibleDescription("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Youtube MP3"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Youtube address."))
        self.pushButton.setText(_translate("Form", "Download"))

    def download(self):
        link = self.lineEdit.text()
        cmd = "yt-dlp.exe -x " + link
        os.system(cmd)
        
        for i in range(101): 
        
            # slowing down the loop 
            time.sleep(0.01) 
            
            # setting value to progress bar 
            self.progressBar.setValue(i) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
