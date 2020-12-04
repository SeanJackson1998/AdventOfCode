import csv

with open("../2020/input/02.csv", 'r', newline='') as input:
    data = list(csv.reader(input, delimiter=','))

# Part 1
count = 0
for d in data:
    if int(d[0]) <= str(d[3]).count(d[2]) <= int(d[1]):
        count += 1
print(count)

# Part 2
count = 0
for d in data:
    if int(d[0]) <= len(str(d[3])) and int(d[1]) <= len(str(d[3])):
        if (str(d[3])[int(d[0])-1] is d[2] and str(d[3])[int(d[1])-1] is not d[2]) or (str(d[3])[int(d[0])-1] is not d[2] and str(d[3])[int(d[1])-1] is d[2]):
            count += 1
print(count)
