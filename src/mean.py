def list_mean(array_input):
    if not array_input:
        return 0.0
    total = 0
    for number in array_input:
        total += number

    return total / len(array_input) * 1.0


print(list_mean([1, 2, 3, 4]))
print(list_mean([1, 3, 4, 5, 2]))
print(list_mean([]))
