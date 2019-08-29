from Site import Site

class Grid:

    def __init__(self, n):
        self.n = n

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
        for step in [-1,1]:
            neighbor = Site(site.getRow() + step, site.getCol())
            if self.contains(neighbor):
                neighbors.append(neighbor)
            
            neighbor = Site(site.getRow(), site.getCol() + step)
            if self.contains(neighbor):
                neighbors.append(neighbor)
        
        return neighbors