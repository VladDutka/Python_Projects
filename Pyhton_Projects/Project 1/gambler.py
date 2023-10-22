import stdio
import sys

# inputs n1 & n2 ase intergers and p as float
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# Finds the propablity for both players
q = 1 - p

# Computes player 1 (p1) probablity
p1 = (1 - (p / q) ** n2) / (1 - (p / q) ** (n1 + n2))

# Computes player (p2) probablity
p2 = ((1 - (q / p) ** n1) / (1 - (q / p) ** (n1 + n2)))

# Writes outpu in terminal of p1 and p2
stdio.writeln(str(p1) + ' ' + str(p2))
