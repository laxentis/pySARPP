from readSarpp import SARPPreader
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class SARPPplot:
    def __init__(self, filename):
        self.__f = filename
        try:
            self.r = SARPPreader(filename)
        except FileNotFoundError:
            raise FileNotFoundError("Selected file was not found")
        except OSError:
            raise OSError("File not found")
        except Exception:
            raise Exception("Invalid file syntax")

    def plotHeight(self):
        self.__makePlot(self.r.getHeights(), "Height", "Height [m]")

    def plotHeightChange(self):
        h = self.r.getHeights()
        chg = []
        prev = 0
        for i in h:
            chg.append(i - prev)
            prev = i
        self.__makePlot(chg, "dH", "Vertical velocity [m/s]")

    def plotAoA(self):
        self.__makePlot(self.r.getAoA(), "AoA", "AoA [degrees]")

    def plotRPM(self):
        self.__makePlot(self.r.getRPM(), "RPM", "RPM [%]")

    def plotIAS(self):
        self.__makePlot(self.r.getIAS(), "IAS", "IAS [km/h]")

    def plotIASchange(self):
        ias = self.r.getIAS()
        chg = []
        prev = 0
        for i in ias:
            i = i / 3.6
            chg.append(i - prev)
            prev = i
        self.__makePlot(chg, "dV", "Acceleration [m/s^2]")

    def plotSAU(self):
        self.__makePlot(self.r.getSAU(), "SAU", "SAU state", True)

    def plotFors(self):
        self.__makePlot(self.r.getFors(), "Fors", "Fors", True)

    def plotTrigger(self):
        self.__makePlot(self.r.getTrigger(), "Trigger", "Trigger", True)

    def plotGs(self):
        plt.plot(self.r.getTimes(), self.r.getGv(), label="Vertical")
        plt.plot(self.r.getTimes(), self.r.getGh(), label="Horizontal")
        plt.xlabel("Time [s]")
        plt.ylabel("G")
        plt.legend()
        plt.savefig(self.__f + '-G.png')
        plt.clf()

    def plotHyd(self):
        plt.plot(self.r.getTimes(), self.r.getHydm(), label="Main")
        plt.plot(self.r.getTimes(), self.r.getHydb(), label="Backup")
        plt.xlabel("Time [s]")
        plt.ylabel("Hydraulics")
        plt.legend()
        plt.savefig(self.__f + '-Hydro.png')
        plt.clf()

    def __makePlot(self, y, name, ylabel, tristate=False):
        plt.plot(self.r.getTimes(), y)
        if tristate:
            x1,x2,y1,y2 = plt.axis()
            plt.axis((x1,x2,0,2.5))
        plt.xlabel("Time [s]")
        plt.ylabel(ylabel)
        plt.savefig(self.__f + '-' + name + '.png')
        plt.clf()
