#from .room import Room
import



class Customer:

    def __init__(self):
        self.suffix = "N/A"
        self.firstName = ""
        self.lastName = ""
        self.phone = ""
        self.email = ""
        self.address = ""
        self.room = Room()
        self.roomNum = self.room.num
        self.roomPrice = self.room.price
        self.desc = ""
        self.accountBalance = 100
        self.roomNum = 0
        self.info = {'suffix':self.suffix,'firstName':self.firstName, 'lastName':self.lastName, 'phone':self.phone, 'email':self.email, 'address':self.address,'roomNum':self.roomNum,'desc':self.desc,'accountBalance':self.accountBalance}

    def setData(self,suffix,firstName, lastName, address, phone, email, roomNum, desc):
        self.suffixes = ["","Mr.","Mrs.","Miss","Ms.", "Dr."]
        self.suffix = self.suffixes[suffix]
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email
        self.address = address
        self.roomNum = roomNum
        self.desc = desc
        self.info = {'suffix':self.suffix,'firstName':self.firstName, 'lastName':self.lastName, 'phone':self.phone, 'email':self.email, 'address':self.address,'roomNum':self.roomNum,'desc':self.desc,'accountBalance':self.accountBalance}

    def saveBalance (self, diff):
        yN = input("Would you want to save $ %s on your account balance? [y/n] " %diff)
        if yN.lower() == "y":
            self.accountBalance += diff
            print("The changes $ %s has been saved on your account. Thanks for using our service!" %diff)
            print(self.accountBalance, "is total left balance on your account.")
            return self.accountBalance
        else:
            return print("You will get refund $ %s in 7 business days to your original payment." %diff)

    def createOrUpdateInfo (self):
        k = input(f'What would you like to change or update? ')
        v = self.info.get(k)
        print(v, type(v))
        if (v is '') or (v is None):
            i = input(f'Create a new information  {k} : ')
            self.info[k] = i
        else:
            vHasValue = input("Do you really want to update information? [y/n] ")
            if vHasValue.lower() == "y":
                i = input(f'Type the update information: {k} ')
                self.info[k] = i
            else:
                print("Nothing has been changed.")

    def makePayment(self):
        payment = float(input("How much do you want to pay now? "))
        if payment < self.roomPrice:
            self.roomPrice, balance = self.checkBalance(self.roomPrice)
        diff = abs(payment-self.roomPrice)
        print("Hello, ",self.suffix, self.lastName, "!")
        if payment < 0:
            print("Something went wrong. Try again another time.")
            return False
        elif payment == self.roomPrice:
            print("Your payment went through successfully.")
            return True
        elif payment > self.roomPrice:
            print("You have made $",payment, " payment. The room has been booked. Over paid amount is $",diff,".")
            self.saveBalance(diff)
            return True
        else:
            print("You have made $",payment + balance, " payment. You need to pay $",diff," more.")
            return False

    def checkBalance(self, roomPrice:float) -> float:
        if self.accountBalance > 0:
            useBalance = input("You still have $ %s left. Would you like to use it all? [y/n] " %(self.accountBalance))
            if useBalance.lower() == 'y':
                balance = self.accountBalance
                print("balance: ",balance)
                roomPrice -= self.accountBalance
                self.accountBalance = 0
            return roomPrice, balance
        else:
            return roomPrice


