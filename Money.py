import time


class MoneyMachine:
    Currency = "₹"

    Cash_values = {"ten": 10, "twenty": 20, "fifty": 50, "five": 5}

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.Currency}{self.profit}")

    def process_coins(self):
        """Return the total processing"""
        print("Insert Money: \nOpening the Cash Gate.......")
        time.sleep(1)
        for cash in self.Cash_values:
            self.money_received += int(input(f"How many {cash}?: "))*self.Cash_values[cash]
        return self.money_received

    def make_payment(self, cost):
        """True if payment accepted"""

        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.Currency}{change} in change")
            time.sleep(1)
            print("Collect your money")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry not enough money\nTry again later")
            self.money_received = 0
            return False
