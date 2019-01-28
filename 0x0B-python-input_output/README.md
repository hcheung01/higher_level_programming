# 0x0B. Python - Input/Output
---
## Description

This project in the High Level Programming series is about:
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

## Files
---
File|Task
---|---
0-read_file.py | function that reads a text file (UTF8) and prints it to stdout
1-number_of_lines.py | function that returns the number of lines of a text file
2-read_lines.py | function that reads n lines of a text file (UTF8) and prints it to stdout
3-write_file.py | writes a string to a text file (UTF8) and returns the number of characters written
4-append_write.py | appends a string at the end of a text file (UTF8) and returns the number of characters added
5-to_json_string.py | returns the JSON representation of an object (string)
6-from_json_string.py | returns an object (Python data structure) represented by a JSON string
7-save_to_json_file.py | writes an Object to a text file, using a JSON representation
8-load_from_json_file.py | creates an Object from a “JSON file”
9-add_item.py | adds all arguments to a Python list, and then save them to a file
10-class_to_json.py | returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
11-student.py | class Student
12-student.py | class Student that defines a student by: (based on 11-student.py)
13-student.py | class Student that defines a student by: (based on 12-student.py)
14-pascal_triangle.py | function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
100-append_after.py | function that inserts a line of text to a file, after each line containing a specific string 
101-stats.py | script that reads stdin line by line and computes metrics

## Directories
---
Directory Name | Description
---|---
0x0B-python-input_output | Main files for all functions

## More Info for Python programs
* All Python files is PEP 8(version 1.7) formatted
* All modules, classes and functions(inside and outside a class) have documentations
* Python Scripts - first line of every file is exactly be exactly #!/usr/bin/python3 and executable

## Python Test Cases
* All tests should be executed by using this command: python3 -m doctest ./tests/*
* All test files is inside a folder tests
* All test files is text files (extension: .txt)

## Author
Heindrick Cheung