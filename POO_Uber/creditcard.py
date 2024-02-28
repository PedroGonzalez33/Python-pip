from payment import Payment

class Creditcard(Payment):
    number = int
    cvv = int
    date = int

    def __init_subclass__(self, number, cvv, date):
        super().__init__()
        self.number = number
        self.cvv = cvv
        self.date = date