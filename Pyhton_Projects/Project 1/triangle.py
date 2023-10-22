import stdio
import sys

# Accepts x (int), y (int), and z (int) as command-line arguments.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Sets expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two, and False otherwise.
expr = x <= y + z and y <= x + z and z <= y + x

# Writes expr to standard output.
stdio.writeln(expr)
