
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredient, amount):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # for ingredient, amount in ingredients.items():
        if ingredient not in self.machine_resources or self.machine_resources[ingredient] < amount:
            return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ingredients_available = True
        for ingredient, amount in order_ingredients.items():
            if not self.check_resources(ingredient, amount):
                print(f"Sorry, we don't have enough {ingredient} for your order.")
                ingredients_available = False
                break
        if ingredients_available:
            print(f"Making a {sandwich_size} sandwich with:")
            for ingredient, amount in order_ingredients.items():
                print(f"- {amount} {ingredient}")
            print("Your sandwich is ready!")
        else:
            print("Unable to make sandwich due to insufficient ingredients.")

     #Test1
resources_available = {
    'bread': 2,
    'cheese': 6,
    'ham': 6,
    'lettuce': 7
}

sandwich_maker = SandwichMaker(resources_available)
sandwich_maker.make_sandwich('large', {'bread': 1, 'cheese': 2, 'ham': 4, 'lettuce': 3})
