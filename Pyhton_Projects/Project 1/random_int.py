import stdio
import stdrandom
import sys

# Accepts a (int) and b (int) as command-line arguments.
a = int(sys.argv[1])
b = int(sys.argv[2])

# Sets r to a random integer between a and b, obtained by calling stdrandom.uniformInt().
r = stdrandom.uniformInt(a, b)

# Writes r to standard output.
stdio.writeln(r)
