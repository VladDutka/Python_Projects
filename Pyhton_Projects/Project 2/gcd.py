import stdio
import sys

# Inputs p and q as integers
p = int(sys.argv[1])
q = int(sys.argv[2])

# While the remainder of p divided by q is not 0 continue
while p % q != 0:
    # Exchanges p and q with q and p mod q
    temp = p
    p = q
    q = temp % q

# Outputs q in standard output
stdio.writeln(q)
