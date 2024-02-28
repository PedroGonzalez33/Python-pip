from car import Car

class UberVan(Car):
    typecaraccepted = ["",["",int]]
    seatsmaterial = ["",""]

    def __init__(self, licenses, driver, typecaraccepted, seatsmaterial):
        super().__init__(licenses, driver)
        self.typecaraccepted = typecaraccepted
        self.seatsmaterial = seatsmaterial