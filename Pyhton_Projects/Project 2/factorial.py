import stdio
import sys

# Accepts n as an integer as an input

n = int(sys.argv[1])

# Sets result to 1.
result = 1

for i in range(1, n + 1):
    # For each value of i from [2, n],
    # set result to its current value times i.
    result = result * i

# Writes result to standard output.
stdio.writeln(result)
