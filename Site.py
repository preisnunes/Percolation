class Site:
    def __init__(self, row :int, col :int):
        self.row = row
        self.col = col

    def validate(self, n :int) ->bool:
        if self.row < 1 or self.row > n:
            return False

        if self.col < 1 or self.col > n:
            return False

        return True

    def convertTo1D(self, n :int):
        return n * (self.row - 1) + self.col -1

    def getNeighbors(self, n:int) ->list: 
        neighbors = []
        for step in [-1,1]:
            neighbor = Site(self.row + step, self.col)
            if neighbor.validate(n):
                neighbors.append(neighbor)
            
            neighbor = Site(self.row, self.col + step)
            if neighbor.validate(n):
                neighbors.append(neighbor)
        
        return neighbors