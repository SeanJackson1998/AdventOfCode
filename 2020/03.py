file = open("2020/input/03.txt", 'r')
data = file.read().splitlines()

# Part 1
trees = 0
fromleft = 0
lineLength = 31
for d in data:
    if fromleft >= lineLength:
        fromleft -= lineLength
    if d[fromleft] == '#':
        trees += 1
    fromleft += 3
print(trees)


# Part 2


def countTrees(right, down):
    trees = 0
    fromleft = 0
    for i in range(0, len(data), down):
        if fromleft >= lineLength:
            fromleft -= lineLength
        if data[i][fromleft] == '#':
            trees += 1
        fromleft += right
    return trees


print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))



