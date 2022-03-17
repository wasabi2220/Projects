# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:57:40 2022

This is a Simple program of exercise for chapter 3 - COP1047C Intro to Python
MDC exercise for CH3
@supervisor: Eduardo Salcedo 
@author: Willy
revised: 03/17/2022 
v1.0

Exercise #4
Write the pseudocode for a program where the player and the computer trade places in the number guessing game.
That is, the player picks a random number between 1 and 100 that the computer has to guess.
Before you start, think about how you guess. If all goes well, try coding the game.
"""

#To call the import random function
import random
import time

#To initialize a random number from 1 to 100
pc_guess = random.randint(1,100)
pc_down = 1
pc_up = 100

count = 0 #To zero out the count value
print("\nHello! I will try to guess your number in ten attempts or less.")
user = int(input("Please pick a number from 1 to 100: "))
#While loop to to run the guess if the number is higher or lower
while (count < 10): #Count the number of attempts
    if pc_guess < user: #If the number is lower the computer will go higher
       pc_up = pc_guess - 1
       pc_guess = random.randint(1, 100)    
       print("\nI'll go higher! guessed number was", pc_guess)
       count = count + 1 #Count the attempts
       time.sleep(0.500) #Add a pause time of 0.5 sec
    elif pc_guess > user: #If the number is higher the computer will go lower
        pc_down = pc_guess + 1
        pc_guess = random.randint(1, 100)
        print("\nI'll go lower! guessed number was", pc_guess)
        count = count + 1 #Count the attempts
        time.sleep(0.500) #Add a pause time of 0.5 sec
    elif pc_guess == user: #If the numer is equal to the random number display the message to the user
        print("\nI guessed it!,", "the number was:", pc_guess, "and it only took me", count, "attempts. YAHOO! 😁" )
        break #Quit the program
    if count == 10: #Display the message to the user after a number of attempts
        print("\nI ran out of guesses!", "It took me", count, "attempted, Better luck for me next time! 😞")
        print("Bye!")
        break #Quit the program
     