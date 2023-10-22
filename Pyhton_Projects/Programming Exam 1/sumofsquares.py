import stdio
# Sets the sum_of_squares to 0
sum_of_squares = 0
# Until the standard input is not empty
while not stdio.isEmpty():
    # Reads each Int in the Input and puts as the variable x
    x = stdio.readInt()

    # Adds the square of x to the sum_of_squares
    sum_of_squares += x ** 2
# outputs the sum of squares in standard output
stdio.writeln(sum_of_squares)
