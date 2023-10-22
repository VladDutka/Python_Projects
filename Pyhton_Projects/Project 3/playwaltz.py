import stdaudio
import stdio
import sys


# Imports Libraries

# Def. main function
def main():
    # Reads the all the integers of the file
    randommeasures = stdio.readAllInts()

    # If the random measures does not equal 32, exits with the message
    if len(randommeasures) != 32:
        sys.exit('A waltz must contain exactly 32 measures')

    #  If a minuet measure is not from 1 - 176, it exits with the message
    for measure in range(16):
        if randommeasures[measure] > 176 or randommeasures[measure] < 1:
            sys.exit('A minuet measure must be from [1, 176]')
    # If a minuet measure is not from 1 - 96 , exits with the message
    for measure in range(17, 32):
        if randommeasures[measure] > 96 or randommeasures[measure] < 1:
            sys.exit('A trio measure must be from [1, 96]')

    # Plays the first 16 measures
    for measure in range(16):
        stdaudio.playFile(f'data/M{randommeasures[measure]}')
    # Plays the last 16 measures
    for measure in range(17, 32):
        stdaudio.playFile(f'data/M{randommeasures[measure]}')


# Calls the main function.
if __name__ == '__main__':
    main()
