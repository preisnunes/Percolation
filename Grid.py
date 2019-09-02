from Site import Site

class Grid:

    def __init__(self, n):
        self.n = n

    def getN(self) ->int:
        return self.n 

    def contains(self, site :Site) ->bool:
        row = site.getRow()
        if row < 1 or row > self.n:
            return False
        
        col = site.getCol()
        if col < 1 or col > self.n:
            return False

        return True

    def retrieveSiteNeighbors(self, site :Site) ->list:
        neighbors = []
        row = site.getRow()
        col = site.getCol()
        
        for step in [-1,1]:
            neighbor = Site(row + step, col)
            if self.contains(neighbor):
                neighbors.append(neighbor)
            
            neighbor = Site(row, col + step)
            if self.contains(neighbor):
                neighbors.append(neighbor)
        
        return neighbors

    def convertToSite1DCoordinates(self, site :Site):
        return self.n * (site.getRow() - 1) + site.getCol()

