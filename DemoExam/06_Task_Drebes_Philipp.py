# Your name: Philipp Drebes

# Start position for task 06!                                Total: 6 Pt.


def getNewCustomerNumber():  # (3 Pt)
    start = 1000
    while True:
        yield start
        start += 1


############
gen = getNewCustomerNumber()

class Customer:
    def __init__(self, first, last, mobile, customer_since):
        ############
        # to do ...  => every new object get's a new number!
        self.customer_id = gen.__next__()  # ( 1 Pt)
        self.first = first
        self.last = last
        self.mobile = mobile
        self.fullname = first + ' ' + last
        self.customer_since = customer_since

    ############
    # to to: Change this __str__()-function to get
    #        the correct output!                            # ( 1Pt )
    #        You will find the correct output below!
    def __str__(self):
        return ("CustomerID: " + str(self.customer_id) + "\nCustomerFullname: " + self.fullname + "\nCustomer since: " + str(
            self.customer_since))


cust01 = Customer("Anna", "Miller", "+41 79 123 45 67", 2012)
cust02 = Customer("Mike", "Sommer", "+41 76 321 54 76", 2019)
cust03 = Customer("Sandy", "Marino", "+41 78 321 34 99", 2021)

print(cust01)
print(cust02)
print(cust03)


##################################
# required output for task 6
##################################

# CustomerID: 1000
# CustomerFullname: Anna Miller
# Customer since: 2012
# **********************
# CustomerID: 1001
# CustomerFullname: Mike Sommer
# Customer since: 2019
# **********************
# CustomerID: 1002
# CustomerFullname: Sandy Marino
# Customer since: 2021
# **********************
