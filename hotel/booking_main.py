import re
from datetime import datetime
import random

class Customer:
    def __init__(self,suffix,firstName, lastName, address, phone, email, roomNum, desc):
        self.suffixes = ["N/A","Mr.","Mrs.","Miss","Ms.", "Dr."]
        self.suffix = self.suffixes[suffix]
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email
        self.address = address
        self.roomNum = roomNum
        self.desc = desc
        self.accountBalance = 0
        self.info = {'suffix':self.suffix,'firstName':self.firstName, 'lastName':self.lastName, 'phone':self.phone, 'email':self.email, 'address':self.address,'roomNum':self.roomNum,'desc':self.desc,'accountBalance':self.accountBalance}


    def saveBalance (self, diff):
        yN = input("Would you want to save $ %s on your account balance? [y/n] " %diff)
        if yN.lower() == "y":
            self.accountBalance += diff
            print("The changes $ %s has been saved on your account. Thanks for using our service!" %diff)
            return self.accountBalance
        else:
            return print("You will get refund $ %s in 7 business days to your original payment." %diff)

    def createOrUpdateInfo (self):
        k = input(f'What would you like to change or update? ')
        e = self.info.get(k)
        if e is None:
            i = input(f'Create a new information  {k} : ')
            self.info[k] = i
        else:
            eHasValue = input("Do you really want to update information? [y/n] ")
            if eHasValue.lower() == "y":
                i = input(f'Type the update information: {k} ')
                self.info[k] = i
            else:
                print("Nothing has been changed.")


    def makePayment(self,roomPrice:float ,payment:float, ):
        roomPrice = self.checkBalance(roomPrice)
        diff = abs(payment-roomPrice)
        print("Hello, ",self.suffix, self.name, "!")
        if payment < 0:
            print("Something went wrong. Try again another time.")
            return False
        elif payment == roomPrice:
            print("Your payment went through successfully.")
            return True
        elif payment > roomPrice:
            print("You have made $",payment, " payment. The room has been booked. Over paid amount is $",diff,".")
            self.saveBalance(diff)
            return True
        else:
            print("You have made $",payment, " payment. You need to pay $",diff," more.")
            return False

    def checkBalance(self, roomPrice:float) -> float:
        if self.accountBalance > 0:
            useBalance = input("You still have $ %s left. Would you like to use it all? [y/m]" %(self.accountBalance))
            if useBalance.lower() == 'y':
                roomPrice -= self.accountBalance
            return roomPrice
        else:
            return roomPrice


class Room:
    def __init__(self,num,size,price, viewType, numsOfPpl, infant, request):
        self.num = num
        sizes = ['queen room','king room','studio','semi suite', 'suite', 'king suite']
        self.size = sizes[size] #300.00booked
        self.price = price
        view = ["ocean","city","none"]
        self.view = view[viewType]
        self.numsOfPpl = numsOfPpl
        self.infant = infant
        self.request = request
        self.booked = self.checkBooking() #False

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
        return self.Customer.makePayment(self.price,payment)

class Hotel():
    def __init__(self,name, info, location, parking, shuttleBus, bar):
        self.name = name
        self.info = info
        self.roomNums = self.hotelRooms()
        self.customers = self.customerData()
        locations = ["ocean","city","none"]
        self.location = locations[location]
        self.parking = parking #False
        self.shuttleBus = shuttleBus #False
        self.bar = bar #True

    def hotelRooms(self,nums):
        nums = nums
        rooms = [num+100 for num in range(1,nums)]
        availabilities = [False for num in range(1,nums)]
        self.roomNums = {r:a for r,a in zip(rooms,availabilities)}
        return self.roomNums

    def customerData(self):
        customerId = datetime.today().strftime("%Y%m%d")+random.randint(range(1,10000))
        self.customers.update({customerId:self.getCustomerInfo()})



    def roomAvailiblity(self, num):
        if self.Room.booked == True:
            print("Room ",num, "is booked.")
        else:
            print("You can book room ",num, "Would you like to make a book today?")

    def checkCustomerInfo(self):
        phoneNum = input("Type the customer's phone number: [num-num-num] ")
        emailAddress = input("Type the customer's email: [id@website.com]")
        regex1 = phoneNum
        regex2 = emailAddress
        phone = re.findall('^',regex1,'$')
        email = re.findall('^',regex2,'$')
        if phone or email in self.customers.values().values():
            print(self.customers['customerId']['suffix'], self.customers['customerId']['lastName'],"has booked room ",self.customers['customerId']['roomNum'],".")
            # return self.customers
    def getCustomerInfo(self):
        return self.Customer.info

    def makeCustomerInfo(self):
        if self.checkCustomerInfo() is False:
            return self.Customer.createOrUpdateInfo()



if __name__ == '__main__':
    a = Room(101,1,100.00,0)
    b = Customer(0,"John","Smith","2450 Massachusetts Ave NW, Washington, DC 20008", "202-322-1113","vacation",2,0)
    c = Hotel("W","With a complete top-to-bottom hotel renovation, W Washington D.C. is ready to be experienced to the fullest.",1)

    print(b.makePayment(a.price,10))
    # print(a.checkBooking())
    # print(c.roomNums,c.location)

