import stdarray
import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Setup a 2D ragged list a of integers. The list must have n + 1 rows, with the ith (0 <= i
# <= n) row a[i] having i + 1 elements, each initialized to 1. For example, if n = 3, a should be
# initialized to [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]].
a = stdarray.create1D(n + 1, [1])
for i in range(n + 1):
    a[i] = stdarray.create1D(i + 1, 1)
# Fill the ragged list a using the formula for Pascal's triangle
#     a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
# where 0 <= i <= n and 1 <= j < i.
for i in range(1, n + 1):
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

# Write a to standard output.
for i in range(0, n + 1):
    for j in range(0, i + 1):
        if i != j:
            # If j is not the last column, write a[i][j] with a space after.
            stdio.write(f'{a[i][j]} ')
        else:
            # Otherwise, write the element with a newline after.
            stdio.writeln(a[i][j])
stdio.writeln()
