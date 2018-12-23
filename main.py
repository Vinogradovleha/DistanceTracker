from math import hypot


points_list = [
    (1.1, 1.33),
    (2.11, 2.88),
    (3, 3.66),
    (-1, -5.33),
    (0.1, 0.33),
]


class Point(object):
    def __init__(self, x, y):
        self.x = self.to_int(x)
        self.y = self.to_int(y)

    def to_int(self, source):
        try:
            return float(source)
        except ValueError:
            raise Exception('Wrong type: %s! Must be int.' % source)

    def distance_to(self, to_point):
        return hypot(to_point.x - self.x, to_point.y - self.y)


def main(*args, **kwargs):
    if len(points_list) < 2:
        raise Exception('Must be more then 1 point in point_list: %s' % points_list)

    current_point = Point(*points_list.pop(0))
    total_distance = 0

    for x_value, y_value in points_list:
        next_point = Point(x_value, y_value)

        total_distance += current_point.distance_to(next_point)
        current_point = next_point

    print('Distance: %s' % total_distance)


main()
