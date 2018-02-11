from display import *


def draw_line( x0, y0, x1, y1, screen, color ):

    #swap
    if x1 < x0: 
        draw_line(x1, y1, x0, y0, screen, color)


    x = x0
    y = y0 
    a = y1 - y0
    b = x0 - x1

    #slope 
    if (x1 - x0) != 0:
        m = float(a)/float(-1 * b)
    else: 
        m = 0

    #OCTANT 1
    if m >= 0 and m <= 1: 
        d = 2 * a + b
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    #OCTANT 2
    elif m > 1: 
        d = a + 2 * b
        while y <= y1:
            plot(screen,color, x, y)
            if d < 0:
                x += 1
                d += 2 * a
            y += 1
            d += 2 * b
    #OCTANT 7
    elif m < -1: 
        d = a - 2 * b
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0: 
                x += 1
                d += 2 * a
            y -= 1
            d -= 2 * b
    #OCTANT 8
    elif m >= -1:
        d = 2 * a - b
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0: 
                y -= 1
                d -= 2 * b
            x += 1
            d += 2 * a
