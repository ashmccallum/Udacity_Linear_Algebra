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


def add(vector1, vector2):

    output = []

    for x in range(vector1.dimension):
        output.insert(x, vector1.coordinates[x] + vector2.coordinates[x])

    return output

def minus(vector1, vector2):

    output = []

    for x in range(vector1.dimension):
        output.insert(x, vector1.coordinates[x] - vector2.coordinates[x])

    return output

def scalar(scalar, vector):

    output = []

    for x in range(vector.dimension):
        output.insert(x, vector.coordinates[x] * scalar)

    return output

add_vector = Vector([8.218, -9.341])
add_vector2 = Vector([-1.129, 2.111])

minus_vector = Vector([7.119, 8.215])
minus_vector2 = Vector([-8.223, 0.878])

scalar_num = 7.41
scalar_vector = Vector([1.671, -1.012, -0.318])

print add(add_vector, add_vector2)
print minus(minus_vector, minus_vector2)
print scalar(scalar_num, scalar_vector)
