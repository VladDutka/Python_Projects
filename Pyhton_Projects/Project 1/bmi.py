import stdio
import sys

# Accepts weight (float) and height (float) as command-line arguments.
weight = float(sys.argv[1])
height = float(sys.argv[2])

# Sets bmi to weight divided by square of height.
bmi = weight / (height ** 2)

# Writes bmi to standard output.
stdio.writeln(bmi)
