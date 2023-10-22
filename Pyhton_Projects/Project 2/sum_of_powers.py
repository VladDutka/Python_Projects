import stdio
import sys

# Accepts n and k as integers as inputs
n = int(sys.argv[1])
k = int(sys.argv[2])

# Sets the current total to 0
total = 0

# Repeats i in range of 1 to n + 1
for i in range(1, n + 1):
    # adds i ** k to total
    total += i ** k
# Outputs total (Sum of powers) in standard output
stdio.writeln(total)
