#! python3
"""
Created on Mar 24, 2017
Finds files over a specified file size in the chosen path
@author: dalton
"""

import os
import re
from math import pow


def convert_byte_to_human(convert_size):
    # Converts bytes from os.path.getsize to human readable format
    endings = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']

    size = convert_size

    for ending in endings:
        if size < 1024:
            return '{0} {1}'.format(str(round(size, 2)), ending)
        size /= 1024


def convert_human_to_byte(convert_size):
    # Converts human-readable format to bytes
    endings = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']

    try:
        return float(convert_size.replace(',', ''))
    except ValueError:
        pass

    split_size = re.match(r'(\d+,?\d*\.?\d*)\s?(\w+)', convert_size)
    if split_size is None:
        raise Exception('Use standard format (e.g. 123 MB, 40kb, 1000B)')
    split_number = split_size.group(1).replace(',', '')
    split_ending = split_size.group(2).upper()

    return float(split_number) * pow(1024, endings.index(split_ending))


def find_files(user_path, minimum_size):
    # Make sure that user_path is absolute path
    user_path = os.path.abspath(user_path)
    if not os.path.isdir(user_path):
        raise Exception('Filepath invalid')
    # Walks specified file path and prints files larger than the minimum size
    for folder_names, _, file_names in os.walk(user_path):
        for file in file_names:
            try:
                file_size = os.path.getsize(os.path.join(folder_names, file))
                if file_size >= minimum_size:
                    print('{0} - {1}'.format(os.path.join(folder_names, file), convert_byte_to_human(file_size)))
            except:
                pass
    print('Search complete.')


try:
    filepath = input('Enter a filepath: ')
    filesize = input('Enter a filesize: (ex. 400 MB) ')

    find_files(filepath, convert_human_to_byte(filesize))
except Exception as err:
    print('An exception has happened: {0!s}'.format(err))
