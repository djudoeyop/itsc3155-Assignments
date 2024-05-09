class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        total = 0
        total += int(input("Enter the number of dollars")) * 1
        total += int(input("Enter the number of quarters: ")) * 0.25
        total += int(input("Enter the number of dimes: ")) * 0.10
        total += int(input("Enter the number of nickels: ")) * 0.05
        total += int(input("Enter the number of pennies: ")) * 0.01
        return total

    def transaction_result(self, total, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if total >= cost:
            return True
        else:
            return False
