# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.


#!/usr/bin/python

import pathlib

file_extensions = [".jpg", ".mov"]

search_folder = input("Please enter the full path of the folder you want to search: ")
search_folder = pathlib.Path(search_folder)

for item in search_folder.iterdir():
    if item.is_file():
        for fex in file_extensions:
            if item.suffix == fex:
                print(item)
    elif item.is_dir():
        for item_l1 in item.iterdir():
            if item_l1.is_file():
                for fex in file_extensions:
                    if item_l1.suffix == fex: 
                        print(item_l1)
            elif item_l1.is_dir():
                for item_l2 in item_l1.iterdir():
                    if item_l2.is_file():
                        for fex in file_extensions:
                            if item_l2.suffix == fex: 
                                print(item_l2)
                            

                        
            