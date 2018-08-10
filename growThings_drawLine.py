from displays import OledScreen
oled = OledScreen(6)

#def drawLine(x0, y0, x1, y1):

def drawLine(point1, point2):

    x0 = point1[0]
    y0 = point1[1]
    x1 = point2[0]
    y1 = point2[1]
    #swap
    if x1 < x0:
        drawLine(x1, y1, x0, y0)

    x = x0
    y = y0
    a = y1 - y0
    b = x0 - x1

    if (b == 0):
        if (y < y1):
            while(y <= y1):
                oled.pixel(x, y, 1)
                y = y + 1
        if (y > y1):
            while(y1 <= y):
                oled.pixel(x, y, 1)
                y = y - 1
        return

    #slope
    m = float(a)/float(-1 * b)


    #OCTANT 1
    if m >= 0 and m <= 1:
        d = 2 * a + b
        while x <= x1:
            oled.pixel(x, y, 1)
            if d > 0:
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    #OCTANT 2
    elif m > 1:
        d = a + 2 * b
        while y <= y1:
            oled.pixel(x, y, 1)
            if d < 0:
                x += 1
                d += 2 * a
            y += 1
            d += 2 * b
    #OCTANT 7
    elif m < -1:
        d = a - 2 * b
        while y >= y1:
            oled.pixel(x, y, 1)
            if d > 0:
                x += 1
                d += 2 * a
            y -= 1
            d -= 2 * b
    #OCTANT 8
    elif m >= -1:
        d = 2 * a - b
        while x <= x1:
            oled.pixel(x, y, 1)
            if d < 0:
                y -= 1
                d -= 2 * b
            x += 1
            d += 2 * a
    oled.show()

drawLine([3, 100], [100, 10])
