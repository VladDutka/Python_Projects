import stdio
import sys

# Inputs as intergers
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Finds the Min
a = min(x, y, z)

# Finds the Max
w = max(x, y, z)

# Finds the Middles number by adding the inputs and subracting the sum of Min and Max
m = (x + y + z) - (a + w)

# Output
stdio.writeln(str(a) + " " + str(m) + " " + str(w))
