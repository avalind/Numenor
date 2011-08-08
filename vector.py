#!/usr/bin/env python
import math

class Vector(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)

  def __mul__(self, scalef):
    return Vector(self.x * scalef, self.y * scalef)

  def length(self):
    length_squared = self.x**2 + self.y**2
    return math.sqrt(length_squared)

  def length_squared(self):
    return self.x**2 + self.y**2

  def normalized(self):
    fac = self.length()
    return Vector(self.x / fac, self.y / fac)

  def __repr__(self):
    return "(%f, %f)" % (self.x, self.y)

  def __str__(self):
    return self.__repr__()

def dot(a,b):
  return a.x*b.x + a.y*b.y


