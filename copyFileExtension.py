#! python3
'''
Created on Mar 23, 2017

@author: dalton
'''

import os, shutil

def copyFiles(folder, extension):
    # Check to see if directory exists and create it if it doesn't
    organizerFolder = 'C:\\Users\\dalton\\Documents\\file_organizer_' + str(extension)
    if not os.path.exists(organizerFolder):
        print('Creating directory %s...' % (organizerFolder))
        os.makedirs(organizerFolder)
    
    count = 0
    # Walk through specified folder
    for folders, subfolders, files in os.walk(folder):

        # Find specified extension's files in path
        for file in files:
            if file.endswith('.' + str(extension)) and folders != organizerFolder:
                print('Copying file %s...' % (folders + '\\' + file))
                shutil.copy(folders + '\\' + file, organizerFolder + '\\' + file)
                count += 1
    print('Successfully copied %s files.' % (count))
        
copyFiles('C:\\Users\\dalton', 'txt')
        