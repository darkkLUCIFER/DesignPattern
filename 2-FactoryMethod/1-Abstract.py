"""
    Abstract class, Abstract Method
"""
from abc import ABC, abstractmethod


# Define an abstract class A that inherits from ABC
class A(ABC):
    # Define an abstract method 'show' which must be implemented by any subclass
    @abstractmethod
    def show(self):
        # This method can still have an implementation, but subclasses must override it
        print("A")


# Define class B that inherits from abstract class A
class B(A):
    # Implement the abstract method 'show' from class A
    def show(self):
        # Call the 'show' method of the superclass A (optional)
        super().show()
        # Print "B" specific to class B
        print("B")


# Create an instance of class B
b1 = B()
# Call the 'show' method on the instance b1
b1.show()

# output:
# A
# B
