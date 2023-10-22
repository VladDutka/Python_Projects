import stdio
import sys


# A data type to represent a 1-dimensional interval [lbound, ubound].
class Interval:
    # Construct a new interval given its lower and upper bounds.
    def __init__(self, lbound, ubound):
        self._lbound = lbound
        self._ubound = ubound

    # Returns the lower bound of this interval.
    def lower(self):
        return self._lbound

    # Returns the upper bound of this interval.
    def upper(self):
        return self._ubound

    # Returns True if this interval contains the point x, and False otherwise.
    def contains(self, x):
        if self._lbound <= x and x <= self._ubound:
            return True
        return False

    # Returns True if this interval intersects other, and False otherwise.
    def intersects(self, other):
        if self._ubound <= other._ubound and self._ubound >= other._lbound or \
                self._lbound >= other._lbound and self._lbound <= other._ubound:
            return True
        return False

    # Returns a string representation of this interval.
    def __str__(self):
        return "[" + str(self._lbound) + ", " + str(self._ubound) + "]"


# Unit tests the data type (DO NOT EDIT).
def _main():
    x = float(sys.argv[1])
    intervals = []
    while not stdio.isEmpty():
        lbound = stdio.readFloat()
        rbound = stdio.readFloat()
        intervals += [Interval(lbound, rbound)]
    for i in range(len(intervals)):
        if intervals[i].contains(x):
            stdio.writef('%s contains %f\n', intervals[i], x)
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                stdio.writef('%s intersects %s\n', intervals[i], intervals[j])


if __name__ == '__main__':
    _main()
