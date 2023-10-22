import stdio
import sys

# Accepts name (str) and age (str) as command-line arguments.
name = sys.argv[1]
age = sys.argv[2]

# Writes the message 'name is age years old.' to standard output.
stdio.writeln(name + " is " + age + " years old.")
