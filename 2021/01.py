file = open("../2021/input/01.txt", 'r')
data = [int(line.strip()) for line in file.read().splitlines()]

increased_counter = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        increased_counter += 1
print(increased_counter)


increased_counter = 0
for i in range(1, len(data)):
    if sum(data[i:i+3]) > sum(data[i-1:i+2]):
        increased_counter += 1
print(increased_counter)