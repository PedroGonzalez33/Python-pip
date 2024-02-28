from account import Account

class Car:
    ID = int
    licenses = str
    driver = Account
    passegenger = str
    
    def __init__(self, licenses, driver):
        self.licenses = licenses
        self.driver = driver

    def printDataCar(self):
        print("Car license: ", self.licenses, " Driver: ", self.driver.name)
            

    