Python - Classes
![Uploading _c25c8515-cd33-47ed-8c66-5272c80524ef.jpg…]()

## General 🐍
* OOP : OOP stands for Object-Oriented Programming. It is a programming paradigm that uses objects, which bundle data and methods, to design and organize code.
* first-class everything : This phrase refers to the concept that in a programming language, everything, including functions and classes, is treated as a first-class citizen, allowing them to be assigned to variables, passed as arguments, and returned from functions.
* Class : A class is a blueprint for creating objects. It defines a data structure along with methods to operate on that data.
* Object and instance : An object is an instance of a class. An instance is a specific realization of a class, created from the class blueprint.
* What the difference between a class and an object or instance? A class is a blueprint or template, while an object (or instance) is a concrete entity created from that blueprint.
* Attribute : An attribute is a piece of data that belongs to a class or an object. It represents a characteristic or property.
* How to use public, protected, and private attributes? Public attributes are accessible from outside the class. Protected attributes (single underscore) are accessible within the class and its subclasses. Private attributes (double underscore) are name-mangled to make them less accessible from outside the class.
* `self` : Convention in Python that represents the instance of a class. It is the first parameter in the methods of a class and refers to the instance itself.
* Method : A method is a function defined within a class. It operates on the data associated with the class and can be called on instances of the class.
* Init method : __init__ is a special method in Python classes used for initializing object attributes. It is called automatically when an instance is created.
* Data Abstraction, Data Encapsulation, and Information Hiding : Data Abstraction involves presenting only essential information and hiding implementation details. Data Encapsulation bundles the data and the methods that operate on that data. Information Hiding is the practice of restricting access to certain details of an object.
* Property : In Python, a property is a special kind of attribute managed by getter, setter, and deleter methods. It allows controlling access to an attribute.
* What is the difference between an attribute and a property in Python? An attribute is a data member of a class, while a property is a special kind of attribute with associated getter, setter, and deleter methods.
* Pythonic way to write getters and setters in Python? Use the @property, @attribute.setter, and @attribute.deleter decorators to define getter, setter, and deleter methods for a property.
* What is the dict of a class and/or instance of a class and what does it contain? __dict__ is a dictionary containing the namespace of a class or instance. It stores the attributes and their values.
* `getattr` : `getattr(object, 'attribute')` is used to get the value of the specified attribute of an object. If the attribute is not found, a default value can be provided as the third argument.

## Requierements ☝️
- We are not allowed to import module.
- Respect the pycodestyle.
- All files must be executable.
- Use #!/usr/bin/python3
- Modules, classes and functions shoukd have a documentation

### Tasks 🥇
- Task 0 : Write an empty class that defines a square
- Task 1 : Write a class that defines a square by: (based on 0-square.py) Private instance attribute: `size`and instantiation with `size` (no type/value verification)
- Task 2 : Write a class that defines a square by: (based on 1-square.py) Private instance attribute: `size`and instantiation with `size` def __init__(self, size=0):
- Task 3 : Write a class that defines a square by: (based on 2-square.py) Private instance attribute: `size`, instantiation with `size` def __init__(self, size=0) and public instance method: def area(self).
- Task 4 : Write a class that defines a square by: (based on 3-square.py) Private instance attribute: `size`, instantiation with `size` def __init__(self, size=0) and public instance method: def area(self).
- Task 5 :  Write a class that defines a square by: (based on 4-square.py) Private instance attribute: `size`, instantiation with `size` def __init__(self, size=0) and public instance method: def area(self) and def my_print(self)
- Task 6 : Write a class that defines a square by: (based on 5-square.py) Private instance attribute: `size`, instantiation with `size` def __init__(self, size=0) and public instance method: def area(self) and def my_print(self)

Authors 🧞‍♀️
Sarah Boutier
