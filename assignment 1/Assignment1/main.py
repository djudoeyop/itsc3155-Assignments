### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.25,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}




class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < amount:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0
        total += int(input("Enter the number of dollars")) * 1
        total += int(input("Enter the number of quarters: ")) * 0.25
        total += int(input("Enter the number of dimes: ")) * 0.10
        total += int(input("Enter the number of nickels: ")) * 0.05
        total += int(input("Enter the number of pennies: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        recipe = recipes[sandwich_size]["ingredients"]
        for ingredient, amount in recipe.items():
             self.machine_resources[ingredient] -= amount


### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

# Test making a sandwich
order_size = "medium"
order_ingredients = recipes[order_size]["ingredients"]

# Check if resources are sufficient
if machine.check_resources(order_ingredients):
    # Process payment
    payment = machine.process_coins()
    cost = recipes[order_size]["cost"]
    # Check if payment is sufficient
    if machine.transaction_result(payment, cost):
        # Make the sandwich
        machine.make_sandwich(order_size, order_ingredients)
        print("Enjoy your", order_size, "sandwich!")
    else:
        print("Sorry, payment is insufficient.")
else:
    print("Sorry, insufficient resources to make the sandwich.")