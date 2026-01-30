def calculateNetCarbonEmmisions(products, totalTransportDistance=0, averageTransportEmissionsPerKm=0):
    #region <Avoided Emissions>
    avoidedEmissions = sum(product.amount * product.averageAvoidedEmissions for product in products)
    #endregion

    #region <Additional Emissions>
    emissionsFromExtraTransport = totalTransportDistance * averageTransportEmissionsPerKm
    emissionsFromExtraStorage = sum(product.amount * product.averageStorageEmissions for product in products)
    emissionsFromConsumerPickup = 0 # Assume negligable for now

    additionalEmissions = emissionsFromExtraTransport + emissionsFromExtraStorage + emissionsFromConsumerPickup
    #endregion

    netCarbonReduction = avoidedEmissions - additionalEmissions
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

