class Velocity:
    def __init__(self):
        super().__init__()
        self.vx = 0
        self.vy = 0


class Universe:
    left_boundary: float
    right_boundary: float
    top_boundary: float
    bottom_boundary: float

    def __init__(self, left_boundary: float, right_boundary: float,
                 top_boundary: float, bottom_boundary:float):
        super().__init__()
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.top_boundary = top_boundary
        self.bottom_boundary = bottom_boundary