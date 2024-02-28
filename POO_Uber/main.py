from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola mundo")

    car1 = Car("AE628EA", Account("Peter33", "3456812", "Peter@gmail.com", "123456"))
    car1.printDataCar()

    car2 = Car("DF458KN", Account("Ann", "4135687", "Ann@gmail.com", "654321"))
    car2.printDataCar()
