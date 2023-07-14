class Manufacturer():
    brands = []
    def __init__(self, name, locations):
        self.name = name
        self.locations = locations
        # self.brands = []
    def add_brand(self, brand):
        self.brands.append(brand)
    def get_brands(self):
        print('name:',self.name)
        print('locations:',self.locations)
        print('brand:',self.brands)
class Car():
        def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year
        def get_details(self):
            print('car brand is:',self.brand)
            print('car model is:',self.model)
            print('car manufacturing year is:',self.year)

a = Manufacturer('x','y')
a.add_brand('kia')
a.get_brands()
b = Manufacturer('m','n')
b.add_brand('honda')
b.get_brands()
c = Car('bmw','p',1900)
c1 = Car('thar','q',1975)
c2 = Car('audi','r',1968)
c.get_details()
c1.get_details()
c2.get_details()

# where 'x' and 'm' are the name of the manufacturer.
# where 'y' and 'n' are the location of the manufacturer.
# where 'p','q' and 'r' are the models of the car.