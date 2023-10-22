import math
import stdio
import sys

# Accepts inputs of Theta1, n1, n2 as floats
Theta1 = math.radians(float(sys.argv[1]))
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# Computes Theta2
Theta2 = n1 * math.sin(Theta1) / n2

# Outputs Theta2
stdio.writeln(math.degrees(math.asin(Theta2)))
