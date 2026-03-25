

from Class.class9 import Car, Race
import random

cars = [Car(f"ABC-{i}", random.randint(100,200)) for i in range(1,11)]

race = Race("Grand Demolition Derby", 8000, cars)
hours = 0

while not race.race_finished():
    
    race.hour_passes()
    hours += 1
    if hours %10 == 0:
        print("----------------------STATUS-------------------------")
        race.print_status()
    
print("Race Finished!")
race.race_finished()
