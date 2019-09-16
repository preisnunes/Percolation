import random
import math
from Percolation import Percolation
from algorithms.WeightedQuickUnion import WeightedQuickUnion
from Statistics import Statistics
from algorithms.Abstract import Abstract as QuickFindAbstract

class PercolationStats:

    def __init__(self, gridSize :int, trials :int):
        self.gridSize = gridSize
        self.trials = trials
        self.statistic = Statistics([])
        
    def simulePercolation(self):
        trialsFraction = []
        for trial in range(self.trials):
            grid = Percolation(self.gridSize, WeightedQuickUnion())
            while not grid.percolates():
                row = random.randint(1, self.gridSize)
                col = random.randint(1, self.gridSize)
                grid.open(row,col)
            trialsFraction.append(grid.numberOfOpenSites()/(self.gridSize*self.gridSize))
        self.statistic = Statistics(trialsFraction)

    def getAverage(self):
        return self.statistic.getAverage()
    
    def getSquareStdDeviation(self):
        return math.sqrt(self.statistic.getSquareStdDeviation())

    def getHighConf(self):
        return self.statistic.getHighConf()

    def getLowConf(self):
        return self.statistic.getLowConf()

gridSize = 2   
trials = 10000

percolationSimulation = PercolationStats(gridSize, trials)
percolationSimulation.simulePercolation()
print('mean: ' + str(percolationSimulation.getAverage()))
print('stddev: ' + str(percolationSimulation.getSquareStdDeviation()))
print("95% confidence interval: " + '[' + str(percolationSimulation.getLowConf()) + ',' + str(percolationSimulation.getHighConf()) + ']')


                

    

