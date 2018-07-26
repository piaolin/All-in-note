import math

class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        (self.x, self.y) = (x, y)
    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
    def get_len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def normalize(self):
        it = self.get_len()
        self.x /= it
        self.y /= it
    def __add__(self, other):
        third = Vector()
        third.x = self.x + other.x
        third.y = self.y + other.y
        return third
    def __sub__(self, other):
        third = Vector()
        third.x = self.x - other.x
        third.y = self.y - other.y
        return third
    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)
    def __div__(self, other):
        if other != 0:
            return Vector(self.x/other, self.y/other)
        else:
            return Vector(self.x, self.y)
    def getpos(self):
        return (self.x, self.y)
    