from math import (
    asin,
    cos,
    sin,
    sqrt,
    radians,
)


points_list = [
    (53.8547566, 27.4459583),
    (53.9338766, 27.6491833),
    (53.8980066, 27.58423),
    (53.9050033, 27.452975),
]


class GPSPoint(object):
    EARTH_RADIUS_KM = 6371.221

    def __init__(self, lat, lon):
        self.lat = self.to_float(lat)
        self.lon = self.to_float(lon)

    def to_float(self, source):
        try:
            return float(source)
        except ValueError:
            raise Exception('Wrong type: %s! Must be int.' % source)

    def distance_to(self, to_point):
        rad_lat_from, rad_lon_from, rad_lat_to, rad_lon_to = map(
            radians,
            (self.lat, self.lon, to_point.lat, to_point.lon)
        )

        # haversine formula
        dlon = rad_lon_to - rad_lon_from
        dlat = rad_lat_to - rad_lat_from

        sphere_radius = sin(dlat / 2) ** 2 + cos(rad_lat_from) * cos(rad_lat_to) * sin(dlon / 2) ** 2

        km = self.EARTH_RADIUS_KM * 2 * asin(sqrt(sphere_radius))
        return km


def main(*args, **kwargs):
    if len(points_list) < 2:
        raise Exception('Must be more then 1 point in point_list: %s' % points_list)

    current_point = GPSPoint(*points_list.pop(0))
    total_distance = 0

    for x_value, y_value in points_list:
        next_point = GPSPoint(x_value, y_value)

        total_distance += current_point.distance_to(next_point)
        current_point = next_point

    print('Distance (km): %s' % total_distance)


main()
