# DSC 510
# Programming Assignment Week 3
# Author: Aaron Brown
# 12/17/2022

# ----Welcome Statement----
print("Hello, thank you for choosing OptiXX Electric!")
company_name = input('Please Enter Your Company Name/n')
print("Welcome, " + company_name + "!")

# ----Order Prompt----
cable_length = float(input('How much OptiXX Cable do you wish to install? (In Feet)/n'))
# ----Workspace----
if cable_length < 100:
    priceperft = float(.87)
    labor_cost = float(cable_length * priceperft)
    roundedcost = round(labor_cost, 2)
    print('Thank You! Your total cost today will be: $' + str(f'{roundedcost}'))
elif 99 < cable_length < 250:
    priceperft = float(.80)
    labor_cost = float(cable_length * priceperft)
    roundedcost = round(labor_cost, 2)
    print('Thank You! Your total cost today will be: $' + str(f'{roundedcost}'))
elif 249 < cable_length < 500:
    priceperft = float(.70)
    labor_cost = float(cable_length * priceperft)
    roundedcost = round(labor_cost, 2)
    print('Thank You! Your total cost today will be: $' + str(f'{roundedcost}'))
elif 499 < cable_length:
    priceperft = float(.50)
    labor_cost = float(cable_length * priceperft)
    roundedcost = round(labor_cost, 2)
    print('Thank You! Your total cost today will be: $' + str(f'{roundedcost}'))


# ----Receipt Generation----
print('OPTIXX ELECTRIC ATLANTA')
print('5555 PeachState Drive')
print('Atlanta, GA 30346')
print('Bill of Sale')
print('Customer:', company_name)
print('Number of Feet Ordered:', cable_length, 'ft')
print("Total Cost: $" + str(roundedcost))
print('***Customer Copy***')

# Change#:1
# Change(s) Made: Added extra receipt verbiage to make it feel 'real'
# Date of Change: 12/10/2022
# Author: Aaron Brown

# Change#:2 Added Code for Bulk Discount
# Change(s) Made: Added round function to simplify long decimal places
# Date of Change: 12/17/2022
# Author: Aaron Brown

# Change#:3
# Change(s) Made: Added Code for Bulk Discount
# Date of Change: 12/17/2022
# Author: Aaron Brown
