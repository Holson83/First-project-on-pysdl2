class Point2d:
    x: float
    y: float

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Line:
    start: Point2d
    end: Point2d

    def __init__(self, start: Point2d, end: Point2d):
        super().__init__()
        self.start = start
        self.end = end

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)


class Rectangle:
    top_left: Point2d
    bottom_right: Point2d

    def __init__(self, top_left: Point2d, bottom_right: Point2d):
        super().__init__()
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __str__(self):
        return '{}, {}'.format(self.top_left, self.bottom_right)


class Circle:
    centre: Point2d
    radius: float

    def __init__(self, centre: Point2d, radius: float):
        super().__init__()
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return '{}, {}'.format(self.centre, self.radius)