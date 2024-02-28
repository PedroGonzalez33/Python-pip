from payment import Payment

class Paypal(Payment):
    email = str

    def __init_(self, email):
        super().__init__()
        self.email = email

    

