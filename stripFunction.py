'''
Created on Mar 11, 2017

@author: dalton
'''

import re

def stringStripper(text, toStrip=' '):
    if toStrip == ' ':
        stripRegex = re.compile(r'^\s+|\s+$')
    else:
        stripRegex = re.compile(r'[' + toStrip + ']')
    
    output = stripRegex.sub('', text)
    
    print(output + "end")
    
    
stringStripper("      testing          ")
stringStripper("let's remove e's and s's", 'es')