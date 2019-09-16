import math
from Site import Site
from Grid import Grid
from algorithms.Abstract import Abstract as QuickFindAbstract
from algorithms.WeightedQuickUnion import WeightedQuickUnion

class Percolation:

    def __init__(self, n :int, quickFindAlgorithm :QuickFindAbstract):
        self.grid = Grid(n)
        totalNumberOfSites = n*n + 2
        self.sitesOpened = [False for i in range(0, totalNumberOfSites)]
        quickFindAlgorithm.setNumberOfItems(totalNumberOfSites)
        self.setQuickFindAlgorithm(quickFindAlgorithm)

    def setQuickFindAlgorithm(self, quickFindAlgorithm :QuickFindAbstract):
        self.quickFindAlgorithm = quickFindAlgorithm

        
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
            self.quickFindAlgorithm.union(site1DCoordinates, neighbor1DCoords)

        if row == 1:
            self.quickFindAlgorithm.union(site1DCoordinates, 0)

        if row == self.grid.getN():
            self.quickFindAlgorithm.union(site1DCoordinates, int(math.pow(self.grid.getN(), 2)) + 1)

    def isOpen(self, row :int, col :int) ->bool:
        return self.sitesOpened[self.grid.convertToSite1DCoordinates(Site(row, col))]

    def numberOfOpenSites(self) ->int:
        return self.sitesOpened.count(True)

    def isFull(self, row :int, col :int) ->bool:
        site1DCoordinates = self.grid.convertToSite1DCoordinates(Site(row, col))
        return self.quickFindAlgorithm.connected(site1DCoordinates, 0)
        
    def percolates(self):
        return self.quickFindAlgorithm.connected(int(math.pow(self.grid.getN(), 2)) + 1, 0)
