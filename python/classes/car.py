from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, mileage = 0):
        Vehicle.__init__(self, brand, model, year, mileage)
    
    def GetType(self):
        return "Car"
    
    def Move(self, distance):
        Vehicle.Move(self, distance)
        print(f"Driving {distance} km!")          
