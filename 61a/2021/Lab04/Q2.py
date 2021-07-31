#distance.py, summer 2021
from math import sqrt
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"
    x1=get_lot(city_a)
    y1=get_lat(city_a)
    x2 = get_lot(city_b)
    y2 = get_lat(city_b)
    return sqrt((x1-x2)**2+(y1-y2)**2)

def make_city(name,lat,lon):
    return [name,lat,lon]
def get_name(city):
    return city[0]
def get_lat(city):
    return city[1]
def get_lot(city):
    return city[2]
