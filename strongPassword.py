'''
Created on Mar 11, 2017

@author: dalton
'''

import re

def passwordChecker(password):
    alphaCheck = re.compile(r'[A-Z]+[a-z]+|[a-z]+[A-Z]+')
    numCheck = re.compile(r'\d')
    
    if len(password) < 8:
        return "Password too short."
    if alphaCheck.search(password) == None:
        return "Password needs at least one upper and lowercase letter."
    if numCheck.search(password) == None:
        return "Password must contain at least one number."
        
    return "This is a strong password"

print(passwordChecker("nouppercaseletters8"))
print(passwordChecker("NOLOWERCASELETTERS8"))
print(passwordChecker("sh0rt"))
print(passwordChecker("NoNuMbEr"))
print(passwordChecker("Thisshouldw0rk"))