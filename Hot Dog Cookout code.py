# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:57:51 2022

Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns 
needed for a cookout, with the minimum amount of leftovers.
The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given.
Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.
The program should display the following details:

• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over

@supervisor: Eduardo Salcedo
@author: willy
@Class: COP1047C - MDC Spring 2022
@Website information:
    1. https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
    2. https://www.w3schools.com/python/python_math.asp
    3. https://realpython.com/python-math-module/
    4. 

"""
#Import a function math for the rounding number
import math

#Declare the constant values for hot dog
hotDog_SausagePerPackage = 10
hotDog_BunsPerPackage = 8

#Read the user input for the numGuest and numHotdog
numGuest = int(input("Number of guests: "))
numHotdog = int(input("Number of Hot Dog per guests: "))

#Calculate total number of Hot Dog required
numOf_hotDog = (numGuest * numHotdog)

#Calculate number of package of Hot Dog sausages 
packageOf_HotdogSausage = numOf_hotDog / hotDog_SausagePerPackage

#Calculate number of package of Hot Gog buns
packagesOf_HotdogBuns = numOf_hotDog / hotDog_BunsPerPackage

#Calculate the remaining hot dog for buns and sausages
leftOver_HotdogSausage = ((math.ceil(packageOf_HotdogSausage) * hotDog_SausagePerPackage) - numOf_hotDog)
leftOver_HtodogBuns = ((math.ceil(packagesOf_HotdogBuns) * hotDog_BunsPerPackage) - numOf_hotDog)

#Display the result for each calculation
print()
print("Total number of Hot Dog required: ", numOf_hotDog)
print("Number package of Hot Dog sausage required: ", math.ceil(packageOf_HotdogSausage))
print("Number package of Hot Dog buns required:", math.ceil(packagesOf_HotdogBuns))
print("Number of left over Hot Dog sausage: ",leftOver_HotdogSausage)
print("Number of left over Hot Dog buns: ", leftOver_HtodogBuns)

"""
#For display result of each result only
print("\n\n")
print("hotDog_Needed:", numOf_hotDog)
print("packageOf_HotdogSausage:", packageOf_HotdogSausage)
print("packagesOf_HotdogBuns:", packagesOf_HotdogBuns)
print("leftOver_HotdogSausage:", leftOver_HotdogSausage)
print("leftOver_HtodogBuns:", leftOver_HtodogBuns)
"""
