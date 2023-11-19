#-1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name of Book: {self.name}")
        print(f"Author of Book: {self.author}")
        print(f"Page_count of Book: {self.page_count} pages.")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Name of Magazine: {self.name}")
        print(f"Chief Editor of magazine: {self.chief_editor}")


Compartment_no_6 = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)
Donald_Duck = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")

print("-.-" * 12)
Compartment_no_6.print_information()
print("-.-" * 12)
Donald_Duck.print_information()
print("-.-" * 12)

# -2


class Car:
    def __init__(self,reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.km_counter = 0

    def drive(self, hours):
        self.km_counter += hours * self.max_speed


class ElectricCar(Car):
    def __init__(self,reg_no, max_speed, battery_cap):
        super().__init__(reg_no, max_speed)
        self.battery_cap = battery_cap


class GasolineCar(Car):
    def __init__(self, reg_no, max_speed, volume_tank):
        super().__init__(reg_no,max_speed)
        self.volume_tank = volume_tank


electric_car = ElectricCar("ABC-15",180,52.5)
gasoline_car = GasolineCar("ACD-123",165,32.3)

electric_car.drive(3)
gasoline_car.drive(3)

print("-.-" * 15)
print(f"Electric Car Kilometer Counter: {electric_car.km_counter} km")
print(f"Gasoline Car Kilometer Counter: {gasoline_car.km_counter} km")
print("-.-" * 15)