import math
import stdio
import sys

# Accepts inputs of λ  and t as floats
λ = float(sys.argv[1])
t = float(sys.argv[2])

# Computes p
p = math.exp(- λ * t)

# Outputs p
stdio.writeln(p)
