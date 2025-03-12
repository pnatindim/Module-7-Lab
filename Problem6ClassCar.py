# Patric Natindim
# March 12 2025

# Problem 6: Prints attributes of a car

class car:
    def __init__(self, model, year, color, miles, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.miles = miles
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_miles(self):
        return self.miles

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return (self.model + ' ' +
                str(self.year) + ' ' +
                self.color + ' ' +
                self.miles + ' ' +
                self.manufacturer)

car1 = car("Sports", 2012, "Blue", "50,000 miles", "Toyota")
car2 = car("Sedan", 2020, "Black", "110,000 miles", "Honda")

print(car1.get_color())        
print(car1.get_model())        
print(car2.get_color())        
print(car1.fullspecs())        
print(car2.fullspecs())        
