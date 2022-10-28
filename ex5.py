def min_number(given_list):
    return min(given_list)


def max_number(given_list):
    return max(given_list)


def avg_number(given_list):
    return sum(given_list) / len(given_list)


def num_duplicates(given_list):
    new_dict = {}
    for x in given_list:
        if x in new_dict.keys():
            new_dict[x] += 1
        else:
            new_dict[x] = 1

    duplicates = 0
    for x in new_dict.keys():
        if new_dict[x] > 1:
            duplicates += (new_dict[x] - 1)
    return duplicates


def num_mode(given_list):
    new_dict = {}
    for x in given_list:
        if x in new_dict.keys():
            new_dict[x] += 1
        else:
            new_dict[x] = 1
    max_key = 0
    for a, b in new_dict.items():
        if new_dict[a] > max_key:
            max_key = a
    return max_key


if __name__ == '__main__':
    list_1 = [2, 3, 4, 4, 4, 5, 6, 6, 8, 9, 9, 9, 9, 9, 4, 4, 4, 4]

    print(min_number(list_1))
    print(max_number(list_1))
    print(avg_number(list_1))
    print(num_duplicates(list_1))
    print(num_mode(list_1))


