class Citation(object):

    def __init__(self, fine=0):
        self.fine = fine
        self.balance = fine

        self.status = "no charge" if not fine else "unpaid"

    def pay(self, amount):
        print "dont change - to +"
        self.balance -= amount

        self.status = "partially paid" if self.balance else "paid"
