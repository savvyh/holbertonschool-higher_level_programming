# Python - Inheritance

![_bfc0be89-0e88-4460-96e8-504b7044ab81](https://github.com/savvyh/holbertonschool-higher_level_programming/assets/139894873/131edce9-b11c-4488-834a-2313dbf38cad)


## General 🐍
A superclass, base class, or parent class is a class from which other classes, called subclasses, inherit attributes and methods. A subclass is a class that inherits attributes and methods from its superclass. To list all attributes and methods of a class or instance, you can use the dir() function in Python. An instance can have new attributes when they are defined within the instance itself or when they are added dynamically during runtime. To inherit a class from another, you use the syntax class SubClass(SuperClass):. You can define a class with multiple base classes by listing them within parentheses after the subclass name, separated by commas. The default class every class inherits from in Python is object. You can override a method or attribute inherited from the base class by redefining it in the subclass with the same name. Attributes or methods available by inheritance to subclasses are those that are not marked private (with a double underscore prefix). The purpose of inheritance is to promote code reusability and create a hierarchy of classes with shared functionality. The isinstance(), issubclass(), type(), and super() built-in functions are used for various purposes in Python. isinstance() is used to check if an object is an instance of a particular class, issubclass() is used to check if a class is a subclass of another class, type() is used to get the type of an object, and super() is used to access methods and attributes of the superclass within the subclass.

## Requirements ⛏️
* We are not allowed to import module.
* Respect the pycodestyle.
* All files must be executable.
* Use #!/usr/bin/python3
* Modules, classes and functions shoukd have a documentation

### Tasks 🥇
0. Lookup : 
    - Write a function that returns the list of available attributes and methods of an object. Return a list object
0. My list : 
    - Write a class MyList that inherits from list
0. Exact same object : 
    - Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
0. Same class or inherit from : 
    - Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
0. Only sub class of : 
    - Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
0. Geometry module : 
    - Write an empty class BaseGeometry.
0. Improve Geometry : 
    - Write a class BaseGeometry (based on 5-base_geometry.py).
0. Integer validator : 
    - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
0. Full rectangle : 
    - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
0. Square #1 : 
    - Write a class Square that inherits from Rectangle (9-rectangle.py):
0.  Square #2
    - Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

## Authors 🧞‍♀️
Sarah Boutier
