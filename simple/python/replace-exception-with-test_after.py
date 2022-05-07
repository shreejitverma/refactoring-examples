def getValueForPeriod(self, periodNumber):
    return 0 if periodNumber >= len(self.values) else self.values[periodNumber]