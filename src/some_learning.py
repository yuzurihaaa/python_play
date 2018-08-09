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

    s = 'CidatuUcityda'

    print(s[6] + s[2:4] + s[7:13])


    def factorial(n):
        if n == 1 or n == 0:
            return n
        return n * factorial(n - 1)


    print(factorial(5))


    def find_last(string, target):
        last_post = string.find(target)
        while True:
            pos = string.find(target, last_post + 1)
            if pos == -1:
                return last_post
            last_post = pos


    print(find_last('aaaa', 'a'))

    print(find_last('aaaaa', 'aa'))

    print(find_last('aaaa', 'b'))

    print(find_last("111111111", "1"))

    print(find_last("222222222", ""))

    print(find_last("", "3"))

    print(find_last("", ""))

    def stamps(num):
        a = 0
        b = 0
        c = 0
        while num - 5 >= 0:
            num = num - 5
            a += 1

        while num - 2 >= 0:
            num = num - 2
            b += 1

        while num - 1 >= 0:
            num = num - 1
            c += 1

        return a, b, c


    print(stamps(0))