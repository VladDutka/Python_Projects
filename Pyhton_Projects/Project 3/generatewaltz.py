import stdarray
import stdrandom
import stdio


# Imports the libraries

# Def. main function
def main():
    # Calls the minuet and the trio functions
    minuet(11, 16, 0)
    trio(6, 16, 0)
    stdio.writeln()


# Def. of the minuetmeasure of the game

def minuet(num1, num2, num3):
    # Creates a 2d array for the minuet measure
    minuetmeasures = stdarray.create2D(num1, num2, num3)
    # Reads every int of the file and puts in the 2d array
    for i in range(num1):
        for j in range(num2):
            minuetmeasures[i][j] = stdio.readInt()
    # randomizes the minutemeasure column
    for j in range(num2):
        i = stdrandom.uniformInt(0, 6) + stdrandom.uniformInt(0, 6)
        stdio.write(f'{minuetmeasures[i][j]}' + ' ')


# Def. trio measure

def trio(num4, num5, num6):
    # Creates a 2d array for triomeasures
    triomeasures = stdarray.create2D(num4, num5, num6)
    # Reads every int of the file and puts in the 2d array
    for i in range(num4):
        for j in range(num5):
            triomeasures[i][j] = stdio.readInt()
    #  randomizes the triomeasure column
    for j in range(num5):
        i = stdrandom.uniformInt(0, 6)
        stdio.write(f'{triomeasures[i][j]}' + ' ')


# Calls the main function
if __name__ == '__main__':
    main()
