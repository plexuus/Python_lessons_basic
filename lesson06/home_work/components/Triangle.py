from components.Point import Point
from components.Vector import Vector


class Triangle:
    def __init__(self, a: list, b: list, c: list):
        self.a_coord = Point(*a)
        self.b_coord = Point(*b)
        self.c_coord = Point(*c)

    # Площадь
    @property
    def square(self):
        return ((self.b_coord.x - self.a_coord.x) * (self.c_coord.y - self.a_coord.y) - (
                    self.c_coord.x - self.a_coord.x) * (self.b_coord.y - self.a_coord.y)) / 2

    # Периметр
    @property
    def perimeter(self):
        return self.ab_side + self.bc_side + self.ca_side

    # Высота треугольника
    @property
    def height(self):
        return 2 * self.square / self.ab_side

    # a -> b
    @property
    def ab_side(self):
        return Vector.len(self.a_coord.x, self.a_coord.y, self.b_coord.x, self.b_coord.y)

    # b -> c
    @property
    def bc_side(self):
        return Vector.len(self.b_coord.x, self.b_coord.y, self.c_coord.x, self.c_coord.y)

    # c -> a
    @property
    def ca_side(self):
        return Vector.len(self.c_coord.x, self.c_coord.y, self.a_coord.x, self.a_coord.y)
