import csv

with open("../2020/input/01.csv", 'r', newline='') as input:
    nums = list(map(int,list(csv.reader(input, delimiter=','))[0]))

# Part 1
for num in nums:
    if (2020 - num) in nums:
        print(num * (2020-num))
        break

# Part 2
mini = min(nums)
found = False
for num in nums:
    if (num < 2020 - 2 * mini):
        for num1 in nums:
            if num1 < 2020 - num - mini:
                if 2020 - num - num1 in nums:
                    print(num * num1 * (2020 - num - num1))
                    found = True
                    break
        if found:
            break

