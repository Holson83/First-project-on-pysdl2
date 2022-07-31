from geometry import Point2d, Line, Rectangle, Circle
from physics import Velocity


class Vector2d(Point2d):
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


#class Line:
#    start: Point2d
#    end: Point2d

#    def __init__(self, start: Point2d, end: Point2d):
#        self.start = start
#        self.end = end

#    def __str__(self):
#        return '({}, {})'.format(self.start, self.end)


class Phys_Rectangle(Rectangle):
    top_left: Point2d
    bottom_right: Point2d
    velocity: Velocity

    def __init__(self, top_left: Point2d, bottom_right: Point2d):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.velocity = Velocity()

    def __str__(self):
        return '{}, {}'.format(self.top_left, self.bottom_right)

    def move(self, dt: float):
        self.top_left.x += self.velocity.vx * dt
        self.top_left.y += self.velocity.vy * dt
        self.bottom_right.x += self.velocity.vx * dt
        self.bottom_right.y += self.velocity.vy * dt


class Phys_Circle(Circle):
    centre: Point2d
    radius: float

    def __init__(self, centre: Point2d, radius: float):
        self.centre = centre
        self.radius = radius
        self.velocity = Velocity()

    def __str__(self):
        return '{}, {}'.format(self.centre, self.radius)

    def move(self, dt: float):
        self.centre.x += self.velocity.vx * dt
        self.centre.y += self.velocity.vy * dt