file = open("../2020/input/08.txt", 'r')
data = [(line.split(" ")[0], line.split(" ")[1]) for line in file.read().splitlines()]

# Part 1
i = 0
total = 0
command = data[i]
previous = []
while i not in previous:
    previous.append(i)
    print(command)
    if command[0] == 'jmp':
        i += int(command[1])
    elif command[0] == 'acc':
        total += int(command[1])
        i += 1
    elif command[0] == 'nop':
        i += 1
    command = data[i]

print(total)
