
class Vehicle:
    def __init__(self, brand, model, year, mileage = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def GetType(self):
        return "Default"

    def Move(self, distance):
        self.mileage += distance

    def __str__(self):
        return f"Vehicle type: {self.GetType()}\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage}"