from components.Point import Point
from components.Vector import Vector

class Trapeze:
    def __init__(self, a: list, b: list, c: list, d: list):
        self.a_coord = Point(*a)
        self.b_coord = Point(*b)
        self.c_coord = Point(*c)
        self.d_coord = Point(*d)

    # Площадь
    @property
    def square(self):
        return ((self.ab_side + self.bc_side) / 2) * \
               ((self.cd_side**2 - (((self.bc_side - self.ab_side)**2 + self.cd_side**2 - self.da_side**2) / (2 * (self.bc_side - self.ab_side)))**2)**0.5)

    # Высота трапеции
    @property
    def height(self):
        return (self.cd_side**2 - (((self.ab_side - self.bc_side)**2 + self.cd_side**2 - self.da_side**2) / (2 * (self.ab_side - self.bc_side)))**2)**0.5

    # Равнобочность трапеции
    @property
    def equal_side(self):
        if self.square == self.height**2:
            return True

        return False

    # Периметр
    @property
    def perimeter(self):
        return self.ab_side + self.bc_side + self.cd_side + self.da_side

    # a -> b
    @property
    def ab_side(self):
        return Vector.len(self.a_coord.x, self.a_coord.y, self.b_coord.x, self.b_coord.y)

    # b -> c
    @property
    def bc_side(self):
        return Vector.len(self.b_coord.x, self.b_coord.y, self.c_coord.x, self.c_coord.y)

    # c -> d
    @property
    def cd_side(self):
        return Vector.len(self.c_coord.x, self.c_coord.y, self.d_coord.x, self.d_coord.y)

    # d -> a
    @property
    def da_side(self):
        return Vector.len(self.d_coord.x, self.d_coord.y, self.a_coord.x, self.a_coord.y)
