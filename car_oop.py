class Car(object):
    
    def __init__(self, name = "General", model = "GM", car_type = "saloon"):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        if self.name.lower() == 'porshe' or self.name.lower() == 'koenigsegg':
            self.num_of_doors = 2
        if self.car_type.lower() == 'trailer':
            self.num_of_wheels = 8
    
    def is_saloon(self):
        if self.car_type.lower() != 'trailer':
            return 'saloon'
        return 'trailer'
        
    def drive(self, speed):
        if speed == 7 and self.car_type.lower() == "trailer":
            self.speed = 77
            return self
        elif speed == 3 and self.name.lower() == "mercedes":
            self.speed = 1000
            return self
        else:
            return "Your cars speed is not yet calculated"
