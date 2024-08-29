"""
    Prototype Design Pattern
    - Prototype is a creational design pattern that lets you copy existing objects
      without making your code dependent on their classes.
"""
import copy


# Prototype class
class Prototype:
    def __init__(self):
        # Dictionary to store registered objects
        self._objects = {}

    # Method to register an object
    def register(self, name, obj):
        # Store the object in the dictionary with a given name
        self._objects[name] = obj

    # Method to unregister an object
    def unregister(self, name):
        # Remove the object from the dictionary
        del self._objects[name]

    # Method to clone a registered object
    def clone(self, name, **kwargs):
        # Create a deep copy of the object
        cloned_obj = copy.deepcopy(self._objects.get(name))
        # Update the cloned object's attributes with new values
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


# Client part
def client_prototype(name, obj, **kwargs):
    # Create a Prototype instance
    prototype = Prototype()
    # Register the object
    prototype.register(name, obj)
    # Clone the object
    return prototype.clone(name, **kwargs)


# Usage example
class Person:
    def __init__(self, name, age):
        # Initialize the Person object's attributes
        self.name = name
        self.age = age


# Create a Person object
p1 = Person('John', 25)

# Clone the Person object
p_clone = client_prototype('p1', p1)
# Print the cloned object's attributes
print(p_clone.__dict__)  # {'name': 'John', 'age': 25}

# Clone the Person object with new attributes
new_clone = client_prototype('new', p1, age=15)
# Print the cloned object's attributes
print(new_clone.__dict__)  # {'name': 'John', 'age': 15}

# Print the IDs of the objects attributes
# Same ID for the 'name' attribute, since it's the same string
print(id(p1.name))  # 125112205454112
print(id(p_clone.name))  # 125112205454112

# Different ID for the 'age' attribute, since it's a new integer
print(id(p1.age))  # 11758760
print(id(new_clone.age))  # 11758440
