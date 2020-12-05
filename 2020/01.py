file = open("../2020/input/01.txt", 'r')
nums = [int(x) for x in file.read().splitlines()]

# Part 1
for num in nums:
    if (2020 - num) in nums:
        print(num * (2020-num))
        break

# Part 2
mini = min(nums)
found = False
for num in nums:
    if num < 2020 - 2 * mini:  # if the number is < 2020 - 2 of the min value in the list
        for num1 in nums:
            if num1 < 2020 - num - mini:  # if the number < 2020 - num and the min value
                if 2020 - num - num1 in nums:  # if the result of the subtraction is in the list then they sum to 2020
                    print(num * num1 * (2020 - num - num1))
                    found = True
                    break
        if found:
            break
