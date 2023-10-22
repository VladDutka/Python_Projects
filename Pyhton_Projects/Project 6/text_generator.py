from markov_model import MarkovModel
import stdio
import sys


def main():
    # Accepts input k and n
    k = int(sys.argv[1])
    n = int(sys.argv[2])

    # Initialize text to text read from standard input using sys.stdin.read()
    text = sys.stdin.read()
    kgram = text[0:k]

    # Use the model to generate a random text of length n
    # and starting with the first k characters of text
    model = MarkovModel(text, k)

    # Write the random text to standard output.
    stdio.writeln(model.gen(kgram, n))


if __name__ == '__main__':
    main()
