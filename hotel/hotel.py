from .customer import Customer

from datetime import datetime
import re
import random

class Hotel():
    def __init__(self,name, info, location, parking, shuttleBus, bar):
        self.name = name
        self.info = info
        self.customer = Customer()
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
        return self.customer.info

    def makeCustomerInfo(self):
        if self.checkCustomerInfo() is False:
            return self.customer.createOrUpdateInfo()




