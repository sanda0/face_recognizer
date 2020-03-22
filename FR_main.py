# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FR_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import face_recon as fr

#new data set
class Ui_Form2(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(473, 405)
        Form.setMaximumSize(QtCore.QSize(473, 405))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.get_dataset = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.get_dataset.setFont(font)
        self.get_dataset.setObjectName("get_dataset")
        ##
        self.get_dataset.clicked.connect(self.get_data_set)
        ##
        self.gridLayout.addWidget(self.get_dataset, 4, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 3, 0, 1, 1)
        self.id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 2, 0, 1, 1)
        self.train_dataset = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.train_dataset.setFont(font)
        self.train_dataset.setObjectName("train_dataset")
        ##
        self.train_dataset.clicked.connect(self.train_data)
        ##
        self.gridLayout.addWidget(self.train_dataset, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
#get dataset
        
    def get_data_set(self):
        _id = self.id.text()
        _name = self.name.text()
        fr.data_set(_id,_name)
        #print(_id)
        

#trin
    def train_data(self):
        fr.train()
        
  

        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Train new dataset"))
        self.label.setText(_translate("Form", "Train New Dataset"))
        self.get_dataset.setText(_translate("Form", "Get Dataset"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Special Notice</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">first, click \'Get Dataset\' button and after stay few second (10 or 15 sec) in front of your camera.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">if you\'re done press \'q\' on your keyboard and click \'Train Dataset\' button.</span></p></body></html>"))
        self.name.setPlaceholderText(_translate("Form", "name"))
        self.id.setPlaceholderText(_translate("Form", "ID"))
        self.train_dataset.setText(_translate("Form", "Train Dataset"))


#main class

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 333)
        Form.setMaximumSize(QtCore.QSize(454, 333))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 411, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        ###
        self.pushButton_2.clicked.connect(self.new_dataset)
        
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.detect_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.detect_b.setFont(font)
        self.detect_b.setObjectName("detect_b")
        ###
        self.detect_b.clicked.connect(self.detect_f)

        self.gridLayout.addWidget(self.detect_b, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Facial Recongnition App[by sandakelum priyamantha]"))
        self.label.setText(_translate("Form", "Facial Recongnition App"))
        self.pushButton_2.setText(_translate("Form", "Train new data for new face"))
        self.label_2.setText(_translate("Form", "by sandakelum priyamantha"))
        self.detect_b.setText(_translate("Form", "Detect Faces"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">please press</span><span style=\" font-size:16pt; font-weight:600;\"> \'q\' </span><span style=\" font-size:16pt;\">on your keyboard exit from face detection window</span></p></body></html>"))

    def detect_f(self):
        print("detect")
        fr.detector()

    def new_dataset(self):
        print("ok")
        #import sys
        #app2 = QtWidgets.QApplication(sys.argv)
        self.Form2 = QtWidgets.QWidget()
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self.Form2)
        self.Form2.show()
        
        #sys.exit(app2.exec_())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

