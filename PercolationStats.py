import random
import math
from Percolation import Percolation
from WeightedQuickUnion import WeightedQuickUnion

class PercolationStats:

    def __init__(self, n :int, trials :int, findUnionAlgorithm):
        self.n = n
        self.trials = trials
        self.trialsFraction = []
        self.findUnionAlgorithm = findUnionAlgorithm
        self.launchSimulations()
        

    def launchSimulations(self):

        for trial in range(self.trials):
            grid = Percolation(self.n, self.findUnionAlgorithm)
            while not grid.percolates():
                row = random.randint(1, self.n)
                col = random.randint(1, self.n)
                grid.open(row,col)
            self.trialsFraction.append(grid.numberOfOpenSites()/(self.n*self.n))

    def getAverage(self):
        return sum(self.trialsFraction)/len(self.trialsFraction)
    
    def getSquareStdDeviation(self):
        average = self.getAverage()
        deviationSum = 0
        for fraction in self.trialsFraction:
            deviationSum += (fraction-average)**2
        return deviationSum/(len(self.trialsFraction)-1)

    def getHighConf(self):
        return self.getAverage() + 1.96 * math.sqrt(self.getSquareStdDeviation()/len(self.trialsFraction))

    def getLowConf(self):
        return self.getAverage() - 1.96 * math.sqrt(self.getSquareStdDeviation()/len(self.trialsFraction))





percolationStats = PercolationStats(100,2, WeightedQuickUnion())
print(percolationStats.trialsFraction)
print(percolationStats.getAverage())
                

    

