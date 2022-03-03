# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:08:08 2022
This is a Simple Income Tax Calculator Project for COP1047C Intro to Python
MDC Project#1
@supervisor: Eduardo Salcedo 
@author: Willy
"""

#Initialize the constants value
tax_rate=0.20 #Tax rate of 20% value
standard_deduction=10000.00 #Standard deduction amount
dependent_deduction=3000.00 #Dependent deduction amount

#Declare the User input
income=float(input("Please enter your gross income including decimal: ")) #Requesting an input from the user the total gross income
num_dependent=int(input("Please enter the number of dependents: ")) #Requesting an user input the total number of dependent

#Declaring the formula for Income Tax calculation
tax=float((income-standard_deduction-(num_dependent*dependent_deduction))*tax_rate) #Income Tax calculation in float

#Print the result
print(f"\nYour gross income taxis: ${income:.2f}") #Print the gross income input with two decimal to the screen
print("\nYour number of dependets:",num_dependent) #Print the number of dependent to the screen
print(f"\nThe income tax is ${tax:.2f}") #Print the total amount of income tax to the screen
