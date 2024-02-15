# Python - Input / Output

## General 🐍
    **How to Perform File Operations in Python :**
        - Opening a File : use the function `open()` specifying the file path and mode (e.g., read, write, append)
            - `file = open("filename.txt", "r")`
        - Writing Text to a File : use the `write()` method. Make sure to open the file in write or append mode
            - `with open("filename.txt", "w") as file:
                    file.write("Hello, world!")`
        - Reading the Full Content of a File : use the `read()` method after opening the file in read mode : 
            - `with open("filename.txt", "r") as file:
                    content = file.read()
                    print(content)`
        - Reading a File Line by Line : use a loop or the `readline()` method within a loop : 
            - `with open("filename.txt", "r") as file:
                    for line in file:
                    print(line)`
        - Moving the Cursor in a File : use the `seek()` method : 
            - `with open("filename.txt", "r") as file:
                    file.seek(10)
                    content = file.read()
                    print(content)`
        - Closing a File : The `with` statement in Python is commonly used for file operations to automatically close files after use : 
            - `with open("filename.txt", "r") as file:
                    content = file.read()
                    print(content)`

    **Understanding JSON Serialization and Deserialization :**
        - What is JSON?
            - JSON (JavaScript Object Notation) is a lightweight format for data interchange, commonly used for serialization and transmission over the internet. It's easily readable and writable by humans and parseable and generatable by machines.
        - What is serialisation ?
            - Serialization is converting a Python data structure into a JSON string, enabling storage or transmission in a format easily reconstructed later.
        - What is Deserialization ?
            - Deserialization converts a JSON string back into a Python data structure, allowing its use within a Python program.
        - How to Convert Between Python and JSON :
            - Python provides modules like json for serializing and deserializing JSON data. json.dumps() converts a Python object to a JSON string, while json.loads() converts a JSON string to a Python object.
    
    **Accessing Command Line Parameters in a Python Script**
        - You can access command line parameters passed to a Python script using the sys.argv list provided by the sys module :
            - `import sys

                    script_name = sys.argv[0]
                    first_parameter = sys.argv[1]
                    second_parameter = sys.argv[2]`
    
## Requirements 💾
Python Script :
- We are not allowed to import module.
- Respect the pycodestyle.
- All files must be executable.
- Use #!/usr/bin/python3

Python Test Cases :
- All test files should be inside a folder tests
- All test files should be text files (extension: .txt)
- All tests should be executed by using this command: python3 -m doctest ./tests/*
- All class, modules and functions should have a documentation

## Tasks : 
0. Read File:
    - Create a function to read the content of a text file and print it to stdout.
    - Use the with statement for file operations to ensure automatic closure after use.
1. Write to a File:
    - Implement a function to write a string to a text file and return the number of characters written.
    - Utilize the with statement for file operations to guarantee proper file handling and closure.
2. Append to a File:
    - Develop a function to append a string to the end of a text file and return the number of characters added.
    - If the file does not exist, it should be created.
    - Use the with statement for file operations for proper file handling.
3. To JSON String:
    - Write a function to return the JSON representation of an object (string).
4. From JSON String to Object:
    - Implement a function to return an object represented by a JSON string.
5. Save Object to a File:
    - Create a function to write an Object to a text file using a JSON representation.
    - Utilize the with statement for file operations for proper file handling.
6. Create Object from a JSON File:
    - Develop a function to create an Object from a JSON file.
    - Use the with statement for file operations for proper file handling.
7. Load, Add, Save:
    - Write a script that adds all arguments to a Python list and saves them to a file.
    - Use the functions save_to_json_file and load_from_json_file for file operations.
8. Class to JSON:
    - Create a function to return the dictionary description for JSON serialization of an object.
9. Student to JSON:
    - Define a class Student with public instance attributes and a method to retrieve a dictionary representation.
10. Student to JSON with Filter:
    - Define a class Student with a method to retrieve a dictionary representation based on specified attributes.
11. Student to Disk and Reload:
    - Define a class Student with methods for serialization and deserialization to/from a JSON file.
    - Utilize the functions save_to_json_file and load_from_json_file for file operations.
12. Pascal's Triangle:
    - Implement a function to generate Pascal's triangle and return it as a list of lists of integers.

## Authors 🧞‍♀️
Sarah Boutier