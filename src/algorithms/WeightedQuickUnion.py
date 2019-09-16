from algorithms.Abstract import Abstract

class WeightedQuickUnion(Abstract):

    def __init__(self, numberOfItems :int = 0):
        self.setNumberOfItems(numberOfItems)

    def getConnectivity(self):
        return self.connectivity

    def setNumberOfItems(self, numberOfItems :int = 0):
        self.numberOfItems = numberOfItems
        self.connectivity = [i for i in range(0, numberOfItems)]
        self.treeSize = [1 for i  in range(0, numberOfItems)]

    def root(self, elementIndex):
        while self.connectivity[elementIndex] != elementIndex:
            elementIndex = self.connectivity[elementIndex]
        return elementIndex

    def connected(self, p :int, q :int):
        return self.root(p) == self.root(q)

    def union(self, p :int, q :int):
        
        pRoot = self.root(p)
        qRoot = self.root(q)
        if pRoot == qRoot:
            return
        
        pRootSize = self.treeSize[p]
        qRootSize = self.treeSize[q]
        
        if pRootSize < qRootSize:
            self.connectivity[pRoot] = qRoot
            self.treeSize[qRoot] += self.treeSize[pRoot]
        else:
            self.connectivity[qRoot] = pRoot
            self.treeSize[pRoot] += self.treeSize[qRoot]


