import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepts private-key n (int) and d (int) as command-line arguments
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    # Gets the number of bits per character
    width = rsa.bitLength(n)
    # Accept message from standard input
    message = stdio.readAll()
    # Assuming l is the length of message, for i ∈ [0, l − 1)
    for i in range(0, len(message), width):
        # Sets s to substring of message from i to i + width
        s = message[i: i + width]
        # Sets y to decimal representation of the binary string s
        y = rsa.bin2dec(s)
        # Decrypts y
        decrypted = rsa.decrypt(y, n, d)
        # Writes the character corresponding to the decrypted value
        stdio.write(chr(decrypted))
    stdio.writeln()


if __name__ == '__main__':
    main()
