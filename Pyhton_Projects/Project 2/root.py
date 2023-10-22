import stdio
import sys

# Accepts k as a int and c and epsilon as floats
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])
# Sets t = c
t = c
# as long as the bs(1 - c / t ** k) is greater than epsilon it
# Continues
while abs(1 - c / t ** k) > epsilon:
    # Uses the formula to determine what t is equal to
    t = t - (t ** k - c) / (k * t ** (k - 1))
# Outputs t in standard output as a float
stdio.writeln(t)
