class WeightedQuickUnion():

    def __init__(self, numberOfItems = 0):
        self.setVariables(numberOfItems)

    def setVariables(self, numberOfItems :int):
        self.numberOfItems = numberOfItems
        self.connectivity = [i for i in range(0, numberOfItems)]
        self.treeSize = [1 for i  in range(0, numberOfItems)]

    def getConnectivity(self):
        return self.connectivity

    def root(self, i):
        while self.connectivity[i] != i:
            i = self.connectivity[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        
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


