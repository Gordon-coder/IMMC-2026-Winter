def calculateNetCarbonEmmisions(products, avoidedFactor):
    netCarbonReduction = avoidedFactor * sum(product.amount * (product.averageAvoidedEmissions - product.averageStorageEmissions) for product in products)
    return netCarbonReduction


class Product:
    """
    amount (kg)
    averageAvoidedEmisions (kg CO2 per kg)
    averageStorageEmissions (kg CO2 per kg)
    """
    def __init__(self, name, amount, averageAvoidedEmissions, averageStorageEmissions):
        self.name = name
        self.amount = amount
        self.averageAvoidedEmissions = averageAvoidedEmissions
        self.averageStorageEmissions = averageStorageEmissions

    def __repr__(self):
        return f"{self.name}"

