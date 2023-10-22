import stdio
import sys

# Accepts n as an input and  as an integer
n = int(sys.argv[1])

# It Sets dragon and nogard to the string 'F'.
dragon = 'F'
nogard = 'F'

# For the times that n is repeating it exchanges dragon and nogard
# with dragon “L” nogard and dragon “R” nogard
for i in range(1, n + 1):
    temp = dragon
    dragon = dragon + 'L' + nogard
    nogard = temp + 'R' + nogard

# Outputs dragon in standard output.
stdio.writeln(dragon)
