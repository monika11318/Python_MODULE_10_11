import random, tabulate

class Car:
    def __init__(self, reg_num, max_speed, cur_speed=0, distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.distance = distance

    def acclerate(self, change_speed):
        self.cur_speed += change_speed
        if self.cur_speed < 0:
            self.cur_speed = 0
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed

    def drive(self, hour):
        self.distance += self.cur_speed * hour

    def get_info(self):
        return {
            "reg_num": self.reg_num,
            "max_speed": self.max_speed,
            "cur_speed": self.cur_speed,
            "distance": self.distance
        }
    
    

class Race:
    def __init__(self, name, distance_KM, cars):
        self.name = name
        self.distance_KM = distance_KM
        self.cars = cars
    
    def hour_passes(self):
        for car in self.cars:
            car.acclerate(random.randint(-10,15))
            car.drive(1)

    def print_status(self):
        printable_cars = []
        for car in self.cars:
            printable_cars.append(car.get_info())
        table = tabulate.tabulate(printable_cars, headers="keys", tablefmt="fancy_grid")
        print(table)

    def race_finished(self):
        return any (car.distance >= self.distance_KM for car in self.cars)
        

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, capacityKWH):
        Car.__init__(self,reg_num, max_speed)
        self.capacity_KWH = capacityKWH


class GasolineCar(Car):
    def __init__(self,reg_num, max_speed, volume_L):
        Car.__init__(self,reg_num, max_speed)
        self.volume_L = volume_L
