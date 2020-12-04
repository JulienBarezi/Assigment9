# author: Barezi Julien and Gihozo Landelin

# defining Account class
from pip._vendor.distlib.compat import raw_input


class Account:
    """ This class is the parent class for the other two accounts (customer and business accounts)
    It has the init function that creates the account and it has five instant variables which are
    name, id number, phone number, balance, and password. It also has two methods which are buy and check balance."""

    def __init__(self, name, idnumber, phonenbr, balance, password):

        self.name = name
        self.idnumber = idnumber
        self.phonenbr = phonenbr
        self.balance = balance
        self.password = password

    # defining buy method

    def buy(self, f):
        """In this method, the user is able to pay for different things such as electricity and airtime.
        the program asks the user which of the two the user want and after the user checking the program
        asks them to input their information and the transaction is made.

        :return= your balance after removing money you used in paying"""

        print("\nYou are buying:")
        print("\n1) Cashpower")
        print("2) Airtime")

        option = input("\nYour choice: ")

        # writing in the file
        f.write(option + "\n")

        if option == "1":
            print("\nYou are buying Cashpower ----")
            cash_power_number = int(input("\nCashpower Number: "))
            amount = int(input("Amount: "))

            # writing in the file
            f.write(str(cash_power_number) + "\n")
            f.write(str(amount) + "\n")

            Try_again = False
            if (self.balance - amount) < 1000:
                print("You have insufficient amount on your account")
                Try_again = True

            while Try_again is True:
                amount = int(input("Try another amount: "))
                if (self.balance - amount) > 1000:
                    break
                else:
                    print("You have insufficient amount on your account")

            print("\nUsing", amount,"FRW on cashpower", cash_power_number)
            password = int(input("\nInput your password to confirm: "))

            # writing in the file
            f.write(str(password) + "\n")

            if password == self.password:
                self.balance -= amount
                print("Transaction done successfully")
                print("\nYour new balance is ", self.balance, "\n")
            else:
                print("Wrong password, try again")

        elif option == "2":
            print("\nYou are buying airtime ----")
            print("\na) Your phone number")
            print("b) Another number")
            p_choice = input("\nChoose: ")

            # writing in the file
            f.write(str(p_choice) + "\n")

            pnbr = 0
            if p_choice == "a":
                print("You are recharging airtime to:", self.phonenbr)
                pnbr = (str(pnbr) + self.phonenbr)
            elif p_choice == "b":
                phone_number = int(input("\nYour phone number: "))

                # writing in the file
                f.write(str(phone_number) + "\n")

                pnbr = pnbr + phone_number

            amount = int(input("Amount: "))

            # writing in the file
            f.write(str(amount) + "\n")

            Try_again = False
            if (self.balance - amount) < 1000:
                print("You have insufficient amount on your account")
                Try_again = True

            while Try_again is True:
                amount = int(input("Try another amount: "))

                # writing in the file
                f.write(str(amount) + "\n")

                if (self.balance - amount) > 1000:
                    break
                else:
                    print("You have insufficient amount on your account")

            print("\nBuying airtime of", amount, "FRW on", pnbr)
            password = int(raw_input("\nInput your password to confirm: "))

            # writing in the file
            f.write(str(password) + "\n")

            if password == self.password:
                self.balance -= amount
                print("Transaction done successfully")
                print("\nYour new balance is", self.balance, "\n")
            else:
                print("Wrong password, try again\n")

        else:
            print("Wrong input, try again!")

    # defining the method that let's you check balance

    def enquiry(self):
        """"  In this method, the user is shown the amount of money s/he has on their account
         after inputting their password.

          :return= available balance"""

        print("Your balance is", self.balance)

    # defining the deposit method

    def deposit(self, f):
        """" In this method, the user is asked the amount of money s/he wants to deposit,
         and then s/he is given a confirmation message that the money has been deposited
         detailing the current balance too.

         :return = money you deposited plus the amount that was on your account before"""
        print("\nYou are Depositing Money ------")
        amount = int(raw_input('\nAmount:'))
        self.balance += amount
        print("Deposited Successfully")
        print("\nYour New Balance is", self.balance, "\n")

        # writing in the file
        f.write(str(amount) + "\n")



