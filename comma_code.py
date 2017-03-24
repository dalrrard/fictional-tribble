'''
Created on Mar 6, 2017

@author: dalton
'''
def commaCode(itemList):
    sentence = ''
    for i in range(len(itemList)):
        sentence += itemList[i] + ', ' if i != len(itemList)-1 else 'and ' + itemList[i]
        
    return sentence
        

spam = ['apples', 'bananas', 'tofu', 'cats', 'bread', 'milk']

print(commaCode(spam))