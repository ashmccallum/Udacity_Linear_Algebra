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

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle(self, v):
        dot = self.dot(v)
        mags = self.magnitude() * v.magnitude()

        return math.acos(dot / mags)

add_vector = Vector([8.218, -9.341])
add_vector2 = Vector([-1.129, 2.111])
print add_vector.add(add_vector2)

minus_vector = Vector([7.119, 8.215])
minus_vector2 = Vector([-8.223, 0.878])
print minus_vector.minus(minus_vector2)

scalar_num = 7.41
scalar_vector = Vector([1.671, -1.012, -0.318])
print scalar_vector.scalar(scalar_num)

w = Vector([-0.221, 7.437])
print w.magnitude()

w = Vector([8.813, -1.331, -6.247])
print w.magnitude()

w = Vector([5.581, -2.136])
print w.normalise()

w = Vector([1.996, 3.108, -4.554])
print w.normalise()

w = Vector([7.887, 4.138])
y = Vector([-8.802, 6.776])
print w.dot(y)

w = Vector([-5.955, -4.904, -1.874])
y = Vector([-4.496, -8.755, 7.103])
print w.dot(y)

w = Vector([3.183, -7.627])
y = Vector([-2.668, 5.319])
print w.angle(y)

w = Vector([7.35, 0.221, 5.188])
y = Vector([2.751, 8.259, 3.985])
print w.angle(y) * 57.2958
