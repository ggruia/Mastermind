# MASTERMIND game
# 21/01/2021 : Free-time project

from termcolor import colored
from colored import fg, attr
import random

print("\nThe MASTERMIND chose the FOUR COLOURS!\n")

colourCode = [1, 208, 220, 2, 27, 129, 99, 0]
master = [random.randint(1, 8) for x in range(4)]
maxTries = 8
reset = attr(0)

print(""">> You have 8 TRIES to guess the colours
    > Each guess consists of 4 numbers (separated by " "), each number representing a colour\n
    >> After typing the numbers, The MASTERMIND will tell you how many are correct
    > red dot = correct number on correct position
    > white dot = correct number on wrong position\n
    > START!...and do not disappoint me!\n""")


def verdict(array):
    global master
    compare = []
    index = 0

    for element in array:
        if array[index] == master[index]:
            compare.append(1)
        elif element in master:
            compare.append(0)
        index += 1
    return sorted(compare, reverse=True), array


while maxTries:
    maxTries -= 1

    for x in range(7):
        print(x+1, end="     ")
    print(8)

    for x in range(7):
        color = fg(colourCode[x])
        reset = attr('reset')
        print(color + '*' + reset, end="     ")
        if x % 3 != 0:
            print(end=" ")

    color = fg(colourCode[7])
    print(color + '*' + reset)

    currentGuess = []
    while len(currentGuess) < 4:
        if len(currentGuess) == 3:
            char = ["colour"]
        else:
            char = ["colours"]
        print("Choose {0} more {1} (1 - 8)".format(4 - len(currentGuess), *char))
        part2 = [int(x) for x in input().split() if 0 < int(x) < 9]
        for x in range(min(4 - len(currentGuess), len(part2))):
            currentGuess.append(int(part2[x]))

    output, lst = verdict(currentGuess)

    if len(output) == 4 and 0 not in output:
        print("You WON!")
        print("The colours were", end=" ")
        for x in master:
            color = fg(colourCode[x - 1])
            print(color + '*' + reset, end=" ")
        break

    else:
        print("Input")
        for x in lst:
            color = fg(colourCode[x-1])
            print(color + '*' + reset, end=" ")
        print()

        print("Output")
        for x in output:
            if x == 1:
                print(colored('*', 'red'), end=" ")
            else:
                print(colored('*', 'white'), end=" ")
        print()

        if maxTries > 0:
            colour = fg(1)
            print("and you have {0} more tries!".format(colour + str(maxTries) + reset))
            print('\n')
        else:
            print("You DONKEY!")
            print("The colours were", end=" ")
            for x in master:
                color = fg(colourCode[x - 1])
                print(color + '*' + reset, end=" ")
