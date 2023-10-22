import math
import stdio
import sys

# Inputs X1, X2, Y1, Y2 as floats
X1 = math.radians(float(sys.argv[1]))
Y1 = math.radians(float(sys.argv[2]))
X2 = math.radians(float(sys.argv[3]))
Y2 = math.radians(float(sys.argv[4]))

# Computers the distance as d
d = 6359.83 * math.acos(math.sin(X1) * math.sin(X2)
                        + math.cos(X1) * math.cos(X2) * math.cos(Y1 - Y2))

# outputs d
stdio.writeln(d)
