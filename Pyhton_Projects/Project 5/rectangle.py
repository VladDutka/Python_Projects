import stdio
import sys
from interval import Interval


class Rectangle:
    def __init__(self, xint, yint):
        self._xint = xint
        self._ynt = yint

    def area(self):
        width = self._xint.upper() - self._xint.lower()
        height = self._ynt.upper() - self._ynt.lower()
        return width * height

    def perimeter(self):
        width = self._xint.upper() - self._xint.lower()
        height = self._ynt.upper() - self._ynt.lower()
        return 2 * (width + height)

    def contains(self, x, y):
        if self._xint.contains(x) and self._ynt.contains(y):
            return True
        return False

    def intersects(self, other):
        if self._xint.intersects(other._xint) and self._ynt.intersects(other._ynt):
            return True
        return False

    def __str__(self):
        return str(self._xint) + " x " + str(self._ynt)


# Unit tests the data type (DO NOT EDIT).
def _main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    rectangles = []
    while not stdio.isEmpty():
        lbound1 = stdio.readFloat()
        rbound1 = stdio.readFloat()
        lbound2 = stdio.readFloat()
        rbound2 = stdio.readFloat()
        rectangles += [Rectangle(Interval(lbound1, rbound1), Interval(lbound2, rbound2))]
    for i in range(len(rectangles)):
        stdio.writef('Area(%s) = %f\n', rectangles[i], rectangles[i].area())
        stdio.writef('Perimeter(%s) = %f\n', rectangles[i], rectangles[i].perimeter())
        if rectangles[i].contains(x, y):
            stdio.writef('%s contains (%f, %f)\n', rectangles[i], x, y)
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                stdio.writef('%s intersects %s\n', rectangles[i], rectangles[j])


if __name__ == '__main__':
    _main()
