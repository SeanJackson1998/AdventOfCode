file = open("../2021/input/02.txt", 'r')
instructions = [line.strip() for line in file.read().splitlines()]

forward = 0
depth = 0
for instruction in instructions:
    parts = instruction.split(" ")
    direction = parts[0].strip()
    quantity = int(parts[1].strip())
    if direction == "forward":
        forward += quantity
    elif direction == "up":
        depth -= quantity
    elif direction == "down":
        depth += quantity
print(forward * depth)


forward = 0
aim = 0
depth = 0
for instruction in instructions:
    parts = instruction.split(" ")
    direction = parts[0].strip()
    quantity = int(parts[1].strip())
    if direction == "forward":
        forward += quantity
        depth += (aim * quantity)
    elif direction == "up":
        aim -= quantity
    elif direction == "down":
        aim += quantity
print(forward * depth)