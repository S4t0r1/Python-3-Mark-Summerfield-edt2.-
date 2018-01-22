
"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:
    
    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y
    
    
    @property
    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)
    
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    
    def __repr__(self):
        return ("{0.__class__.__name__}({0.x!r}, {0.y!r})".format(self))
    
    
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):
    
    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super.__init__(x, y)
        self.radius = radius
    
    
    @property
    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin - self.radius)
    
    
    @property
    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)
    
    
    @property
    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius

    
    @property
    def radius(self):
        """The circle's radius

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle.radius = 6
        """
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be non-zero or non-negative"
        self.__radius = radius
    
    
    def __eq__(self, other):
        return self.radius == other.radius and super.__eq__(other)
    
    
    def __repr__(self):
        return ("{0.__class__.__name__}({0.radius!r}, {0.x!r}, " 
                "{0.y!r})".format(self))
    


if __name__ == "__main__":
    import doctest
    doctest.testmod()
