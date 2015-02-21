def CONST_MAXOFFSET = 7
def CONST_MINOFFSET = 3

class Window():
    def __init__(self, rowMin, rowMax, colMin, colMax, picShape):
        self.rowMin = rowMin - CONST_MINOFFSET
        self.rowMax = rowMax + CONST_MAXOFFSET
        self.colMin = colMin - CONST_MINOFFSET
        self.colMax = colMax + CONST_MAXOFFSET
        self.width = self.rowMax - self.rowMin
        self.height = self.colMax - self.colMin
        self.shape = picShape
        self.squareOff()
        self.checkBounds()

    def squareOff(self):
        if (self.width < self.height):
            #scale up width
            diff = self.height - self.width
            self.colMin = self.colMin - diff/2
            self.colMax = self.colMax + diff/2
            if (diff % 2 == 1):
                self.colMax = self.colMax + 1
            self.width = self.height
        elif (self.height < self.width):
            #scale up height
            diff = self.width - self.height
            self.rowMin = self.rowMin - diff/2
            self.rowMax = self.rowMax + diff/2
            if (diff % 2 == 1):
                self.rowMax = self.rowMax + 1
            self.height = self.width

    def checkBounds(self):
        if (self.rowMin < 0):
            offset =  0 - self.rowMin
            self.rowMin = 0
            self.rowMax = self.rowMax + offset
        if (self.colMin < 0):
            offset = 0 - self.colMin
            self.colMin = 0
            self.colMin = self.colMin + offset
        if (self.rowMax > self.shape[0]):
            offset = self.rowMax - self.shape[0]
            self.rowMax = self.shape[0]
            self.rowMin = self.rowMin - offset
        if (self.colMax > self.shape[1]):
            offset = self.colMax - self.shape[1]
            self.colMax = self.shape[1]
            self.colMin = self.colMin - offset
