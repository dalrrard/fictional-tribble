'''
Created on Mar 4, 2017

@author: dalton

Collatz sequence
'''
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
    
print('Enter a number: ')
try:
    startingValue = int(input())
    
    while startingValue != 1:
        startingValue = collatz(startingValue)
except ValueError:
    print('You must enter a number')

