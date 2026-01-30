

def calculateNetCarbonEmmisions(products):


    #region <Avoided Emissions>
    avoidedEmissions = sum(product.amount * product.averageAvoidedEmmisions for product in products)
    #endregion

    #region <Additional Emissions>
    emissionsFromExtraTransport = sum(product.amount * product.averageTransportEmmissions for product in products)
    emissionsFromExtraStorage = sum(product.amount * product.averageStorageEmmissions for product in products)
    emissionsFromConsumerPickup = 0 # Assume negligable for now

    additionalEmissions = emissionsFromExtraTransport + emissionsFromExtraStorage + emissionsFromConsumerPickup
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
    averageAvoidedEmisions (kg CO2 per kg)
    averageStorageEmissions (kg CO2 per kg)
    averageTransportEmissions (kg CO2 per kg)
    """
    def __init__(self, name, amount, averageAvoidedEmissions, averageStorageEmissions, averageTransportEmissions):
        self.name = name
        self.amount = amount
        self.averageAvoidedEmissions = averageAvoidedEmissions
        self.averageStorageEmissions = averageStorageEmissions
        self.averageTransportEmissions = averageTransportEmissions

    def __repr__(self):
        return f"{self.name}"