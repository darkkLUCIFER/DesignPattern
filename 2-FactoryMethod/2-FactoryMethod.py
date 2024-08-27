"""
    Factory Method Design Pattern
    - Factory is a creational design pattern that provides an interface to creating objects
      in a superclass, but allows subclasses to alter the type of objects that will be created.

    Three parts ⇒ 1. Creator, 2. Product, 3. Client
"""
from abc import ABC, abstractmethod

# Global registry for formats
_format_registry = {}


def register_format(format_name):
    """
    Decorator to register a new format.
    """

    def decorator(cls):
        _format_registry[format_name] = cls
        return cls

    return decorator


# Creator Part
class File(ABC):
    """
        The 'Creator' class declares the factory method 'make' that returns an object of type 'Product'.
        Subclasses usually implement this method to create specific product objects.
    """

    def __init__(self, file):
        self.file = file

    # Abstract factory method that subclasses must implement
    @abstractmethod
    def make(self):
        pass

    # Common logic that uses the product created by the factory method
    def call_edit(self):
        # Call the factory method to get the product object
        product = self.make()
        # Use the product object to perform some operation
        result = product.edit(self.file)
        return result


# Concrete Creator classes that implement the factory method to return a specific product object
@register_format('json')
class JsonFile(File):
    def make(self):
        return Json()


@register_format('xml')
class XmlFile(File):
    def make(self):
        return Xml()


# Product Part
class Json:
    """
        The 'Product' class represents a type of object the factory method creates.
    """

    def edit(self, file):
        # Some operation specific to the JSON product
        return f"working on {file} Json..."


class Xml:
    def edit(self, file):
        return f"working on {file} XML..."


# Client Part
def client(file, format):
    """
        The 'Client' code that interacts with the creator class via the factory method.
        It doesn't need to know the specific class of the product object it works with.
    """
    if format not in _format_registry:
        raise ValueError(f"Unknown format: {format}")

    # Instantiate the appropriate Creator class based on the format
    result = _format_registry[format](file)

    # Use the product created by the factory method
    return result.call_edit()


# Example usage of the client function
print(client("show", "json"))


# output: working on show Json...


# Add a new format without modifying the client code
@register_format("yaml")
class YamlFile(File):
    def make(self):
        return Yaml()


class Yaml:
    def edit(self, file):
        return f"working on {file} YAML..."


print(client("config", "yaml"))
# output: working on config YAML...
