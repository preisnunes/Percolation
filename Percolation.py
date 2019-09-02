import math
from WeightedQuickUnion import WeightedQuickUnion
from Site import Site
from Grid import Grid

class Percolation:

    def __init__(self, n :int, quickUnionAlgo):
        self.grid = Grid(n)
        allSites = n*n + 2
        self.sitesOpened = [False for i in range(0, allSites)]
        self.algo = quickUnionAlgo
        self.algo.setUp(allSites)

    def open(self, row :int, col :int):
        site = Site(row, col)
        site1DCoordinates = self.grid.convertToSite1DCoordinates(site)
        
        if self.sitesOpened[site1DCoordinates]:
            return
        
        self.sitesOpened[site1DCoordinates] = True
        
        for neighbor in self.grid.retrieveSiteNeighbors(site):
            neighbor1DCoords = self.grid.convertToSite1DCoordinates(neighbor)
            if not self.sitesOpened[neighbor1DCoords]:
                continue
            self.algo.union(site1DCoordinates, neighbor1DCoords)

        if row == 1:
            self.algo.union(site1DCoordinates, 0)

        if row == self.grid.getN():
            self.algo.union(site1DCoordinates, int(math.pow(self.grid.getN(), 2)) + 1)

    def isOpen(self, row :int, col :int) ->bool:
        return self.sitesOpened[self.grid.convertToSite1DCoordinates(Site(row, col))]

    def numberOfOpenSites(self) ->int:
        return self.sitesOpened.count(True)

    def isFull(self, row :int, col :int) ->bool:
        site1DCoordinates = self.grid.convertToSite1DCoordinates(Site(row, col))
        return self.algo.connected(site1DCoordinates, 0)
        
    def percolates(self):
        return self.algo.connected(int(math.pow(self.grid.getN(), 2)) + 1, 0)
