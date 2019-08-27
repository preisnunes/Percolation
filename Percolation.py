from WeightedQuickUnion import WeightedQuickUnion
from Site import Site


class Percolation:

    def __init__(self, n :int, quickUnionAlgo):
        self.n = n
        numberOfGridItems = n*n
        self.grid = [False for i in range(0, numberOfGridItems)]
        self.algo = quickUnionAlgo
        self.algo.setVariables(numberOfGridItems)

    def open(self, row :int, col :int):
        site = Site(row, col)
        siteIndexIn1D = site.convertTo1D(self.n)
        if self.isOpenByIndexIn1D(siteIndexIn1D):
            return
        self.grid[siteIndexIn1D] = True
        
        for neighbor in site.getNeighbors(self.n):
            neighbor1DIndex = neighbor.convertTo1D(self.n)
            if not self.isOpenByIndexIn1D(neighbor1DIndex):
                continue
            self.algo.union(siteIndexIn1D, neighbor1DIndex)

    def isOpenByIndexIn1D(self, indexIn1D :int):
        return self.grid[indexIn1D]

    def isOpen(self, row :int, col :int) ->bool:
        site = Site(row, col)
        return self.grid[site.convertTo1D(self.n)]

    def numberOfOpenSites(self) ->int:
        return self.grid.count(True)

    def isFull(self, row :int, col :int) ->bool:
        isFull = False
        site = Site(row, col)
        siteIndexIn1D = site.convertTo1D(self.n)
        
        for i in range(1, self.n + 1):
            topRowSite = Site(1, i)
            if self.algo.connected(siteIndexIn1D, topRowSite.convertTo1D(self.n)):
                isFull = True
                break
        return isFull

    def percolates(self):
        for i in range(1, self.n + 1):
            if self.isFull(self.n, i):
                return True
        return False
