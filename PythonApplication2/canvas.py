from turtle import title
from geometry import Point2d, Line, Rectangle, Circle
import time
import sdl2.ext
import sdl2
import copy


class Canvas:
    __window: sdl2.ext.Window
    __renderer:  sdl2.ext.renderer.Renderer

    def __init__(self, width: int, height: int):
        self.__window = sdl2.ext.Window("Hello World!", size=(width, height),
                                        flags=(sdl2.SDL_WINDOW_SHOWN |
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

    def points_draw(self,
                    points: list[tuple[float, float]],
                    color: sdl2.ext.color.Color):
        self.__renderer.draw_point(points, color)

    def rect_draw(self, rect: Rectangle, color: sdl2.ext.color.Color):
        width = rect.bottom_right.x - rect.top_left.x
        height = rect.bottom_right.y - rect.top_left.y

        self.__renderer.fill(
            [(rect.top_left.x, rect.top_left.y, width, height)], color)

    #def rect_draw2(self, rect: Rectangle, color: sdl2.ext.color.Color):
    #    width = rect.bottom_right.x - rect.top_left.x
    #    height = rect.bottom_right.y - rect.top_left.y

    #    if (rect.top_left.x <= rect.bottom_right.x):
    #        top_left = rect.top_left
    #        bottom_right = rect.bottom_right
    #    else:
    #        top_left = rect.bottom_right
    #        bottom_right = rect.top_left

    #    p = copy.copy(top_left)
    #    while p.y <= bottom_right.y:
    #        while p.x <= bottom_right.x:
    #            self.point2d_draw(p, color)
    #            p.x += 1

    #        p.y += 1
    #        p.x = top_left.x

    def circle_color(self, circle: Circle, color: sdl2.ext.color.Color):
        height = circle.radius * 2
        width = circle.radius * 2

        dx = circle.radius - width
        dy = circle.radius - height

        points = list()
        for dy in range(-int(circle.radius), int(circle.radius + 1)):
            for dx in range(-int(circle.radius), int(circle.radius + 1)):
                if(dx * dx + dy * dy < circle.radius * circle.radius):
                    points.append((circle.centre.x + dx, circle.centre.y + dy))
        self.points_draw(points, color)

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

    def title(self, title): 
        self.__window.title = title