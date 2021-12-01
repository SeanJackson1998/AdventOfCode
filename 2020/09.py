file = open("../2020/input/09.txt", 'r')
data = [int(x) for x in file.read().splitlines()]

# Part 1
preamble = data[:25]
numbers = data[25:]

for i in numbers:
    invalid = False
    for p in preamble:
        if i - p in preamble and i - p is not p:
            invalid = True
            break
    preamble = preamble[-24:] + [i]
    if not invalid:
        print(i)

# Part 2
value = 1721308972

print(len(data))
