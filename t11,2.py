

from Class.class9 import *


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.acclerate(120)
gasoline_car.acclerate(100)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car's KM counter: {electric_car.distance} KM")
print(f"Gasoline car's KM counter: {gasoline_car.distance} KM")


