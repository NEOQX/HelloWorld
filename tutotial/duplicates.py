numbers = [2,2,3,8,4,5,4,7,7,6,6,9,2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)