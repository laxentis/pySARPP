from makePlots import *
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    plot = SARPPplot(filename)
    plot.plotAll()
