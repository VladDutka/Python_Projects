import stdio
import sys

# Accepts t and v as inputs
t = float(sys.argv[1])
v = float(sys.argv[2])

# Checks if t (Temperature) is Less than 50
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")
# Checks if v (Wind speed) is less than 3 mph
elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")
# If the t is less than 50 and the if v is greater than 3
# Then it uses the wind chill formula to calculate the wind chill
else:
    w = 35.74 + (.6215 * t) + ((.4275 * t - 35.75) * v ** .16)
    # Writes in standard output
    stdio.writeln(w)
