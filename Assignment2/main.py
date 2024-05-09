import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
        ##  write the rest of the codes ##
        order_size = "medium"
        order_ingredients = recipes[order_size]["ingredients"]

        # Check if resources are sufficient
        if sandwich_maker_instance.check_resources(order_ingredients):
            # Process payment
            payment = cashier_instance.process_coins()
            cost = recipes[order_size]["cost"]
            # Check if payment is sufficient
            if cashier_instance.transaction_result(payment, cost):
                # Make the sandwich
                sandwich_maker_instance.make_sandwich(order_size, order_ingredients, cost)
                print("Enjoy your", order_size, "sandwich!")
            else:
                print("Sorry, payment is insufficient.")
        else:
            print("Sorry, insufficient resources to make the sandwich.")

if __name__=="__main__":
    main()
