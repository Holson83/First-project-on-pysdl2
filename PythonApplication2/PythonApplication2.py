from struct import Struct
import time
import sdl2.ext
import sdl2
import copy


class Point2d(object):
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Line(object):
    start: Point2d
    end: Point2d

    def __init__(self, start: Point2d, end: Point2d):
        self.start = start
        self.end = end

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)


class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0


class Rectangle(object):
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


class Circle(object):
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


class Canvas:
    __window: sdl2.ext.Window
    __renderer:  sdl2.ext.renderer.Renderer

    def __init__(self, width: int, height: int):
        self.__window = sdl2.ext.Window("Hello World!", size=(width, height), flags=(sdl2.SDL_WINDOW_SHOWN |
                                                                                    sdl2.SDL_WINDOW_RESIZABLE))
        self.__renderer = sdl2.ext.renderer.Renderer(self.__window)

    def update(self):
        self.__renderer.present()

    def set_color(self, color: sdl2.ext.color.Color):
        self.__renderer.color = color

    def fill(self, color: sdl2.ext.color.Color):
        self.__renderer.clear(color)

    def point2d_draw(self, point: Point2d, color: sdl2.ext.color.Color):
        self.__renderer.draw_point([(point.x, point.y)], color)

    def rect_draw(self, rect: Rectangle, color: sdl2.ext.color.Color):
        width = rect.bottom_right.x - rect.top_left.x
        height = rect.bottom_right.y - rect.top_left.y

        self.__renderer.fill([(rect.top_left.x, rect.top_left.y, width, height)], color)

        #if (rect.top_left.x <= rect.bottom_right.x):
        #    top_left = rect.top_left
        #    bottom_right = rect.bottom_right
        #else:
        #    top_left = rect.bottom_right
        #    bottom_right = rect.top_left

        #p = copy.copy(top_left)
        #while p.y <= bottom_right.y:
        #    while p.x <= bottom_right.x:
        #        self.point2d_draw(p, color)
        #        p.x += 1

        #    p.y += 1
        #    p.x = top_left.x

    def circle_color(self, circle: Circle, color: sdl2.ext.color.Color):
        height = circle.radius * 2
        width = circle.radius * 2

        dx = circle.radius - width
        dy = circle.radius - height

        for dy in range(-circle.radius, circle.radius + 1):
            for dx in range(-circle.radius, circle.radius + 1):
                if(dx * dx + dy * dy < circle.radius * circle.radius):
                    p = Point2d(circle.centre.x + dx, circle.centre.y + dy)
                    self.point2d_draw(p, color)


    def line_draw(self, line: Line, color: sdl2.ext.color.Color):
        if (line.start.x <= line.end.x):
            start = line.start
            end = line.end
        else:
            start = line.end
            end = line.start

        p = start
        while p.x < end.x:
            self.point2d_draw(p, color)
            p1 = Point2d(p.x, p.y + 1)
            p2 = Point2d(p.x + 1, p.y)
            p3 = Point2d(p.x, p.y - 1)
            t1 = abs((end.y - start.y) * p1.x - (end.x - start.x) * p1.y +
            end.x * start.y - end.y * start.x)
            t2 = abs((end.y - start.y) * p2.x - (end.x - start.x) * p2.y +
            end.x * start.y - end.y * start.x)
            t3 = abs((end.y - start.y) * p3.x - (end.x - start.x) * p3.y +
            end.x * start.y - end.y * start.x)

            if t1 < t2:
                if t1 < t3:
                    p = p1
                else:
                    p = p3
            else:
                if t2 <= t3:
                    p = p2
                else:
                    p = p3

        y = min(p.y, end.y)
        end.y = max(p.y, end.y)
        p.y = y
        while p.y <= end.y:
            self.point2d_draw(p, color)
            p.y += 1


def main():
    try:
        window_width = 640
        window_height = 480
        sdl2.ext.init()
        canvas = Canvas(640, 480)

        rect = Rectangle(Point2d(100, 80), Point2d(200, 160))
        circle = Circle(Point2d(100, 100), radius = 50)

        rect.velocity.vx = 200
        rect.velocity.vy = 100

        canvas.update()

        running = True
        dt = 0
        while running:
            t0 = time.monotonic()
            events  = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running  = False
                    break

            rect.move(dt)
            if (rect.bottom_right.y >= window_height and
                rect.velocity.vy > 0):
                rect.velocity.vy *= -1
            if (rect.bottom_right.x >= window_width and
                rect.velocity.vx > 0):
                rect.velocity.vx *= -1
            if (rect.top_left.y <= 0 and rect.velocity.vy < 0):
                rect.velocity.vy *= -1
            if (rect.top_left.x <= 0 and rect.velocity.vx < 0):
                rect.velocity.vx *= -1

            canvas.fill(sdl2.ext.color.Color(r=0, g=0, b=0, a=255))

            #canvas.pixel_color(Point2d(20, 50), sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            canvas.rect_draw(rect, sdl2.ext.color.Color(r=255, g=165, b=0, a=255))
            canvas.circle_color(circle, sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            #canvas.line_draw(Line(Point2d(80, 90), Point2d(300, 100)), sdl2.ext.color.Color(r=255, g=0, b=0, a=255))

            canvas.update()
            t1 = time.monotonic()
            dt = t1 - t0
    finally:
        sdl2.ext.quit()


if __name__ == '__main__':
    main()
