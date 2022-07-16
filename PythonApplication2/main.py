from geometry import Point2d, Line, Rectangle, Circle
from canvas import Canvas
import time
import sdl2.ext
import sdl2
import copy


def main():
    try:
        window_width = 640
        window_height = 480
        sdl2.ext.init()
        canvas = Canvas(640, 480)

        rect = Rectangle(Point2d(100, 80), Point2d(200, 160))
        #circle = Circle(Point2d(100, 100), radius = 50)

        rect.velocity.vx = 200
        rect.velocity.vy = 100

        canvas.update()

        running = True
        #dT = 0
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
            #canvas.circle_color(circle, sdl2.ext.color.Color(r=255, g=0, b=0, a=255))
            #canvas.line_draw(Line(Point2d(80, 90), Point2d(300, 100)), sdl2.ext.color.Color(r=255, g=0, b=0, a=255))

            canvas.update()
            t1 = time.monotonic()
            dt = t1 - t0
            #canvas.title(f'FPS:{frames/dT}')
            #frames = 0
    finally:
        sdl2.ext.quit()


if __name__ == '__main__':
    main()
