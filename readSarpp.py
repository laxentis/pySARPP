import csv
import os

class SARPPreader:
    """ Reading SARPP data
        Column order:
            Time, Height, IAS, G_v, G_h, RPM, AoA, Hyd_m, Hyd_b, SAU, Fors, Trigger
    """
    def __init__(self,filename):
        try:
            if not os.stat(filename).st_size > 0:
                raise Exception("File empty")
            else:
                if self.__validateFile(filename):
                    f = open(filename)
                    self.data = list()
                    self.__read(f)
                else:
                    raise Exception("Invalid file syntax")
        except OSError:
            raise OSError("File not found")

    def __validateFile(self, filename):
        f = open(filename)
        fline = f.readline()
        f.close()
        pfline = 'Time\t\tH (m)\t\tIAS (km/h)\tG_vert \t\tG_horiz \tRPM \t\tAoA \t\tHydro_m \tHydro_b \tSAU \t\tFors \t\tTrigger \n'
        if fline == pfline:
            return True
        else:
            return False

    def getColumn(self, col):
        ret = list()
        for line in self.data:
            ret.append(line[col])
        return ret

    def getTimes(self):
        return self.getColumn(0)

    def getHeights(self):
        return self.getColumn(1)

    def getIAS(self):
        return self.getColumn(2)

    def getGv(self):
        return self.getColumn(3)

    def getGh(self):
        return self.getColumn(4)

    def getRPM(self):
        return self.getColumn(5)

    def getAoA(self):
        return self.getColumn(6)

    def getHydm(self):
        return self.getColumn(7)

    def getHydb(self):
        return self.getColumn(8)

    def getSAU(self):
        return self.getColumn(9)

    def getFors(self):
        return self.getColumn(10)

    def getTrigger(self):
        return self.getColumn(11)
        
    def __read(self, f):
        r = csv.reader(f, delimiter = '\t')
        for row in r:
            self.__validateRow(row)

    def __validateRow(self, row):
        if row[0] != 'Time':
            row.pop() # Popping last element to remove the unnecessary empty element
            row = [float(i) for i in row] # turn to floats
            self.data.append(row)

