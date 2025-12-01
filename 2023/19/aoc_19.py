# AOC Day 19
with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

from functools import lru_cache

empty_list_index = [index for index, sublist in enumerate(lines) if sublist == []][0]

workflow = [line[0] for line in lines[:empty_list_index]]
rating = [line[0] for line in lines[(empty_list_index + 1) :]]
import re


@lru_cache(maxsize=None)
def extract_rating_numeric(rating_item, letter):
    pattern = f"{letter}=(\d+)"
    match = re.search(pattern, rating_item)
    return match.group(1)


@lru_cache(maxsize=None)
def extract_workflow_name(workflow_item):
    pattern = r"(.*?)\{"
    match = re.search(pattern, workflow_item)
    return match.group(1)


@lru_cache(maxsize=None)
def extract_workflow_substrings(workflow_item):
    pattern = r"[{,]([^,}]+)"
    matches = re.findall(pattern, workflow_item)
    return matches


@lru_cache(maxsize=None)
def compare_integers(num1, num2, comp_char):
    if comp_char == ">":
        return num1 > num2
    elif comp_char == "<":
        return num1 < num2
    elif comp_char == "<=":
        return num1 <= num2
    elif comp_char == "<=":
        return num1 <= num2


@lru_cache(maxsize=None)
def extract_workflow_return(workflow_item):
    pattern = r":(.*)"
    match = re.search(pattern, workflow_item).group(1)
    return match


@lru_cache(maxsize=None)
def sum_rating_digits(rating_item):
    digits = re.findall(r"\d+", rating_item)
    return sum(int(digit) for digit in digits)


def get_return_value(rating_item, workflow_name):
    for w in workflow:

        name = extract_workflow_name(w)

        if name == workflow_name:

            substrings = extract_workflow_substrings(w)

            for s in substrings:

                if ":" in s:

                    char = s[0]
                    comparator = s[1]
                    workflow_value = int(re.search(r"(\d+)", s).group(0))

                    rating_value = int(extract_rating_numeric(rating_item, char))

                    if compare_integers(rating_value, workflow_value, comparator):

                        return_value = extract_workflow_return(s)

                        break
                else:

                    return_value = s

    return return_value


partone = 0
for rating_item in rating:
    workflow_name = "in"

    while True:
        workflow_name = get_return_value(rating_item, workflow_name)
        if workflow_name == "A":

            sum_value = sum_rating_digits(rating_item)
            partone += sum_value
            break

        if workflow_name == "R":
            break


## Part 2
def extract_workflow_pipeline(
    workflow_name, workflow_item, inital_swtich=False, inital_value=""
):

    if inital_swtich:
        workflow_search = inital_value
    else:
        workflow_search = workflow_name

    if (
        f"{workflow_search}" + "{" in workflow_item
        and ":A," in workflow_item
        or f":{workflow_name}" in workflow_item
    ):

        items = pattern = re.sub(r".*?\{", "", workflow_item).split(",")
        index_match = [i for i, item in enumerate(items) if workflow_name in item][0]
        items_a = items[:index_match]

        items_aa = [
            re.search(r"^(.*?):", match1)
            .group(1)
            .replace("<", "#")
            .replace(">", "<=")
            .replace("#", ">=")
            for match1 in items_a
        ]
        items_b = [re.search(r"^(.*?):", items[index_match]).group(1)]

        return items_aa + items_b
    elif (
        f"{workflow_search}" + "{" in workflow_item
        and ",A" + "}" in workflow_item
        or f",{workflow_name}" + "}" in workflow_item
    ):

        user_input = "," + workflow_name
        pattern = r"\{(.*?)\b" + re.escape(user_input)
        match = re.search(pattern, workflow_item)
        matches = match.group(1).split(",")
        matches_clean = [
            re.search(r"^(.*?):", match1)
            .group(1)
            .replace("<", "#")
            .replace(">", "<=")
            .replace("#", ">=")
            for match1 in matches
        ]
        return matches_clean


def update_store(store, comparator, num):
    if comparator == "<":
        store = (store[0], min(store[1], num - 1))
    elif comparator == "<=":
        store = (store[0], min(store[1], num))
    elif comparator == ">":
        store = (max(store[0], num + 1), store[1])
    elif comparator == ">=":
        store = (max(store[0], num), store[1])
    return store


def extract_workflow_a(workflow_name, workflow_item):

    items = re.sub(r".*?\{", "", workflow_item).split(",")

    index_match = [i for i, item in enumerate(items) if "A" in item]
    store = []
    for a in index_match:
        if f":A" in workflow_item:

            items_a = items[: a + 1]

            items_aa = [re.search(r"^(.*?):", items_a[-1]).group(1)]

            if a != 0:
                items_b = [
                    re.search(r"^(.*?):", match1)
                    .group(1)
                    .replace("<", "#")
                    .replace(">", "<=")
                    .replace("#", ">=")
                    for match1 in items_a[:-1]
                ]
            else:
                items_b = []

            store.append(items_aa + items_b)

            workflow_item = workflow_item.replace("A", "X", 1)

        elif f",A" + "}" in workflow_item:

            if index_match == 0:
                continue
            else:
                matches_clean = [
                    re.search(r"^(.*?):", match1)
                    .group(1)
                    .replace("<", "#")
                    .replace(">", "<=")
                    .replace("#", ">=")
                    for match1 in items[:-1]
                ]
                matches_clean
                store.append(matches_clean)
    return store


workflow_pos = []
for wp in workflow:
    if "A}" in wp or ":A" in wp:
        workflow_pos.append(wp)
import copy

super_store = []
for w1 in workflow_pos:
    wp_name = extract_workflow_name(w1)
    wp_name_copy = copy.deepcopy(wp_name)
    init_store = extract_workflow_a(wp_name, w1)

    for init in init_store:
        store = init
        wp_name = wp_name_copy
        workflow1 = copy.deepcopy(workflow)
        breakflag = True
        while breakflag:
            for w in workflow:
                if (
                    f",{wp_name}" + "}" in w
                    or f":{wp_name}" + "}" in w
                    or f",{wp_name}," in w
                    or f":{wp_name}," in w
                ):

                    string = extract_workflow_pipeline(wp_name, w)
                    for s in string:
                        store.append(s)
                    wp_name = extract_workflow_name(w)
                    if wp_name == "in":
                        breakflag = False
                        super_store.append(store)
                    continue
super_critical = []
for store in super_store:
    xpos = (1, 4000)
    mpos = (1, 4000)
    apos = (1, 4000)
    spos = (1, 4000)

    for x in store:

        comp = "".join(re.findall(r"[^a-zA-Z0-9\s]", x))
        char = x[0]
        digits = int(re.findall(r"(\d+)", x)[0])

        if char == "x":
            xpos = update_store(xpos, comp, digits)
        elif char == "m":
            mpos = update_store(mpos, comp, digits)
        elif char == "a":
            apos = update_store(apos, comp, digits)
        elif char == "s":
            spos = update_store(spos, comp, digits)

    crit = [xpos, mpos, apos, spos]
    super_critical.append(crit)
from functools import reduce

parttwo = 0
for y in super_critical:
    val_store = []
    for x in y:
        val = x[1] - x[0] + 1
        val_store.append(val)
    value = reduce(lambda x, y: x * y, val_store)
    parttwo += value
print(partone)
print(parttwo)
