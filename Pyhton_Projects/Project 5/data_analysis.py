import math
import stdio


# Entry point.
def main():
    # set ETA, rho, t, and r to appropriate values.
    eta = 9.135e-4
    rho = .5e-6
    t = 297
    r = 8.31457

    # Calculates var as the sum of the squares of the displacements (in meters) squared.
    var = 0
    n = 0
    while not stdio.isEmpty():
        n += 1
        var += (float(stdio.readFloat()) * 0.175e-6) ** 2

    # Sets var to var / 2 * n
    var = var / (2 * n)

    # Calculates Boltzmann's constant and Avogadro's constant.
    k = 6 * math.pi * var * eta * rho / t
    avogadro = r / k

    # Write the two constants to standard output separated by spaces in scientific notation.
    stdio.writef('%e %e\n', k, avogadro)


if __name__ == '__main__':
    main()
