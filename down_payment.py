''' *Price of a house is 1 million
    *if buyer has good credit   \
        they need to put down 10%
    otherwise 
        they need to put down 20%
        * Print the down payment'''
# Name - Aditya Kumar
# ID - 22BTCSE067
# Programme - Btech CSE
print("Thanks for choosing this house")
print("for Payment Let me Know...")
price_of_house = 1000000
is_goodCredit = input("Does the person has good credit (yes/no): ").lower()
creditable_downpayment_percentage = 0.10
regular_downpayment_percentage = 0.20
if (is_goodCredit == 'yes'):
    down_payment = price_of_house*creditable_downpayment_percentage
else:
    down_payment = price_of_house*regular_downpayment_percentage
print(f"You need to put down Rs{down_payment} as down payment to purchase this house")