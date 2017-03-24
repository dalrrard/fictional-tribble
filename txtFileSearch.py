'''
Created on Mar 14, 2017

@author: dalton
'''

import re, os

while True:
    filePath = input("Enter a valid folder path: ")
    if os.path.exists(filePath):
        break

regex = re.compile(input("Enter a regular expression to search for: "))

for file in os.listdir(filePath):
    splitFile = file.split('.')
    if len(splitFile) > 1 and splitFile[1] == 'txt':
        textFile = open(filePath + "\\" + file, 'r')
        textFileContent = textFile.readlines()
        for line in textFileContent:
            if regex.search(line):
                print(filePath + "\\" + file)
                print(line)