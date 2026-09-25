# ============================================================
# DUNDER METHODS IN PYTHON
# ============================================================

"""
Dunder Methods
--------------

Dunder methods are also known as Magic Methods.

"Dunder" stands for "Double Underscore" because these methods
start and end with double underscores.

Examples:
    __init__
    __str__
    __add__
    __sub__
    __eq__

Dunder methods are special methods that Python calls
automatically when we perform certain operations on objects.

They help us:
    - Customize the behavior of our classes.
    - Make our objects work with Python's built-in operations.
    - Define how objects should behave with operators,
      print(), comparisons, etc.
"""


# ============================================================
# 1. __init__ METHOD
# ============================================================

"""
__init__
--------

__init__ is a special method that is automatically called
when an object is created.

It is commonly used to initialize the object's attributes.

In this example:
    Animal("Lion")

automatically calls:

    __init__(self, "Lion")
"""

class Animal:

    def __init__(self, name):
        # 'self.name' stores the name inside the object.
        self.name = name


# Creating an object of the Animal class
obj = Animal("Lion")

# 'obj' refers to the Animal object created above.
print(obj)

"""
Output will look similar to:

<__main__.Animal object at 0x000001...>

Why?

We have not defined __str__ yet.

Therefore, print(obj) uses Python's default object
representation, which includes the class name and
an object-related memory representation.
"""


# ============================================================
# 2. __str__ METHOD
# ============================================================

"""
__str__
-------

__str__ defines what should be returned when we convert
an object into a readable string.

It is automatically called when we use:

    print(obj)

For example:

    print(obj)

is internally similar to:

    obj.__str__()
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        # Return a user-friendly string representation
        # of the object.
        return f"My name is {self.name}"


# Creating objects
obj = Animal("Lion")
obj2 = Animal("Tiger")

# print() automatically calls __str__()
print(obj)
print(obj2)

"""
Output:

My name is Lion
My name is Tiger
"""


# ============================================================
# 3. __add__ METHOD
# ============================================================

"""
__add__
-------

__add__ defines what the '+' operator should do when
it is used with objects of our class.

For example:

    num1 + num2

Python automatically calls:

    num1.__add__(num2)

Without defining __add__, Python does not know how to
perform '+' between two objects of our custom class.
"""


class Numbers:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        # 'other' represents the second object.
        #
        # For:
        #     num1 + num2
        #
        # self  -> num1
        # other -> num2
        #
        # So we add their 'num' values.
        return self.num + other.num

    def __sub__(self, other):
        # Defines the behavior of '-' between two objects.
        #
        # For:
        #     num1 - num2
        #
        # Python calls:
        #     num1.__sub__(num2)
        return self.num - other.num

    def __eq__(self, other):
        # Defines the behavior of '==' between two objects.
        #
        # For:
        #     num1 == num2
        #
        # Python calls:
        #     num1.__eq__(num2)
        return self.num == other.num


# Creating two objects
num1 = Numbers(30)
num2 = Numbers(30)


# ------------------------------------------------------------
# Using the overloaded operators
# ------------------------------------------------------------

# '+' automatically calls __add__()
print("Addition:", num1 + num2)

# '-' automatically calls __sub__()
print("Subtraction:", num1 - num2)

# '==' automatically calls __eq__()
print("Are they equal?", num1 == num2)


"""
Output:

Addition: 60
Subtraction: 0
Are they equal? True
"""


# ============================================================
# IMPORTANT CONCEPT
# ============================================================

"""
When we write:

    num1 + num2

Python internally calls:

    num1.__add__(num2)


When we write:

    num1 - num2

Python internally calls:

    num1.__sub__(num2)


When we write:

    num1 == num2

Python internally calls:

    num1.__eq__(num2)


This allows us to define how operators should behave
for our own classes.
"""