#! python3
'''
Created on Mar 14, 2017

@author: dalton
'''
import re

madlibFile = open('C:\\Users\\dalton\\Documents\\madlib.txt')
madlibContent = madlibFile.read()
madlibFile.close()
madlibRegex = re.compile(r'VERB|ADJECTIVE|NOUN|ADVERB')

mo = madlibRegex.findall(madlibContent)

for partOfSpeech in mo:
    madlibContent = madlibRegex.sub(input("Enter a(n) " + partOfSpeech.lower() + ": "),
                                     madlibContent, 1)

print(madlibContent)

madlibNewFile = open('C:\\Users\\dalton\\Documents\\madlib_new.txt', 'w')
madlibNewFile.write(madlibContent)
madlibNewFile.close()