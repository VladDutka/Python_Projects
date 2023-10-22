import math
import stdio
import sys

# inputs Latitude (la) and longitude (lo) as floats
la = math.radians(float(sys.argv[1]))
lo = float(sys.argv[2])

# Computes x and y
y = math.log((1 + math.sin(la)) / (1 - math.sin(la))) / 2
x = lo

# Outputs x and y with space
stdio.writeln(str(x) + " " + str(y))
