import math

class Statistics:

    def __init__(self, values :list):
        self.values = values

    def getAverage(self):
        return sum(self.values)/len(self.values)
    
    def getSquareStdDeviation(self):
        average = self.getAverage()
        deviationSum = 0
        for fraction in self.values:
            deviationSum += (fraction-average)**2
        return deviationSum/(len(self.values)-1)

    def getHighConf(self):
        return self.getAverage() + 1.96 * math.sqrt(self.getSquareStdDeviation()/len(self.values))

    def getLowConf(self):
        return self.getAverage() - 1.96 * math.sqrt(self.getSquareStdDeviation()/len(self.values))

    def getConfInterval(self):
        return [self.getLowConf(), self.getHighConf()]

        