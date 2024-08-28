"""
    Abstract Factory Design Pattern
    - Abstract Factory Pattern servers to provide an interface for creating related/dependent
      objects without the need to specify their actual class.

      Car ⇒ Benz, Bmw ⇒ Suv, Coupe
            benz suv ⇒ gla (product)
            bmw suv ⇒ x1 (product)
            benz coupe ⇒ cls (product)
            bmw coupe ⇒ M2 (product)
"""

from abc import ABC, abstractmethod

# global registry for car class types
_class_type_registry = {}


# Decorator to register a class type
def register_class_type(class_type: str):
    """
    Decorator to register a class type
    :param class_type
    """

    def decorator(cls):
        # Add the class to the registry
        _class_type_registry[class_type] = cls
        return cls

    return decorator


# Creator Part
class Car(ABC):  # Abstract Factory
    """
        This is the abstract factory class that defines the interface for creating cars.
    """

    @abstractmethod
    def call_suv(self):
        """
            This method must be implemented by concrete factories to create an SUV.
        """
        pass

    @abstractmethod
    def call_coupe(self):
        """
            This method must be implemented by concrete factories to create a Coupe.
        """
        pass


@register_class_type('Benz')
class Benz(Car):  # Concrete Factory 1
    """
        This is a concrete factory class that creates Benz cars.
    """
    def call_suv(self):
        # Create a Benz SUV (Gla)
        return Gla()

    def call_coupe(self):
        # Create a Benz Coupe (Cls)
        return Cls()


@register_class_type('Bmw')
class Bmw(Car):  # Concrete Factory 2
    """
        This is a concrete factory class that creates BMW cars.
    """
    def call_suv(self):
        # Create a BMW SUV (X1)
        return X1()

    def call_coupe(self):
        # Create a BMW Coupe (M2)
        return M2()


# Product Part
class Suv(ABC):  # Abstract Product A
    """
        This is the abstract product class that defines the interface for SUVs.
    """

    @abstractmethod
    def create_suv(self):
        """
            This method must be implemented by concrete SUVs to create an SUV.
        """
        pass


class Coupe(ABC):  # Abstract Product B
    """
        This is the abstract product class that defines the interface for Coupes.
    """

    @abstractmethod
    def create_coupe(self):
        """
            This method must be implemented by concrete Coupes to create a Coupe.
        """
        pass


class Gla(Suv):  # Concrete Product A1
    """
        This is a concrete SUV class that creates a Benz Gla SUV.
    """
    def create_suv(self):
        # Create a Benz Gla SUV
        print('this is your suv benz gla...')


class X1(Suv):  # Concrete product B1
    """
        This is a concrete SUV class that creates a BMW X1 SUV.
    """
    def create_suv(self):
        # Create a BMW X1 SUV
        print('this is your suv bmw X1...')


class Cls(Coupe):  # Concrete product A2
    """
        This is a concrete Coupe class that creates a Benz Cls Coupe.
    """
    def create_coupe(self):
        # Create a Benz Cls Coupe
        print('this is your coupe benz Cls...')


class M2(Coupe):  # Concrete product B2
    """
        This is a concrete Coupe class that creates a BMW M2 Coupe.
    """
    def create_coupe(self):
        # Create a BMW M2 Coupe
        print('this is your coupe bmw M2...')


# Client Part
def client_suv(class_type: str):  # Client
    """
        This client function creates an SUV using the specified class type.
        :param class_type
    """
    if class_type not in _class_type_registry:
        # Raise an error if the class type is unknown
        raise ValueError(f"unknown class type: {class_type}")
    # Create an SUV using the specified class type
    suv = _class_type_registry[class_type]().call_suv()
    # Use the SUV product
    suv.create_suv()


def client_coupe(class_type: str):  # Client
    """
        This client function creates a Coupe using the specified class type.
        :param class_type
    """
    if class_type not in _class_type_registry:
        # Raise an error if the class type is unknown
        raise ValueError(f"unknown class type: {class_type}")
    # Create a Coupe using the specified class
    coupe = _class_type_registry[class_type]().call_coupe()
    # Use the Coupe product
    coupe.create_coupe()


# Test the client methods
client_suv("Benz")
# output: this is your suv benz gla...

client_coupe("Bmw")
# output: this is your coupe bmw M2...
