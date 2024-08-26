"""
    Singleton Design Pattern
        - Ensure a class only has one instance, and provides global point access to it.
"""


# First Way to Implement Singleton Pattern (Without MetaClasses)
class A:
    # Private class variable to store the single instance
    __instance = None

    def __init__(self):
        # Prevent direct instantiation by raising an error
        raise RuntimeError('call get_instance() instead')

    @classmethod
    def get_instance(cls):
        # Class method to get the single instance
        if cls.__instance is None:
            # If the instance does not exist, create it
            cls.__instance = cls.__new__(cls)  # Create a new instance without calling __init__

        return cls.__instance  # Return the existing instance


# Example Usage of Singleton A
# Trying to create an instance directly will raise an error
# b = A()  # Uncommenting this line will raise RuntimeError

# Correct way to create/get the instance using get_instance()
a1 = A.get_instance()
a2 = A.get_instance()

# Both instances should have the same memory address, proving that only one instance exists
print(id(a1), id(a2))  # Output: (e.g., 140569349076272 140569349076272)


###############################################################
# Second Way to Implement Singleton Pattern (Using Meta classes)

# Define a metaclass for Singleton
class Singleton(type):
    # Private class variable to store the single instance
    __instance = None

    def __call__(self, *args, **kwargs):
        # Override the __call__ method to control instantiation
        if self.__instance is None:
            # If the instance does not exist, create it using the parent __call__ method
            self.__instance = super().__call__(*args, **kwargs)

        return self.__instance  # Return the existing instance


# Define a class B that uses Singleton metaclass
class B(metaclass=Singleton):
    pass  # This class doesn't need to do anything special


# Example Usage of Singleton B
b1 = B()
b2 = B()

# Both instances should have the same memory address, proving that only one instance exists
print(id(b1), id(b2))  # Output: (e.g., 125838582344944 125838582344944)
