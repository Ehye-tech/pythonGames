from .customer import Customer

class Room:
    def __init__(self):
        self.num = 0
        self.size = ""
        self.price = 0
        self.view = ""
        self.numsOfPpl = ""
        self.infant = ""
        self.request = ""
        self.customer = Customer()
        self.booked = False

    def setdata(self,num,size,price, viewType, numsOfPpl, infant, request):
        self.num = num
        sizes = ['queen room','king room','studio','semi suite', 'suite', 'king suite']
        self.size = sizes[size] #300.00booked
        self.price = price
        view = ["ocean","city","none"]
        self.view = view[viewType]
        self.numsOfPpl = numsOfPpl
        self.infant = infant
        self.request = request

    def checkBooking (self):
        if self.booked == True:
            print("Room", self.num, "is not available")
            return False
        else:
            print("You can book Room", self.num)
            if(self.makePayment() == True):
                return True
            else:
                print("Please make a payment for booking the room immediately. Thank you!")
                return False

    def makePayment(self,payment) -> object:
        return self.customer.makePayment(self.price,payment)

