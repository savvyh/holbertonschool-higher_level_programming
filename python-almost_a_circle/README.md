# Python - Almost a Circle

![_35f54180-c558-4289-8ffa-0718d51a905b](https://github.com/savvyh/holbertonschool-higher_level_programming/assets/139894873/f83ae043-5916-4f18-b102-867193341331)

## General 🐍

Here is a new project about Python. This project offers a comprehensive review of essential Python concepts, covering topics such as importing modules, handling exceptions, defining classes with private attributes and methods, implementing getters and setters, utilizing class methods and static methods, exploring inheritance, performing unit testing, and reading/writing files. 
Additionally, participants will delve into more advanced concepts including working with `*args `and `**kwargs`, serialization and deserialization techniques, and handling JSON data.

### Step by step ⚔️

- Write the first class Base
- Write the class Rectangle that inherits from Base
- Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
- Update the class Rectangle by adding the public method `def area(self):` that returns the area value of the Rectangle instance
- Update the class Rectangle by adding the public method `def display(self):` that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
- Update the class Rectangle by overriding the `str` method so that it returns `[Rectangle]` instance
- Update the class Rectangle by improving the public method `def display(self):` to print in stdout the Rectangle instance with the character # by taking care of x and y
- Update the class Rectangle by adding the public method `def update(self, *args):` that assigns an argument to each attribute
- Update the class Rectangle by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, kwargs)` that assigns a key/value argument to attributes
- Write the class Square that inherits from Rectangle
- Update the class Square by adding the public getter and setter `size`
- Update the class Square by adding the public method `def update(self, *args, kwargs):` that assigns attributes
- Update the class Rectangle by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle
- Update the class Square by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Square
- Update the class Base by adding the class method `def savetofile(cls, listobjs):` that writes the JSON string representation of `listobjs` to a file
- Update the class Base by adding the static method `def fromjsonstring(jsonstring):` that returns the list of the JSON string representation `jsonstring`
- Update the class Base by adding the class method `def create(cls, dictionary):` that returns an instance with all attributes already set
- Update the class Base by adding the class method `def loadfromfile(cls):` that returns a list of instances

### Objectives :astronaut:
- What is Unit testing and how to implement it in a large project ?
    - Unit testing involves validating individual components of code to ensure their correctness. In a large project, unit testing is crucial for maintaining code quality and catching bugs early. It is typically implemented using frameworks like Pytest or unittest, where tests are written to verify the behavior of each unit of code.
- How to serialize and deserialize a Class ?
    - Serialization is the process of converting an object into a format that can be stored or transmitted, while deserialization involves reconstructing the object from its serialized form. In Python, serialization and deserialization can be achieved using libraries such as Pickle or JSON.

- How to write and read a JSON file ?
    - In Python, writing and reading JSON files is straightforward using the built-in json module. To write data to a JSON file, you can use the json.dump() function, and to read data from a JSON file, you can use the json.load() function.

- What is `*args` and how to use it ?
    - `args` is a special syntax in Python that allows functions to accept a variable number of positional arguments. It collects all the positional arguments passed to the function into a tuple. To use `args`, simply prefix the parameter with an asterisk in the function definition : `*args`

- What is `**kwargs` and how to use it ?
    - `kwargs` is similar to `args`, but it collects variable numbers of keyword arguments into a dictionary instead of a tuple. This allows functions to accept an arbitrary number of keyword arguments. To use `kwargs`, prefix the parameter with two asterisks in the function definition : `**kwargs`

- How to handle named arguments in a function ?
    - Named arguments in a function are handled by explicitly specifying the parameter names when calling the function. This allows for greater clarity and readability, especially when dealing with functions that accept multiple arguments. In Python, named arguments are specified using the format `parameter_name=value` when calling the function.

## Requirements :alien:

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

### Tasks :arrow_heading_down:
0. If it's not tested it doesn't work : 
   - All files, classes and methods must be unit tested and be PEP 8 validated.
0. Base class : 
   - Write the first class `Base`.
0. First Rectangle : 
   - Write the class `Rectangle` that inherits from `Base`.
0. Validate attributes : 
   - Update the class `Rectangle` by adding validation of all setter methods and instantiation (id excluded).
0. Area first : 
   - Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.
0. Display #0 : 
   - Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#`.
0. __str__ : 
   - Update the class `Rectangle` by overriding the __str__ method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`, without `x`and `y`.
0. Display #1 : 
   - Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x`and `y`.
0. Update #0 : 
   - Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute: `id`, `width`, `height`, `x`and `y`.
0. Update #1 : 
   - Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument.
0. And now, the Square! : 
   - Write the class `Square` that inherits from `Rectangle`.
0. Square size : 
   - Update the class `Square` by adding the public getter and setter `size`.
0. Square update : 
   - Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes: `id`, `size`, `x`and `y`.
0. Rectangle instance to dictionary representation : 
   - Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`.
0. Square instance to dictionary representation : 
   - Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square` : `id`, `size`, `x`and `y`.
0. Dictionary to JSON string : 
   - Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`.
0. JSON string to file : 
   - Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file.
0. JSON string to dictionary : 
   - Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`.
0. Dictionary to Instance : 
   - Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set.
0. File to instances : 
   - Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances.

### Authors 🧞‍♀️
Sarah Boutier
