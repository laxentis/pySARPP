from makePlots import *
import sys
from PyQt4 import QtCore, QtGui
from dialog import Ui_Dialog
class GUI(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.plotter = None
        QtCore.QObject.connect(self.ui.generateAllButton, QtCore.SIGNAL("clicked()"), self.generateAll)
        QtCore.QObject.connect(self.ui.generateButton, QtCore.SIGNAL("clicked()"), self.generate)

    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.ui.filename.setText(fname)

    def generate(self):
        self.openFile()
        self.plotter = SARPPplot(self.ui.filename.text())
        if self.ui.height.checkState() == 2:
            self.plotter.plotHeight()
        if self.ui.ias.checkState() == 2:
            self.plotter.plotIAS()
        if self.ui.rpm.checkState() == 2:
            self.plotter.plotRPM()
        if self.ui.fors.checkState() == 2:
            self.plotter.plotFors()
        if self.ui.aoa.checkState() == 2:
            self.plotter.plotAoA()
        if self.ui.sau.checkState() == 2:
            self.plotter.plotSAU()
        if self.ui.trigger.checkState() == 2:
            self.plotter.plotTrigger()
        if self.ui.g.checkState() == 2:
            self.plotter.plotGs()
        if self.ui.hyd.checkState() == 2:
            self.plotter.plotHyd()

    def generateAll(self):
        self.openFile()
        self.plotter = SARPPplot(self.ui.filename.text())
        self.plotter.plotAll()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
