import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        output = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return output

    def minus(self, v):
        output = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return output

    def scalar(self, scalar):
        output = [scalar * x for x in self.coordinates]
        return Vector(output)

    def magnitude(self):
        coords_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coords_squared))

    def normalise(self):
        try:
            magnitude = self.magnitude()
            return self.scalar(1/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector')

add_vector = Vector([8.218, -9.341])
add_vector2 = Vector([-1.129, 2.111])
print add_vector.add(add_vector2)

minus_vector = Vector([7.119, 8.215])
minus_vector2 = Vector([-8.223, 0.878])
print minus_vector.minus(minus_vector2)

scalar_num = 7.41
scalar_vector = Vector([1.671, -1.012, -0.318])
print scalar_vector.scalar(scalar_num)

v = Vector([-0.221, 7.437])
print v.magnitude()

v = Vector([8.813, -1.331, -6.247])
print v.magnitude()

v = Vector([5.581, -2.136])
print v.normalise()

v = Vector([1.996, 3.108, -4.554])
print v.normalise()