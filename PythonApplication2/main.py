from PhysObject import Vector2d, Phys_Rectangle, Phys_Circle
from physics import Velocity, Universe
from geometry import Point2d
from canvas import Canvas
import time
import sdl2.ext
import sdl2
import copy


def main():
    try:
        #window_height = 480
        #window_width = 640
        left_boundary = 480
        right_boundary = 480
        top_boundary = 640
        bottom_boundary = 640

        sdl2.ext.init()
        canvas = Canvas(640, 480)
        rect_1 = Phys_Rectangle(Point2d(200, 0), Point2d(300, 80))
        circle = Phys_Circle(Point2d(300, 100), radius = 50)
        #rect_1 == rect
        #rect_2 == rect

        rect_1.velocity.vx = 200
        rect_1.velocity.vy = 100
        circle.velocity.vx = 100
        circle.velocity.vy = 200

        canvas.update()

        running = True
        frames = 0
        dT = 0
        T0 = time.monotonic()
        dt = 0
        while running:
            t0 = time.monotonic()
            events  = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running  = False
                    break
        
            rect_1.move(dt)
            if (rect_1.bottom_right.y >= left_boundary and
                right_boundary and
                rect_1.velocity.vy > 0):
                rect_1.velocity.vy *= -1
            if (rect_1.bottom_right.x >= top_boundary and
                bottom_boundary and
                rect_1.velocity.vx > 0):
                rect_1.velocity.vx *= -1
            if (rect_1.top_left.y <= 0 and rect_1.velocity.vy < 0):
                rect_1.velocity.vy *= -1
            if (rect_1.top_left.x <= 0 and rect_1.velocity.vx < 0):
                rect_1.velocity.vx *= -1
            
            circle.move(dt)
            if (circle.centre.x + circle.radius > right_boundary and
                circle.velocity.vx > 0):
                circle.velocity.vx *= -1
            if (circle.centre.x - circle.radius < left_boundary and
                circle.velocity.vx < 0):
                circle.velocity.vx *= -1
            if (circle.centre.y + circle.radius > bottom_boundary and
                circle.velocity.vy > 0):
                circle.velocity.vy *= -1
            if (circle.centre.y - circle.radius < top_boundary and
                circle.velocity.vy < 0):
                circle.velocity.vy *= -1

            canvas.fill(sdl2.ext.color.Color(r=0, g=0, b=0, a=255))

            #canvas.pixel_color(Point2d(20, 50),
            #                   sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            #canvas.rect_draw(rect_1,
            #                 sdl2.ext.color.Color(r=255, g=165, b=0, a=255))
            canvas.circle_color(circle,
                                sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            #canvas.line_draw(Line(Point2d(80, 90), Point2d(300, 100)),
            #                 sdl2.ext.color.Color(r=255, g=0, b=0, a=255))

            canvas.update()
            frames += 1
            t1 = time.monotonic()
            dt = t1 - t0
            dT = t1 - T0
            if dT > 1:
                canvas.title(f'FPS:{frames/dT}')
                frames = 0
                T0 = t1
    finally:
        sdl2.ext.quit()


if __name__ == '__main__':
    main()
