#! python3
'''
Created on Mar 24, 2017

@author: dalton
'''

import os, re
from math import pow

def convert_byte_to_human(convert_size):
    # Converts bytes from os.path.getsize to human readable format
    endings = ['B','KB','MB','GB','TB','PB','EB','ZB']
    
    size = convert_size
    
    for ending in endings:
        if size < 1024:
            return str(round(size, 2)) + ' ' + ending
        size /= 1024

def convert_human_to_byte(convert_size):
    # Converts human-readable format to bytes
    endings = [' B','KB','MB','GB','TB','PB','EB','ZB']
    
    if convert_size.isdigit():
        return convert_size
    
    split_size = re.match(r'(\d+) (\w+)', convert_size)
    split_number = split_size.group(1)
    split_ending = split_size.group(2)
    
    for i in range(len(endings)):
        if convert_size.endswith(endings[i]):
            return int(split_number) * pow(1024, i)
            

def find_files(user_path, minimum_size):
    # Make sure that user_path is absolute path
    user_path = os.path.abspath(user_path)
    
    # Walks specified file path and prints files larger than the minimum size
    for folder_names, subfolders, file_names in os.walk(user_path):
        for file in file_names:
            try:
                file_size = os.path.getsize(os.path.join(folder_names,file))
                if file_size >= minimum_size:
                    print('{0} - {1}'.format(os.path.join(folder_names, file), convert_byte_to_human(file_size)))
            except:
                pass
    print('Search complete.')


filepath = input('Enter a filepath: ')
filesize = input('Enter a filesize: (ex. 400 MB) ')
find_files(filepath, convert_human_to_byte(filesize))