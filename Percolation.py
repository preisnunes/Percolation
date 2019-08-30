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
        siteCoordIn1D = self.grid.convertSiteTo1D(site)
        print('siteIndex: ' + str(siteCoordIn1D))
        
        if self.sitesOpened[siteCoordIn1D]:
            return
        
        self.sitesOpened[siteCoordIn1D] = True
        
        for neighbor in self.grid.retrieveSiteNeighbors(site):
            neighbor1DCoords = self.grid.convertSiteTo1D(neighbor)
            if not self.sitesOpened[neighbor1DCoords]:
                continue
            self.algo.union(siteCoordIn1D, neighbor1DCoords)

        if row == 1:
            self.algo.union(siteCoordIn1D, 0)

        if row == self.grid.getN():
            self.algo.union(siteCoordIn1D, math.pow(self.grid.getN(), 2) + 1)

    def isOpen(self, row :int, col :int) ->bool:
        site = Site(row, col)
        return self.sitesOpened[self.grid.convertSiteTo1D(site)]

    def numberOfOpenSites(self) ->int:
        return self.sitesOpened.count(True)

    def isFull(self, row :int, col :int) ->bool:
        siteCoordIn1D = self.grid.convertSiteTo1D(Site(row, col))
        return self.algo.connected(siteCoordIn1D, 0)
        
    def percolates(self):
        return self.algo.connected(math.pow(self.grid.getN(), 2) + 1, 0)
