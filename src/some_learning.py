def for_loops():
    a = list(range(1, 5))
    print(a)

    total = 0
    for number in a:
        print(number)
        total += number

    print(total)


def modular():
    total = 0
    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            total += number

    print(total)


if __name__ == '__main__':
    b = ['banana', 'apple', 'microsoft']

    # in phyton we can swap the value just like this
    b[0], b[2] = b[2], b[0]

    print(b)

    for_loops()
    modular()