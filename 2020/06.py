file = open("../2020/input/06.txt", 'r')
data = file.read().splitlines()

# Part 1
answers = set()
total = 0

for d in data:
    if d == '':
        total += len(answers)
        answers = set()
    else:
        answers.update(list(d))
print(total)

# Part 2
answers = set()
total = 0
blank = True

for d in data:
    if blank:
        answers = set(list(d))
        blank = False
    else:
        if d == '':
            total += len(answers)
            blank = True
        else:
            answers = answers.intersection(set(list(d)))
print(total)
