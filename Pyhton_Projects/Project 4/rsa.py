import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    lst_prime = _primes(lo, hi)
    lst_sample = _sample(lst_prime, 2)
    p = lst_sample[0]
    q = lst_sample[1]
    n = p * q
    m = (p - 1) * (q - 1)
    lst_prime = _primes(2, m)
    lst_prime2 = []
    for e in range(len(lst_prime)):
        if m % lst_prime[e] != 0:
            lst_prime2.append(lst_prime[e])
    e = _choice(lst_prime2)
    d = 1
    while e * d % m != 1:
        d += 1

    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return x ** e % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return y ** d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % width)


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    lst = []
    for i in range(lo, hi):
        possible_divisor = 2
        while possible_divisor < i / possible_divisor:
            if i % possible_divisor == 0:
                break
            possible_divisor += 1
        if i % possible_divisor != 0:
            lst.append(i)
    return lst


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    lstb = a.copy()
    for n in range(k):
        value = stdrandom.uniformInt(0, len(lstb))
        temp = lstb[n]
        lstb[n] = lstb[value]
        lstb[value] = temp
    lsta = []
    for i in range(0, k):
        lsta.append(lstb[i])

    return lsta


# Returns a random item from the list a.
def _choice(a):
    y = len(a)
    r = stdrandom.uniformInt(0, y)
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
