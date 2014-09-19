# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Fri Sep 19 18:50:13 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 250, 411, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.filename = QtGui.QLineEdit(Dialog)
        self.filename.setGeometry(QtCore.QRect(70, 10, 301, 20))
        self.filename.setObjectName(_fromUtf8("filename"))
        self.plots = QtGui.QGroupBox(Dialog)
        self.plots.setGeometry(QtCore.QRect(10, 30, 371, 211))
        self.plots.setObjectName(_fromUtf8("plots"))
        self.checkboxes = QtGui.QSplitter(self.plots)
        self.checkboxes.setGeometry(QtCore.QRect(20, 20, 76, 171))
        self.checkboxes.setOrientation(QtCore.Qt.Vertical)
        self.checkboxes.setObjectName(_fromUtf8("checkboxes"))
        self.height = QtGui.QCheckBox(self.checkboxes)
        self.height.setObjectName(_fromUtf8("height"))
        self.ias = QtGui.QCheckBox(self.checkboxes)
        self.ias.setObjectName(_fromUtf8("ias"))
        self.aoa = QtGui.QCheckBox(self.checkboxes)
        self.aoa.setObjectName(_fromUtf8("aoa"))
        self.rpm = QtGui.QCheckBox(self.checkboxes)
        self.rpm.setObjectName(_fromUtf8("rpm"))
        self.sau = QtGui.QCheckBox(self.checkboxes)
        self.sau.setObjectName(_fromUtf8("sau"))
        self.fors = QtGui.QCheckBox(self.checkboxes)
        self.fors.setObjectName(_fromUtf8("fors"))
        self.trigger = QtGui.QCheckBox(self.checkboxes)
        self.trigger.setObjectName(_fromUtf8("trigger"))
        self.g = QtGui.QCheckBox(self.checkboxes)
        self.g.setObjectName(_fromUtf8("g"))
        self.hyd = QtGui.QCheckBox(self.checkboxes)
        self.hyd.setObjectName(_fromUtf8("hyd"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 270, 371, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.generateButton = QtGui.QPushButton(self.splitter)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.generateAllButton = QtGui.QPushButton(self.splitter)
        self.generateAllButton.setObjectName(_fromUtf8("generateAllButton"))
        self.closeButton = QtGui.QPushButton(self.splitter)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "pySARPP", None))
        self.label.setText(_translate("Dialog", "Filename:", None))
        self.plots.setTitle(_translate("Dialog", "Plots", None))
        self.height.setText(_translate("Dialog", "Height", None))
        self.ias.setText(_translate("Dialog", "IAS", None))
        self.aoa.setText(_translate("Dialog", "AoA", None))
        self.rpm.setText(_translate("Dialog", "RPM", None))
        self.sau.setText(_translate("Dialog", "SAU", None))
        self.fors.setText(_translate("Dialog", "Fors", None))
        self.trigger.setText(_translate("Dialog", "Trigger", None))
        self.g.setText(_translate("Dialog", "G", None))
        self.hyd.setText(_translate("Dialog", "Hydraulics", None))
        self.generateButton.setText(_translate("Dialog", "Generate", None))
        self.generateAllButton.setText(_translate("Dialog", "Generate all", None))
        self.closeButton.setText(_translate("Dialog", "Close", None))

