from markov_model import MarkovModel
import stdio
import sys


def main():

    # Accepts k(int), n(int) and text(str) as standard input
    k = int(sys.argv[1])
    s = sys.argv[2]
    text = sys.stdin.read()

    # assigns model to markov_model
    model = MarkovModel(text, k)

    # write our fixed text to standard output
    stdio.writeln(model.replace_unknown(s))


if __name__ == '__main__':
    main()
