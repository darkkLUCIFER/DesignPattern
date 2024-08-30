"""
    Builder Design Pattern
    - builder is a creational design pattern that lets you construct complex objects step by step.
      The pattern allows you to produce different types and representations of an object using the same
      construction code.
"""
from abc import ABC, abstractmethod

# global car type registry
_car_type_registry = {}


# Decorator to register car types
def register_car_type(car_type: str):
    def decorator(cls):
        # Add the class to the registry
        _car_type_registry[car_type] = cls
        return cls

    return decorator


# Product class
class Car:
    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel):
        self._wheel = wheel
        return self

    def set_engine(self, engine):
        self._engine = engine
        return self

    def set_body(self, body):
        self._body = body
        return self

    def detail(self):
        print(f"body: {self._body.shape}")
        print(f"engine: {self._engine.hp}")
        print(f"wheel: {self._wheel.size}")


# Abstract Builder class
class AbstractBuilder(ABC):

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_body(self):
        pass


@register_car_type("Benz")
class Benz(AbstractBuilder):  # Concrete Builder 1
    def get_engine(self):
        return Engine(500)

    def get_wheel(self):
        return Wheel(22)

    def get_body(self):
        return Body("Suv")


@register_car_type("Bmw")
class Bmw(AbstractBuilder):  # Concrete Builder 2
    def get_engine(self):
        return Engine(1000)

    def get_wheel(self):
        return Wheel(30)

    def get_body(self):
        return Body("sedan")


class Wheel:
    def __init__(self, size: int):
        self.size = size


class Body:
    def __init__(self, shape: str):
        self.shape = shape


class Engine:
    def __init__(self, hp: int):
        self.hp = hp


class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        car = Car()

        body = self._builder.get_body()
        car.set_body(body)

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        return car


def client_builder(builder: str):
    # Check if builder is registered
    if builder not in _car_type_registry:
        raise ValueError(f"unknown builder: {builder}")

    # Get builder from registry
    car = _car_type_registry[builder]()

    # Create director
    director = Director()
    director.set_builder(car)

    # Construct car
    result = director.construct()
    return result.detail()


# Usage Sample
client_builder("Bmw")

# output:
# body: sedan
# engine: 1000
# wheel: 30
