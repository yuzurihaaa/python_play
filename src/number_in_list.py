# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

# Hint - "int()" turns a string's element into a number


def numbers_in_lists(input):
    input_to_list = list(input)
    final_list = [int(input_to_list[0])]
    new_list = []
    i = 1
    while i < len(input_to_list):
        current_number = int(input_to_list[i])
        previous_number = int(input_to_list[i - 1])
        max_number = 0
        if new_list:
            max_number = max(new_list)

        if current_number < previous_number:

            new_list.append(current_number)
            if i == len(input_to_list) - 1:
                final_list.append(new_list)
        elif current_number < previous_number \
                or current_number == previous_number or \
                current_number <= max_number:

            new_list.append(current_number)
            if i == len(input_to_list) - 1:
                final_list.append(new_list)
        else:

            if new_list:
                final_list.append(new_list)
            final_list.append(current_number)
            new_list = []
        i += 1

    print(final_list)
    return final_list


if __name__ == '__main__':
    # testcases
    string = '543987'
    result = [5, [4, 3], 9, [8, 7]]
    print(repr(string), numbers_in_lists(string) == result)
    string = '987654321'
    result = [9, [8, 7, 6, 5, 4, 3, 2, 1]]
    print(repr(string), numbers_in_lists(string) == result)
    string = '455532123266'
    result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
    print(repr(string), numbers_in_lists(string) == result)
    string = '123456789'
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(repr(string), numbers_in_lists(string) == result)
