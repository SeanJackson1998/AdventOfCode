import csv

with open("2020/input/04.csv", 'r', newline='') as input:
    data = list(csv.reader(input, delimiter=','))

# Part 1
valid = 0
for creds in data:
    credentials = dict()
    for cred in creds:
        credentials[str(cred).split(":")[0]] = str(cred).split(":")[1]
    if ('cid' in credentials.keys() and len(credentials) == 8) or (
            'cid' not in credentials.keys() and len(credentials) == 7):
        valid += 1
print(valid)

# Part 2

valid = 0


def validBYR(byr):
    return 1920 <= int(byr) <= 2002


def validIYR(iyr):
    return 2010 <= int(iyr) <= 2020


def validEYR(eyr):
    return 2020 <= int(eyr) <= 2030


def validHGT(hgt):
    if 'in' in hgt:
        return 59 <= int(hgt.partition('in')[0].strip()) <= 76
    elif 'cm' in hgt:
        return 150 <= int(hgt.partition('cm')[0].strip()) <= 193
    return False


def validHCL(hcl):
    allowed_chars = set('1234567890abcdef')
    return '#' in hcl and len(hcl[1:]) == 6 and set(hcl[1:]).issubset(allowed_chars)


def validECL(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validPID(pid):
    return len(pid) == 9 and pid.isnumeric()


def isValid(c):
    if validBYR(c['byr']) and \
            validIYR(c['iyr']) and \
            validEYR(c['eyr']) and \
            validHGT(c['hgt']) and \
            validHCL(c['hcl']) and \
            validECL(c['ecl']) and \
            validPID(c['pid']):
        return True
    return False


for creds in data:
    credentials = dict()
    for cred in creds:
        credentials[str(cred).split(":")[0]] = str(cred).split(":")[1]
    if ('cid' in credentials.keys() and len(credentials) == 8) or (
            'cid' not in credentials.keys() and len(credentials) == 7):
        if isValid(credentials):
            valid += 1
print(valid)
