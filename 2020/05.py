file = open("../2020/input/05.txt", 'r')
data = file.read().splitlines()

# Part 1
ids = list()
for d in data:
    row = int(str(d)[:-3].replace('B', '1').replace('F', '0'), 2)  # getting first 7 chars, replacing with 1,0s then converting to decimal
    col = int(str(d)[7:].replace('R', '1').replace('L', '0'), 2)  # getting last 3 chars, replacing with 1,0s then converting to decimal
    ids.append(row * 8 + col)
print(max(ids))

# Part 2
for i in range(127 * 8 + 7):
    if i not in ids and i + 1 in ids and i - 1 in ids:
        print(i)
