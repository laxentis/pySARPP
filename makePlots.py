from readSarpp import SARPPreader
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class SARPPplot:
    def __init__(self, filename):
        self.__f = filename
        self.r = SARPPreader(filename)

    def plotAll(self):
        self.plotRPM()
        self.plotHeight()
        self.plotAoA()
        self.plotIAS()
        self.plotSAU()
        self.plotFors()
        self.plotTrigger()
        self.plotGs()
        self.plotHyd()

    def plotHeight(self):
        self.__makePlot(self.r.getHeights(), "Height", "Height [m]")

    def plotAoA(self):
        self.__makePlot(self.r.getAoA(), "AoA", "AoA [degrees]")

    def plotRPM(self):
        self.__makePlot(self.r.getRPM(), "RPM", "RPM [%]")

    def plotIAS(self):
        self.__makePlot(self.r.getIAS(), "IAS", "IAS [km/h")

    def plotSAU(self):
        self.__makePlot(self.r.getSAU(), "SAU", "SAU state")

    def plotFors(self):
        self.__makePlot(self.r.getFors(), "Fors", "Fors")

    def plotTrigger(self):
        self.__makePlot(self.r.getTrigger(), "Trigger", "Trigger")

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

    def __makePlot(self, y, name, ylabel):
        plt.plot(self.r.getTimes(), y)
        plt.xlabel("Time [s]")
        plt.ylabel(ylabel)
        plt.savefig(self.__f + '-' + name + '.png')
        plt.clf()
