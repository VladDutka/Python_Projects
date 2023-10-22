import math
import stdio
import sys

# Imports r and h as floats and command line arguments
r = float(sys.argv[1])
h = float(sys.argv[2])

# Computes the Surface Area as S
S = 2 * math.pi * r * (r + h)

# Computes the Volume as V
V = math.pi * r ** 2 * h

# Outputs S on its own line in standard output
stdio.writeln('S = ' + str(S))

# Outputs V on its own line in standard output
stdio.writeln('V = ' + str(V))
