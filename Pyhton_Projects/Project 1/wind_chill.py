import stdio
import sys

# Accepts inputs t & v as floats
t = float(sys.argv[1])
v = float(sys.argv[2])

# computes w
w = 35.74 + 0.6215 * t + (.4275 * t - 35.75) * v ** .16

# Outputs w
stdio.writeln(w)
