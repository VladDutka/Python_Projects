import markov_model
from symboltable import SymbolTable
import stdio
import stdrandom
import sys


class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):
        self._k = k
        self._st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            kgram = circ_text[i:i + k]
            next_char = circ_text[i + k: i + k + 1]
            if (kgram in self._st) is True:
                if (next_char in self._st[kgram]) is True:
                    self._st[kgram][next_char] = 1 + self._st[kgram][next_char]
                else:
                    self._st[kgram][next_char] = 1
            else:
                self._st[kgram] = {next_char: 1}

    # Returns the order this Markov model.
    def order(self):

        return self._k

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is
    # nonexistent. Raises an error if kgram is not of length k.
    def kgram_freq(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        a = (self._st).setdefault(kgram, 0)
        if a == 0:
            return 0
        else:
            b = sum((self._st[kgram]).values())
            return b

    # Returns number of times character c follows kgram in this Markov model; and 0 if kgram is
    # nonexistent or if it is not followed by c. Raises an error if kgram is not of length k.

    def char_freq(self, kgram, c):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        a = (self._st).setdefault(kgram, 0)
        if a == 0:
            return 0
        else:
            if c in self._st[kgram].keys():
                b = self._st[kgram][c]
                return b
            else:
                return 0

    # Returns a random character following kgram in this Markov model. Raises an error if kgram is
    # not of length k or if kgram is nonexistent.
    def rand(self, kgram):

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)
        chances = []
        items = list(self._st[kgram].keys())
        for char in items:
            chances += [self.char_freq(kgram, char) / self.kgram_freq(kgram)]
        rand = stdrandom.discrete(chances)
        return items[rand]

    # Generates and returns a string of length n from this Markov model, the first k characters of
    # which is kgram.

    def gen(self, kgram, n):
        a = kgram
        for i in range(0, n):
            a = a + self.rand(kgram)
            kgram = a[i + 1:i + 1 + self._k]
            if len(a) == n:
                return a

    # Replaces unknown characters (~) in corrupted with most probable characters from this Markov
    # model, and returns that string.
    def replace_unknown(self, corrupted):
        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                key = self._st[corrupted[i - self._k:i]].keys()
                p = []
                for y in key:
                    p += [[y, (corrupted[i - self._k:i] + y + corrupted[i + 1:i + self._k + 1]), 1]]

                # Finds the likely hood

                for u in range(len(p)):
                    for a in range(self._k + 1):
                        t = self.char_freq(p[u][1][a:a + self._k], p[u][1][a + self._k])
                        if self.kgram_freq(p[u][1][a:a + self._k]) == 0:
                            p[u][2] = 0
                            break
                        p[u][2] *= t / self.kgram_freq(p[u][1][a:a + self._k])

                # Finds the most likely letter
                c = 0
                for h in range(len(p)):
                    if (p[h][2] > c):
                        c = p[h][2]

                # Adds the most likely letter
                for q in range(len(p)):
                    if c == p[q][2]:
                        original += p[q][0]
                        break

            else:
                original += corrupted[i]
        return original


# Given a list a, _argmax returns the index of the maximum value in a.
def _argmax(a):
    return a.index(max(a))


# Unit tests the data type [DO NOT EDIT].
def _main():
    text = sys.argv[1]
    k = int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace('-', ' '), char.replace('-', ' ')))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char, model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
