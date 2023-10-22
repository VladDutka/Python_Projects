import stdio
import sys

# Accepts n (integer) as an input
n = int(sys.argv[1])

# Repeats for each a in range of 1 to n ** int(n ** (1 / 3 + 1))
for a in range(1, int(n ** (1 / 3) + 1)):
    # Repeats for each b in range of 1 to n ** int(n ** (1 / 3 + 1))
    for b in range(a + 1, int((n - a ** 3) ** (1/3) + 1)):
        # Repeats for each c in range of 1 to n ** int(n ** (1 / 3 + 1))
        for c in range(a + 1, int((n ** (1/3) + 1))):
            # Repeats for each d in range of 1 to n ** int(n ** (1 / 3 + 1))
            for d in range(c + 1, int((n - c ** 3) ** (1/3) + 1)):
                # if a * a * a + b * b * b == c * c * c + d * d * d then
                if a * a * a + b * b * b == c * c * c + d * d * d:
                    # total equals a * a * a + b * b * b
                    total = a * a * a + b * b * b
                    # outputs total as a str, a (str), c (str), and d (str) in standard ouput
                    stdio.writeln(str(total) + ' = ' + str(a) + '^3 + ' + str(b) + '^3 = '
                                  + str(c) + '^3 + ' + str(d) + '^3')
