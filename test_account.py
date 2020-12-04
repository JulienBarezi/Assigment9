import unittest
from account import Account

account1 = Account("Christian", "199290877464727", "0780987122", 2000, 1234)


class MyTestCase(unittest.TestCase):

    def test_enquiry(self):
        self.assertEqual(account1.balance, 2000)

    def test_deposit(self):
        amount = 1000
        self.assertEqual(account1.balance+amount, 3000)

    def test_buy(self):
        amount = 1000
        self.assertEqual(account1.balance-amount, 1000)

    def test_password(self):
        self.assertEqual(account1.password, 1234)

    def test_name(self):
        self.assertEqual(account1.name, "Christian")


if __name__ == '__main__':
    unittest.main()