import ast

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

questionMarks = [[3, 0], [2, 3], [6, 3], [1, 5], [3, 6], [6, 6]]

winningPaths = ""
with open('winners.txt', 'r') as f:
    winningPaths = f.read()

winningPaths = winningPaths.split('\n')

pathList = []
for x in range(0, len(winningPaths)):
    if (winningPaths[x] == ''):
        continue
    asList = ast.literal_eval(winningPaths[x])
    newList = []
    for subList in asList:
        newList.append([subList[0], subList[1]])
    pathList.append(newList)

newPathList = []
for x in range(0, len(pathList)):
    for questionSquare in questionMarks:
        path = pathList[x]
        numOccurences = path.count(questionSquare)
        if (numOccurences <= 1):
            continue
        # remove everything from first to last index
        firstIndex = path.index(questionSquare)
        lastIndex = len(path) - 1 - path[::-1].index(questionSquare)

        path = path[:firstIndex] + path[lastIndex:]
        if path not in newPathList:
            newPathList.append(path)

shortestPath = newPathList[0]
for newPath in newPathList:
    if len(newPath) < len(shortestPath):
        shortestPath = newPath

for x in range(0, len(shortestPath)):
    shortestPath[x] = [shortestPath[x][0] + 1, 8 - shortestPath[x][1]]

print(shortestPath)
