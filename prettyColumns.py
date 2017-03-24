'''
Created on Mar 8, 2017

@author: dalton
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for lists in range(len(table)):
        for items in table[lists]:
            colWidths[lists] = len(items) if len(items) > colWidths[lists] else colWidths[lists]
    
    for lengths in range(len(table[0])):
        for items in range(len(table)):
            print(table[items][lengths].rjust(colWidths[items]), end=' ')
        print()

printTable(tableData)