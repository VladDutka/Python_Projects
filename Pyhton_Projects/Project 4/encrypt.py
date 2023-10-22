import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepts public-key n (int) and e (int) as command-line arguments.
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    # Get the number of bits per character
    width = rsa.bitLength(n)
    # Accept message to encrypt from standard input.
    message = stdio.readAll()
    # For each character c in message
    for c in message:
        # Uses the built-in function ord() to turn c into an integer x
        x = ord(c)
        # Encrypts x
        encrypted = rsa.encrypt(x, n, e)
        # Writes the encrypted value as a width-long binary string
        binary = rsa.dec2bin(encrypted, width)
        stdio.write(binary)
    # Writes a newline character
    stdio.writeln()


if __name__ == '__main__':
    main()
