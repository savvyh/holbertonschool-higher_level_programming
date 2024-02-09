# Python - More Classes

## General 🐍
Here is a project about classes. I ever did a project similar, so I will be concise for the general presentation and talk about new concept : 

* What are __str__ and __repr__ ?
__str__ and __repr__ are special methods used to define the string representation of an object. __str__ is used for informal string representation, while __repr__ is used for formal string representation.
What is the difference between str and repr?
__str__ is used for creating a human-readable string representation of an object, while __repr__ is used for creating a machine-readable string representation, typically used for debugging.
* What is a class attribute?
A class attribute is a variable that is associated with a class rather than any particular instance of the class.
* What is the difference between an object attribute and a class attribute?
An object attribute is specific to each instance of a class, while a class attribute is shared among all instances of the class.
* What is a class method?
A class method is a method that is bound to the class rather than an instance of the class.
* What is a static method?
A static method is a method that does not access or modify class or instance state. It is bound to the class, not to the instance.
* How to dynamically create arbitrary new attributes for existing instances of a class?
Attributes can be dynamically added to instances by simply assigning values to them using dot notation.
* How to bind attributes to objects and classes?
Attributes can be bound to objects by assigning values to them using dot notation. Class attributes can be bound to classes by directly defining them within the class definition.
* What is and what does contain dict of a class and of an instance of a class?
__dict__ is a dictionary containing the attributes (methods and variables) of an object or class.
* How does Python find the attributes of an object or class?
Python first looks for attributes in the instance namespace. If an attribute is not found, it then looks in the class namespace. If the attribute is still not found, it looks in the base classes.
* How to use the getattr function?
The getattr function is used to get the value of an attribute of an object by name. It takes the object and the attribute name as arguments. If the attribute does not exist, getattr raises an AttributeError or returns a default value if provided.

## Requierements ☝️
- We are not allowed to import module.
- Respect the pycodestyle.
- All files must be executable.
- Use #!/usr/bin/python3
- Modules, classes and functions shoukd have a documentation

### Tasks 📚
- The tasks of this project consist of creating a rectangle. 
- This rectangle is defined according to various instructions. 
- Each task refers to the previous task in order to improve this rectangle as the tasks progress.

### Authors 🧞‍♀️
Sarah Boutier