import stdarray
import stdio
import sys

# Accept m (int) and n (int) as command-line arguments.
m = int(sys.argv[1])
n = int(sys.argv[2])

# Accept m x n floats from standard input and store them in a 2D list a.
a = stdarray.create2D(m, n, 0.0)
for i in range(m):
    for j in range(n):
        a[i][j] = stdio.readFloat()

# Set c (the transpose of a) to a 2D list with n rows and m columns, with all the elements
# initialized to 0.0
c = stdarray.create2D(n,  m, 0.0)

# Fill in the elements of c such that c[i][j] = a[j][i], where 0 <= i < n and 0 <= j < m.
for i in range(n):
    for j in range(m):
        c[i][j] = a[j][i]

# Write c to standard output.
for i in range(n):
    for j in range(m):
        if j != m - 1:
            # If j is not the last column, write c[i][j] with a space after.
            stdio.write(f'{str(c[i][j])}' + ' ')
        else:
            # Otherwise, write the element with a newline after.
            stdio.writeln(f'{str(c[i][j])}')
