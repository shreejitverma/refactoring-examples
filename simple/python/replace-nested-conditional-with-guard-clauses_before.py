def getPayAmount(self):
    if self.isDead:
        return deadAmount()
    elif self.isSeparated:
        return separatedAmount()
    else:
        return retiredAmount() if self.isRetired else normalPayAmount()