from math import hypot


class Point(object):
    def __init__(self):
        raw_x_value = self.request_coordinate('x')
        self.x = self.to_int(raw_x_value)

        raw_y_value = self.request_coordinate('y')
        self.y = self.to_int(raw_y_value)

    def request_coordinate(self, name):
        return input("Enter %s:" % name)

    def to_int(self, source):
        try:
            return int(source)
        except ValueError:
            raise Exception('Wrong type: %s! Must be int.' % source)

    def distance_to(self, to_point):
        return hypot(to_point.x - self.x, to_point.y - self.y)


def main(*args, **kwargs):
    print('First point:')
    first_point = Point()

    print('Second point:')
    second_point = Point()

    distance = first_point.distance_to(second_point)

    print('Distance: %s' % distance)


main()
