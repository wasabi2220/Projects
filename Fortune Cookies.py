# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:19:14 2022
This is a Simple program of exercise for chapter 3 - COP1047C Intro to Python
MDC exercise for CH3
@supervisor: Eduardo Salcedo 
@author: Willy
revised: 03/16/2022 
v1.0

Exercise #1
Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random
each time it's run.
"""

#Calling an import ramdon function
import random #This is to create a random integer to be use in the if-else statement

#Random generator number in integer from 1 to 5
luck_gen = random.randint(1, 5)

#Random fortune message
cookies_num1 = "\nA feeling is an idea with roots."
cookies_num2 = "\nA new voyage will fill your life with untold memories."
cookies_num3 = "\nYou cannot love life until you live the life you love."
cookies_num4 = "\nThe love of your life is stepping into your planet this summer."
cookies_num5 = "\nYour hard work will be rewarded."

#Display the message
print("\nYour fortune cookie says:")
#if-else statement to display a random messages
if luck_gen == 1 :
    print(cookies_num1)
elif luck_gen == 2 :
    print(cookies_num2)
elif luck_gen == 3 :
    print(cookies_num3)
elif luck_gen == 4 :
    print(cookies_num4)
elif luck_gen == 5 :
    print(cookies_num5)
else :
    print("Runout of fortune cookies!")

input("\n\nPress the Enter key to exit.")