import stdio
import stdrandom

# Sets the rank of the card to a random int
rank = stdrandom.uniformInt(2, 15)
# Sets rankStr to an empty string
rankStr = ''
# if the rank  corresponds with the if and elif statements number
# Then set rankStr to the corresponding rank
if rank == 2:
    rankStr = '2'
elif rank == 3:
    rankStr = '3'
elif rank == 4:
    rankStr = '4'
elif rank == 5:
    rankStr = '5'
elif rank == 6:
    rankStr = '6'
elif rank == 7:
    rankStr = '7'
elif rank == 8:
    rankStr = '8'
elif rank == 9:
    rankStr = '9'
elif rank == 10:
    rankStr = '10'
elif rank == 11:
    rankStr = "Jack"
elif rank == 12:
    rankStr = 'Queen'
elif rank == 13:
    rankStr = 'King'
else:
    rankStr = 'Ace'

# Sets the suit of the card to a random int
suit = stdrandom.uniformInt(1, 5)
# Sets suitStr to an empty string
suitStr = ''
# if the suit corresponds with the if and elif statements number
# Then set suitStr to the corresponding rank
if suit == 1:
    suitStr = 'Clubs'
elif suit == 2:
    suitStr = 'Diamonds'
elif suit == 3:
    suitStr = 'Hearts'
else:
    suitStr = 'Spades'

# Outputs the rankStr and suitStr as strings in standard output
stdio.writeln(f'{rankStr} of {suitStr}')
