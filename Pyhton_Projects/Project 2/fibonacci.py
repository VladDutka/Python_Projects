import stdio
import sys

# Accepts n (int) as an input
n = int(sys.argv[1])

# Sets a and b (first two Fibonacci numbers) to 1, and i to 3.
a = 1
b = 1
i = 3

# Repeats the loop as long as i is less than or equal to n.
while i <= n:
    temp = a
    a = b
    b += temp
    i += 1

# Writes b to standard output.
stdio.writeln(b)
