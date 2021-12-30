'''
Thing
Week 4 Meal Price Calculator
'''

# Asks for the meal prices
child_price = float(input('What is the price of a child\'s meal? '))
adult_price = float(input('What is the price of an adult\'s meal? '))

# Asks for the number of children and adults
child_num = int(input('How many children are there? '))
adult_num = int(input('How many adults are there? '))

# Asks for the sales tax rate
tax_rate = float(input('What is the sales tax rate? '))

# Calculates the total before tax, the taxt amount, and the total after tax
subtotal = child_price * child_num + adult_price * adult_num
tax_amount = subtotal * (tax_rate / 100)
total = subtotal + tax_amount

# Prints the subtotal, tax, and total
print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${tax_amount:.2f}')
print(f'Total: ${total:.2f}')

# Asks user for the amount they are paying with and calculates the change
# from it
paid_amount = float(input('What is the payment amount? '))
change_amount = paid_amount - total

'''
"Make it your own" portion of this project: A while loop.

If the user does not enter enough money to cover the bill, the program will
send back an error stating the amount still needed, and allows the user to
input another payment amount. If the new payment amount is still not enough,
the error repeats with the new amount needed, and if it is sufficient, then
it displays the change amount. If the initial payement amount is enough, then
it will just display the change amount.
'''

while change_amount < 0:
    change_amount = abs(change_amount)
    print(f'Error: payment amount is not sufficient. ${change_amount:.2f} '
          'more is needed.')
    paid_amount = float(input('What is the payment amount? '))
    change_amount = paid_amount - change_amount
else:
    print(f'Change: ${change_amount:.2f}')
