from numpy import sort

file = open("../2020/input/10.txt", 'r')
data = list(sort([int(x) for x in file.read().splitlines()]))

three = 1  # diff between mine and highest rated
one = 1  # diff between charger and lowest in the bag
for i in range(len(data)-1):
    if data[i+1] - data[i] == 3:
        three += 1
    elif data[i+1] - data[i] == 1:
        one += 1

print(three * one)
