"""
    __call__
"""


# example of using method __call__

class A:
    def __call__(self, name, *args, **kwargs):
        print(name)


# make an instance and call it like a function

a1 = A()
a1('luci')

# output: luci
