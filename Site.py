class Site:
    def __init__(self, row :int, col :int):
        self.row = row
        self.col = col

    def getRow(self) ->int:
        return self.row

    def getCol(self) ->int:
        return self.col

    def convertTo1D(self, n :int):
        return n * (self.row - 1) + self.col

   