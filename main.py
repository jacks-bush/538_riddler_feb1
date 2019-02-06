from enum import Enum
import random


class BreakOutAndStartOver(Exception):
    pass


class WinnerWinnerChickenDinner(Exception):
    pass


class SquareType(Enum):
    Left = 1
    Right = 2
    UTurn = 3
    Straight = 4
    Choose = 5
    Lava = 6
    SmileyFace = 7


maze = [
    ['L', 'U', 'U', '?', 'U', 'L', 'X', 'L'],
    ['R', 'L', 'R', 'L', 'U', 'E', 'U', 'U'],
    ['S', 'L', 'R', 'L', 'U', 'L', 'X', 'R'],
    ['U', 'R', '?', 'R', 'S', 'L', '?', 'R'],
    ['R', 'U', 'U', 'R', 'R', 'R', 'S', 'L'],
    ['S', '?', 'S', 'L', 'S', 'S', 'L', 'R'],
    ['R', 'L', 'R', '?', 'R', 'L', '?', 'L'],
    ['L', 'R', 'S', 'R', 'S', 'L', 'R', 'L']
]


def main(maze):
    nextInfo = getEntryPointAndDirection()
    path = [nextInfo]
    winnerPaths = []
    counter = 0
    while True:
        try:
            while True:
                nextInfo = getNextSquare(nextInfo)
                path.append(nextInfo)

                # watch for infinite loops
                if (len(path) > 300):
                    raise BreakOutAndStartOver()
        except BreakOutAndStartOver:
            nextInfo = getEntryPointAndDirection()
            path = [nextInfo]
        except WinnerWinnerChickenDinner:
            if path not in winnerPaths:
                winnerPaths.append(path)
            nextInfo = getEntryPointAndDirection()
            path = [nextInfo]
        counter += 1
        if counter > 10000:
            break

    for x in range(0, len(winnerPaths)):
        winnerPaths[x] = str(winnerPaths[x])
    with open('winners.txt', 'w') as f:
        f.write("\r\n".join(winnerPaths))


def getEntryPointAndDirection():
    x = 0
    y = 0
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if x % 7 == 0 or y % 7 == 0:
            break

    # get direction
    direction = ""
    if (x == 0 and y == 0):
        direction = 'right' if random.randint(0, 1) == 0 else 'down'
    elif (x == 0 and y == 7):
        direction = 'right' if random.randint(0, 1) == 0 else 'up'
    elif (x == 7 and y == 0):
        direction = 'left' if random.randint(0, 1) == 0 else 'down'
    elif (x == 7 and y == 7):
        direction = 'left' if random.randint(0, 1) == 0 else 'up'

    elif (x == 0):
        direction = 'right'
    elif (x == 7):
        direction = 'left'
    elif (y == 0):
        direction = 'down'
    elif (y == 7):
        direction = 'up'

    return [x, y, direction]


def getNextSquare(curInfo):
    x = curInfo[0]
    y = curInfo[1]
    direction = curInfo[2]

    nextDirection = ""

    curSquareContents = maze[y][x]

    if (curSquareContents == 'E'):
        raise WinnerWinnerChickenDinner('You won!')
    if (curSquareContents == 'X'):
        raise BreakOutAndStartOver('Nice try!')

    if (curSquareContents == 'S'):
        nextDirection = direction

    if (curSquareContents == 'L'):
        if (direction == 'up'):
            nextDirection = 'left'
        if (direction == 'down'):
            nextDirection = 'right'
        if (direction == 'left'):
            nextDirection = 'down'
        if (direction == 'right'):
            nextDirection = 'up'

    if (curSquareContents == 'R'):
        if (direction == 'up'):
            nextDirection = 'right'
        if (direction == 'down'):
            nextDirection = 'left'
        if (direction == 'left'):
            nextDirection = 'up'
        if (direction == 'right'):
            nextDirection = 'down'

    if (curSquareContents == 'U'):
        if (direction == 'up'):
            nextDirection = 'down'
        if (direction == 'down'):
            nextDirection = 'up'
        if (direction == 'left'):
            nextDirection = 'right'
        if (direction == 'right'):
            nextDirection = 'left'

    if (curSquareContents == '?'):
        nextDirInt = random.randint(1, 4)
        if (nextDirInt == 1):
            nextDirection = 'down'
        if (nextDirInt == 2):
            nextDirection = 'up'
        if (nextDirInt == 3):
            nextDirection = 'right'
        if (nextDirInt == 4):
            nextDirection = 'left'

    # increment points
    if (nextDirection == 'left'):
        x -= 1
    if (nextDirection == 'right'):
        x += 1
    if (nextDirection == 'up'):
        y -= 1
    if (nextDirection == 'down'):
        y += 1

    if (x < 0 or x > 7 or y < 0 or y > 7):
        raise BreakOutAndStartOver
    return [x, y, nextDirection]


main(maze)
