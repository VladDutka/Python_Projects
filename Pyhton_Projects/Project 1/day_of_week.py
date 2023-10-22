import stdio
import sys

# Month
m = int(sys.argv[1])
# Day
d = int(sys.argv[2])
# Year
y = int(sys.argv[3])

# Computes Day of the week
Y0 = y - (14 - m) // 12
X0 = Y0 + Y0 // 4 - Y0 // 100 + Y0 // 400
M0 = m + 12 * ((14 - m) // 12) - 2
DOW = (d + X0 + 31 * M0 // 12) % 7

# Prints Day of the week in terminal
stdio.writeln(DOW)
