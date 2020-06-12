"""
Program: BasicLoops.py
Author: Paul Elsea
Last Modified: 06/12/2020

Program to demonstrate two for-loops.
"""

'''This is a list of numbers to be referenced by a for-loop'''
floatList = [1.45, 5.54, 9.87, 14.45, 1.78, 6.54]

'''For-loop that pulls each number one at a time from the list above and prints them'''
for num in floatList:
    print(num)

'''Print of an empty line to provide a space between the two loops'''
print('')

'''For-loop that prints each odd number in a descending order from 99 to 33 inclusive'''
for oddNum in range(99, 32, -2):
    print(oddNum)