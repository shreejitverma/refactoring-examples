def calculateTotal():
    return basePrice() * 0.95 if basePrice() > 1000 else basePrice() * 0.98

def basePrice():
    return quantity * itemPrice