class Car(object):
    
    def __init__(self, name = "General", model = "GM", car_type = "saloon"):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = 4
        self.num_of_wheels = 4
        if self.name.lower() == 'porshe' or self.name.lower() == 'koenigsegg':
            self.num_of_doors = 2
        if self.car_type.lower() == 'trailer':
            self.num_of_wheels = 8
    
    def is_saloon(self):
        if self.car_type.lower() != 'trailer':
            return True
        
porshe = Car('Porshe', '911 Turbo')
print porshe.is_saloon() ==True
 
