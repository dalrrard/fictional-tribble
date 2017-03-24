'''
Created on Mar 6, 2017

@author: dalton
'''
def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)