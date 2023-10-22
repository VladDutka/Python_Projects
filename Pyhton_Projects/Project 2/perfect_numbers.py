import stdio
import sys

# Accepts n (integer) as an input
n = int(sys.argv[1])

# Repeating from  2 to n, tests if the factors of the number add up to the
# number.
for i in range(2, n + 1):
    total = 0
    j = 1
    while j <= i / 2:
        if i % j == 0:
            total += j
        j += 1
    if total == i:
        # If a number meets the requirements to be a perfect number
        # outputs i to standard output.
        stdio.writeln(i)
