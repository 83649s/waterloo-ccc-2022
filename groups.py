def main():
    # Same group
    x = int(input())

    required_pairs = []
    for i in range(x):
        group = str(input())
        group_list = group.split()
        required_pairs.append(group_list)

    # Diff group
    y = int(input())

    banned_pairs = []
    for i in range(y):
        group = str(input())
        group_list = group.split()
        banned_pairs.append(group_list)

    real_pairs = []
    g = int(input())
    for i in range(g):
        group = str(input())
        group_list = group.split()
        real_pairs.append(group_list)

    rules_violated = 0

    # Check for banned pairs in groups
    for i in banned_pairs:
        is_violated = False
        for j in real_pairs:
            if check_pairs_bad(i, j) == False and is_violated == False:
                is_violated = True
                rules_violated += 1
    
    # Check for required pairs in groups
    for i in required_pairs:
        is_violated = False
        for j in real_pairs:
            if check_pairs(i, j) == False and is_violated == False:
                is_violated = True
                rules_violated += 1
    
    print(rules_violated)


def check_pairs(pair, group):
    pair_one_found = False
    pair_two_found = False
    for i in group:
        if pair[0] == i:
            pair_one_found = True
        if pair[1] == i:
            pair_two_found = True
    if pair_one_found == True and pair_two_found == True:
        return True
    elif pair_one_found == False and pair_two_found == False:
        return True
    else:
        return False

def check_pairs_bad(pair, group):
    pair_one_found = False
    pair_two_found = False
    for i in group:
        if pair[0] == i:
            pair_one_found = True
        if pair[1] == i:
            pair_two_found = True
    if pair_one_found == True and pair_two_found == True:
        return False
    else:
        return True

if __name__ == '__main__':
    main()