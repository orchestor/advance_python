"""
Given
v1 = Vector(1, 2)
v2 = Vector(2, 3)

then 
v3 = v1 + v2 = Vector(3, 5)
"""

from math import hypot
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __repr__(self):
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)

    def __abs__(self):
        return hypot(self._x, self._y)

    def __mul__(self, scalar):
        return Vector(self._x*scalar, self._y*scalar)
