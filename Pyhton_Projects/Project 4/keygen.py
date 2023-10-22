import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepts lo (int) and hi (int) as command-line arguments.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])
    # Gets public/private keys as a tuple
    key = rsa.keygen(lo, hi)
    # Writes the three values in the tuple, separated by a space.
    stdio.writeln(str(key[0]) + ' ' + str(key[1]) + ' ' + str(key[2]))


if __name__ == '__main__':
    main()
