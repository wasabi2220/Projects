# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:08:39 2022

This is a Simple program of exercise for chapter 3 - COP1047C Intro to Python
MDC exercise for CH3
@supervisor: Eduardo Salcedo 
@author: Willy
revised: 03/17/2022 
v1.0

Exercise #3
Modify the Guess My Number game so that the player has a limited number of guesses.
If the player fails to guess in time, the program should display an appropriately chastising message.
"""

#To call the import random function
import random

#To initialize a random number from 1 to 10
num = random.randint(1,10)
count = 0 #To zero out the count value

#While loop to to run the guess if the number is higher or lower
while (count < 5): #Count the number of attempts
    i = int(input("Guess the number from 1 to 20: "))
    if i < num: #If the number is lower as the user to go higher
        print("\nGo higher!")
        count = count + 1 #Count the attempts
    elif i > num: #If the number is higher as the user to go lower
        print("\nGo lower!")
        count = count + 1 #Count the attempts
    elif i == num: #If the numer is equal to the random number display the message to the user
        print("\nYou guessed it!,", "the number was:", num, "and it only took you", count, "attempts. Congratulation!" )
        break #Quit the program
    if count == 5: #Display the message to the user after a number of attempts
        print("\nYou ran out of guesses!", "It took you", count, "attempts, Better luck next time!")
        print("Bye!!")
        break #Quit the program
     