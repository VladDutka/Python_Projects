import math
import stdio
import sys

# Accepts a (float), b (float), and c (float) as command-line arguments.
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:

    # If a is 0, write the message 'Value of a must not be 0' to standard output.

    stdio.writeln('Value of a must not be 0')
else:
    # Computes discriminant (b^2 - 4ac).
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        # If discriminant is negative, write the message 'Value of discriminant must not be
        # negative' to standard output.
        stdio.writeln('Value of discriminant must not be negative')

    else:
        # Computes the two roots of the quadratic equation ax^2 + bx + c = 0.
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        # Writes the two roots to standard output , separated by a space .
        stdio.writeln(str(root1) + ' ' + str(root2))
