"""
Manipulating files in Python!

The open() function opens a file, and returns it as a file object
    open(file, mode)
        file	The path and name of the file
        mode	A string, define which mode you want to open the file in:
            "r" - Read - Default value. Opens a file for reading, error if the file does not exist

            "a" - Append - Opens a file for appending, creates the file if it does not exist

            "w" - Write - Opens a file for writing, creates the file if it does not exist

            "x" - Create - Creates the specified file, returns an error if the file exist

            In addition you can specify if the file should be handled as binary or text mode

            "t" - Text - Default value. Text mode

            "b" - Binary - Binary mode (e.g. images)
Source:
https://docs.python.org/3/library/functions.html#open
https://www.w3schools.com/python/ref_func_open.asp
"""
import os

file = open('abc.txt', 'w+')

file.write('Line 1\n')
file.write('Line 2\n')
file.write('Line 3\n')

file.seek(0, 0)  # Set the cursor in the beginner of file
print('Read lines:')
print(file.read(), end='')
print('---')

file.seek(0, 0)  # Set the cursor in the beginner of file
print(file.readline(), end='')  # Read only a line and put the cursor in the next
print(file.readline(), end='')  # Read only a line and put the cursor in the next
print(file.readline(), end='')  # Read only a line and put the cursor in the next
print('---')

file.seek(0, 0)  # Set the cursor in the beginner of file
print(file.readlines())  # Return a list with all lines
print('---')

file.close()

with open('abc.txt', 'a+') as file:  # With "with" block, we don't need to close the file
    file.write('Other line\n')
    file.seek(0, 0)
    print(file.read())

os.remove('abc.txt')  # Removing a file
