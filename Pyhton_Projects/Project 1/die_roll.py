import stdio
import stdrandom
import sys

# Input
n = int(sys.argv[1])

# The first roll
roll1 = stdrandom.uniformInt(1, n + 1)

# Second Roll
roll2 = stdrandom.uniformInt(1, n + 1)

# Adds the both roll number together
sum = roll1 + roll2

# output
stdio.writeln(sum)
