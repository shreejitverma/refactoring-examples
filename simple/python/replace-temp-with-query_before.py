def calculateTotal():
    basePrice = quantity * itemPrice
    return basePrice * 0.95 if basePrice > 1000 else basePrice * 0.98