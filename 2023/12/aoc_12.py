with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

score = 0
for line in lines:
    string = line[0]
    test = [int(int1) for int1 in line[1].split(",")]

    # Get number of question marks
    question_mark_count = sum(1 for char in string if char == "?")

    # Get number of hash
    sumcount = sum(test)
    hash_count = sum(1 for char in string if char == "#")

    # Get position of question marks
    question_mark_index = [i for i, ind in enumerate(string) if ind == "?"]

    from itertools import product

    # Generate all possible combinations of '#' and '.' of length 9
    combinations = list(product("#.", repeat=question_mark_count))

    # Create all combinations of solutions
    for comb in combinations:
        if sum(1 for char in comb if char == "#") == sumcount - hash_count:
            list1 = string
            for i in range(0, len(comb)):
                list1 = (
                    list1[: question_mark_index[i]]
                    + comb[i]
                    + list1[question_mark_index[i] + 1 :]
                )

            t1 = [i for i, ind in enumerate(list(list1)) if ind == "#"]
            counts = []
            count = 1
            for i in range(1, len(t1)):
                if t1[i] == t1[i - 1] + 1:
                    count += 1
                else:
                    counts.append(count)
                    count = 1

            counts.append(count)
            score += counts == test
print(score)

score = 0
for line in lines:
    string = line[0] * 5
    test = [int(int1) for int1 in line[1].split(",")] * 5

    # Get number of question marks
    question_mark_count = sum(1 for char in string if char == "?")

    # Get number of hash
    sumcount = sum(test)
    hash_count = sum(1 for char in string if char == "#")

    # Get position of question marks
    question_mark_index = [i for i, ind in enumerate(string) if ind == "?"]

    from itertools import product

    # Generate all possible combinations of '#' and '.' of length 9
    combinations = list(product("#.", repeat=question_mark_count))

    # Create all combinations of solutions
    for comb in combinations:
        if sum(1 for char in comb if char == "#") == sumcount - hash_count:
            list1 = string
            for i in range(0, len(comb)):
                list1 = (
                    list1[: question_mark_index[i]]
                    + comb[i]
                    + list1[question_mark_index[i] + 1 :]
                )

            t1 = [i for i, ind in enumerate(list(list1)) if ind == "#"]
            counts = []
            count = 1
            for i in range(1, len(t1)):
                if t1[i] == t1[i - 1] + 1:
                    count += 1
                else:
                    counts.append(count)
                    count = 1

            counts.append(count)
            score += counts == test
print(score)
