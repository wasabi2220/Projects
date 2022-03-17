# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:16:02 2022
This is a Simple program of exercise for chapter 3 - COP1047C Intro to Python
MDC exercise for CH3
@supervisor: Eduardo Salcedo 
@author: Willy
revised: 03/17/2022 
v1.0

Exercise #2
Write a program that flips a coin 100 times and then tells you the number of heads and tails.
"""

#To call the import random function
import random

#Create a Dictionarie function to store the counts of heads and tails
results = {"heads": 0, "tails": 0}

#To initialize the counter to zero
coin_flipped = 0

#To set the heads ass '0' and tails as '1'
sides = list(results.keys())

#To start the counting from 0 to 100 (0 to 99)
for coin_flipped in range(100):
    results[random.choice(sides)] += 1 #For each run store the result to heads or tails 

#Display the result of heads and tails
print()
print('Heads:', results['heads'])
print('Tails:', results['tails'])

#Display the winner message
if results["heads"] > results["tails"]:
    print("\nHeads win!")
elif results["tails"] > results["heads"]:
    print("\nTails win!")
else:
    print("\nIt's a tie!")