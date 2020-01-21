class Vehicle:
    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    def drive(self):
        return 'The vehicle drives down the road'

    def turn(self, direction):
        return f'The vehicle turns {direction}'

    def stop(self):
        return 'The vehicle stops'

class Car(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model, color)

    def drive(self):
        return f'The {self.color} {self.model} cruises down the road'

    def turn(self, direction):
        return f'The {self.model} turns {direction} smoothly'

    def stop(self):
        return f'The {self.model} eases to a stop'

class Truck(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model, color)

    def drive(self):
        return f'The {self.color} {self.model} barrels down the road'

G35 = Car('Infiniti', 'G35', 'black')
Supra = Car('Toyota', 'Supra', 'blue')
Civic = Car('Honda', 'Civic', 'burgandy')
Silverado = Truck('Chevrolette', 'Silverado', 'red')
F150 = Truck('Ford', 'F150', 'white')

vehicle_list = [G35, Supra, Civic, Silverado, F150]

for vehicle in vehicle_list:
    print(vehicle.drive())
    print(vehicle.turn("left"))
    print(vehicle.stop())