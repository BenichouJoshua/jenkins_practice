
from vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand, model, year, mileage = 0):
        Vehicle.__init__(self, brand, model, year, mileage)

    def GetType(self):
        return "Boat"

    def Move(self, distance):
        Vehicle.Move(self, distance)
        print(f"Sailing {distance} km!")    