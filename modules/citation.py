class Citation(object):

    def __init__(self, fine=0):
        self.fine = fine
        self.balance = fine

        if not fine:
            self.status = "no charge"
        else:
            self.status = "unpaid"

    def pay(self, amount):
        self.balance += amount

        if self.balance:
            self.status = "partially paid"
        else:
            self.status = "paid"
