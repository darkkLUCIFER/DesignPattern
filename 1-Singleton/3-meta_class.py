"""
    Meta Class
"""


class Singleton(type):
    _instances = None

    def __call__(self, *args, **kwargs):
        if self._instances is None:
            self._instances = super().__call__(*args, **kwargs)

        return self._instances


class Db(metaclass=Singleton):
    pass


db1 = Db()
db2 = Db()

print(id(db1), id(db2))
# output: 124718218732768 124718218732768
