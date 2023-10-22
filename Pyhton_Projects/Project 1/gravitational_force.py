import stdio
import sys

# inputs variables m1, m2, and r as floats
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# G is gravitational Constant
G = 6.674 * 10 ** -11

# Computes the gravitional force in N between objects centers
f = G * (m1 * m2 / r ** 2)

# outputs the gravitional force as f
stdio.writeln(f)
