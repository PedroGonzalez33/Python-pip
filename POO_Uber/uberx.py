from car import Car

class UberX(Car):
    brand = str
    model = str

    def __init__(self, licenses, driver, brand, model):
        super().__init__(licenses, driver)
        self.brand = brand
        self.model = model
        