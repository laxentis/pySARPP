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
        fdial = QtGui.QFileDialog(self)
        fdial.setFilter("Text files (*.txt)")
        fname = fdial.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
        self.ui.filename.setText(fname)

    def generate(self):
        fname = self.openFile()
        if not self.ui.filename.text():
            return
        try:
            self.plotter = SARPPplot(self.ui.filename.text())
        except Exception:
            err = QtGui.QErrorMessage(self)
            err.showMessage("The specified file is not a correct SARPP file")
        except FileNotFoundError:
            err = QtGui.QErrorMessage(self)
            err.showMessage("The selected file was not found")
        else:
            pd = QtGui.QProgressDialog(self)
            pd.setRange(0, 9)
            pd.setLabelText("Generating plots")
            pd.open()
            if self.ui.height.checkState() == 2:
                self.plotter.plotHeight()
                pd.setValue(1)
            if self.ui.ias.checkState() == 2:
                self.plotter.plotIAS()
                pd.setValue(2)
            if self.ui.rpm.checkState() == 2:
                self.plotter.plotRPM()
                pd.setValue(3)
            if self.ui.fors.checkState() == 2:
                self.plotter.plotFors()
                pd.setValue(4)
            if self.ui.aoa.checkState() == 2:
                self.plotter.plotAoA()
                pd.setValue(5)
            if self.ui.sau.checkState() == 2:
                self.plotter.plotSAU()
                pd.setValue(6)
            if self.ui.trigger.checkState() == 2:
                self.plotter.plotTrigger()
                pd.setValue(7)
            if self.ui.g.checkState() == 2:
                self.plotter.plotGs()
                pd.setValue(8)
            if self.ui.hyd.checkState() == 2:
                self.plotter.plotHyd()
                pd.setValue(9)

    def generateAll(self):
        self.ui.height.setCheckState(2);
        self.ui.ias.setCheckState(2);
        self.ui.rpm.setCheckState(2);
        self.ui.fors.setCheckState(2);
        self.ui.aoa.setCheckState(2);
        self.ui.sau.setCheckState(2);
        self.ui.trigger.setCheckState(2);
        self.ui.g.setCheckState(2);
        self.ui.hyd.setCheckState(2);
        self.generate()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
