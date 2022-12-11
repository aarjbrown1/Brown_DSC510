# DSC 510
# Week 2
# Programming Assignment Week 2.1
# Author: Aaron Brown
# 12/09/2022

# ----Welcome Statement----
print("Hello, thank you for choosing OptiXX Electric!")
company_name = input('Please Enter Your Company Name/n')
print("Welcome, " + company_name + "!")

# ----Order Prompt----
cable_length = float(input('How much OptiXX Cable do you wish to install? (In Feet)/n'))
labor_cost = float(cable_length * 0.87)
print('Thank You! Your total cost today will be: $' + str (f'{labor_cost}'))

# ----Receipt Generation----
print ('OPTIXX ELECTRIC ATLANTA')
print ('5555 PeachState Drive')
print ('Atlanta, GA 30346')
print ('Bill of Sale')
print ('Customer:', company_name)
print ('Number of Feet Ordered:', cable_length, 'ft')
print ('Total Cost ($0.87 per ft): $', labor_cost)
print ('***Customer Copy***')

# Change#:1
# Change(s) Made: Added extra receipt verbiage to make it feel 'real'
# Date of Change: 12/10/2022
# Author: Aaron Brown





