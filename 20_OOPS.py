'''
Classes:
--------
    Class is an blueprint/ Template of an object
    Syntax:
        class Class_Name:
    We can create objects from it.
        obj_name=Class_Name()  
Object:
--------
    An Object is an actual instance created from a class

Constructor:
-------------
    It is a special method used to initialize objects which is created from the class.
    Object creation and initialization are handled through the __new__() and __init__() methods.

    i) The__new__():
        created and returns new instance of the class
        it allocates the memory and return new OBJECTS.
        it is called before __init__

        class ClassName:
        def __new__(cls, parameters):
            instance = super(ClassName, cls).__new__(cls)
            return instance

    ii) __init__():
        This method initializes the newly created instance and is commonly used as a Constructor in python
        It is called after the ceation of object by the __new__()
        It is resbonsible for initializing the attributes of the instance
        
        class ClassName:
        def __init__(self, parameters):
            self.attribute = value

Types of Constructor
--------------------

    ✨Default Constructor
        does not take any parameters other than self. It initializes the object with default attribute values.
    ✨Parameterized Constructor
        accepts arguments to initialize the object's attributes with specific values.


'''
# DEFAULT CONSTRUCTOR
class Car:
    def __init__(self):

        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

# PARAMETERIZED CONSTRUCTOR
car = Car()
print(car.make)
print(car.model)
print(car.year)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)

'''
Instance Attribute:
------------------
    An instance attribute is the data which is belongs to an particuular object
'''
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Abirami", 22)
student2 = Student("Priya", 21)
print(student1.name)
print(student2.name)

'''
Class Attribute:
------------------
    A Class attribute is the data which is belongs to a class and is shared by all object
'''
class Student:
    college="ACGCET"
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Abirami", 22)
student2 = Student("Priya", 21)
print(student1.name)
print(student2.name)
print(student1.college)
print(student2.college)

''''
SELF:
-----
    This is one of the most important concepts in python OOP
    self means the current object

Pattern:
---------
    class ClassName:

        def __init__(self, data):
            self.data = data

        def method(self):
            print(self.data)
    object1 = ClassName(value)
    object1.method()
'''

