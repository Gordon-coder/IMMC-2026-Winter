from netCarbonEmissions import *
from csv import reader

#region <Load product data from CSV>
products = []
with open("./emissionData.csv", 'r') as file:
    csvReader = reader(file)
    next(csvReader)  # Skip header
    for row in csvReader:
        name = row[0]
        amount = float(row[1])
        averageAvoidedEmissions = float(row[2])
        averageStorageEmissions = float(row[3])
        product = Product(name, amount, averageAvoidedEmissions, averageStorageEmissions)
        products.append(product)
#endregion

netCarbonReduction = calculateNetCarbonEmmisions(products, 0.9)
print(f"Net Carbon Reduction: {netCarbonReduction} kg CO2")