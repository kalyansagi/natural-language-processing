def editdistancealgorithm(string1: str, string2: str) -> int:
    if len(string1) == 0:
        return len(string2)
    if len(string2) == 0:
        return len(string1)
    previous_row = list(range(len(string2) + 1))
    # iterating through the string1
    for i, c1 in enumerate(string1):
        current_row = [i + 1]
        # iterating through the string2
        for j, c2 in enumerate(string2):
            # finding the costs
            insert = previous_row[j + 1] + insertionCost
            delete = current_row[j] + deletionCost
            if c1 != c2:
                replace = previous_row[j] + replaceCost
            else:
                replace = previous_row[j] + 0
            # find the min and append to current row
            current_row.append(min(insert, delete, replace))
        previous_row = current_row
    # return final element in the matrix. i.e., min distance needed to match the strings.
    return previous_row[-1]


if __name__ == "__main__":
    string1 = input('Enter String1:\n')
    string2 = input('Enter String2:\n')
    insertionCost = int(input('Enter cost you wish to use for insert operation:\n'))
    deletionCost = int(input('Enter cost you wish to use for delete operation:\n'))
    replaceCost = int(input('Enter cost you wish to use for replace operation:\n'))

    output = editdistancealgorithm(string1, string2)
    print('Minimum Edit Distance is', output)
