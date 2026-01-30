

def calculateNetCarbonEmmisions(products):


    #region <Avoided Emissions>
    avoidedEmissions = sum(product.amount * product.averageAvoidedEmmisions for product in products)
    #endregion

    #region <Additional Emissions>
    emmissionsFromExtraTransport = sum(product.amount * product.averageTransportEmmissions for product in products)
    emmissionsFromExtraStorage = sum(product.amount * product.averageStorageEmmissions for product in products)
    emmissionsFromConsumerPickup = 0 # Assume negligable for now

    additionalEmissions = emmissionsFromExtraTransport + emmissionsFromExtraStorage + emmissionsFromConsumerPickup
    #endregion

    netCarbonReduction = avoidedEmissions - additionalEmissions
    return netCarbonReduction

class kgCO2:
    """
    Class to represent kilograms of CO2 emissions.
    """
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} kg CO2"
    
class Product:
    """
    amount (kg)
    averageAvoidedEmmisions (kg CO2 per kg)
    averageStorageEmmissions (kg CO2 per kg)
    averageTransportEmmissions (kg CO2 per kg)
    """
    def __init__(self, name, amount, averageAvoidedEmmisions, averageStorageEmmissions, averageTransportEmmissions):
        self.name = name
        self.amount = amount
        self.averageAvoidedEmmisions = averageAvoidedEmmisions
        self.averageStorageEmmissions = averageStorageEmmissions
        self.averageTransportEmmissions = averageTransportEmmissions

    def __repr__(self):
        return f"{self.name}"