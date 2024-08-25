"""
    __new__
"""


# example of using method __new__
class A:

    def __new__(cls, name, *args, **kwargs):
        if name == 'john':
            return None
        else:
            return super().__new__(cls, *args, **kwargs)

    def __init__(self, name):
        self.name = name


# make instance with random name
a1 = A('wick')
print(a1)
# output: <__main__.A object at 0x71c5301fe390>

# make instance with name john
a2 = A('john')
print(a2)
# output: None
