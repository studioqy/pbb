'''
QY
November 21 2020
PBB

Week 09/10
Shopping Cart Assignment
Focus: Lists
'''

menu_value = 0
shopping_cart = []
all_prices = []
total_price = 0.00

print("Welcome to the Shopping Cart!\n")

# Loops the main menu that lets the user add and remove items, see total, etc.
# The loop starts once the user enters 5 from the menu
while menu_value != 5:
    print("Select an option by entering the cooresponding number:\n")
    menu_value = int(input("1 Add an item to cart\n"
                           "2 Remove an item from cart\n"
                           "3 View items in cart\n"
                           "4 Compute Total Cost\n"
                           "5 Quit\n"))

    # Adding an item to cart option
    if menu_value == 1:
        cart_item = input("\nEnter the item you wish to add to the cart: ")
        # Adds entered item to the list
        shopping_cart.append(cart_item)
        # Takes down the cost of the item and adds it to the all_prices list
        item_price = float(input(f"Enter the price of the {cart_item}: "))
        all_prices.append(item_price)
        print(f"{cart_item} has been added to the cart.\n")

    # Removing an item cart option
    elif menu_value == 2:
        # Loop in case the users enters a number out of the list
        while True:
            remove_item = int(input("\nEnter the number of the item you wish "
                                    "to remove from the cart: "))
            # If it's within the list, the item is removes
            if remove_item <= (len(shopping_cart)):
                print(f"{shopping_cart[remove_item - 1]} has been removed "
                      "from the cart.\n")
                shopping_cart.pop(remove_item - 1)
                break
            # If not, it loops back to the enter number message and sends an
            # error message
            else:
                print("Entered value not valid: Please select another value.")

    # Displaying the items in the cart option
    elif menu_value == 3:
        print("\nItems in cart:\n")
        # prints the list with all the added items
        # Something extra: The numbers, items, and prices should line up when
        # printed
        for item in shopping_cart:
            print(f"{shopping_cart.index(item) + 1:3} {item:15} "
                  f"${all_prices[shopping_cart.index(item)]}")
        print()

    # Compute total cost option
    elif menu_value == 4:
        # Iterates through the list and adds the cost of the items to
        # total_price
        for price in all_prices:
            total_price += price
        print(f"\nTotal cost of items in the cart: {total_price}\n")

    # Quitting the shopping cart option
    elif menu_value == 5:
        print("\nShopping cart successfully closed.")

    # If the user doesn't enter a number 1-5 at the menu, it sends this error
    # message and reprints the menu
    else:
        print("\nEntered value not valid: Please select another value.\n")
