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
    correct = [[1, 2, 3],
               [2, 3, 1],
               [3, 1, 2]]

    incorrect = [[1, 2, 3, 4],
                 [2, 3, 1, 3],
                 [3, 1, 2, 3],
                 [4, 4, 4, 4]]

    incorrect2 = [[1, 2, 3, 4],
                  [2, 3, 1, 4],
                  [4, 1, 2, 3],
                  [3, 4, 1, 2]]

    incorrect3 = [[1, 2, 3, 4, 5],
                  [2, 3, 1, 5, 6],
                  [4, 5, 2, 1, 3],
                  [3, 4, 5, 2, 1],
                  [5, 6, 4, 3, 2]]

    incorrect4 = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    incorrect5 = [[0, 1, 2],
                  [2, 0, 1],
                  [1, 2, 0]]


    def check_sudoku(sudoku):
        n = len(sudoku)
        i = 0
        while i < n:
            j = 0
            while j < n:
                current_digit = sudoku[i][j]
                occurence_column = 0
                k = 0
                while k < n:
                    if not isinstance(sudoku[k][j], int) or sudoku[k][j] < 1:
                        return False
                    if len(str(sudoku[k][j])) > 3:
                        return False
                    if sudoku[k].count(current_digit) > 1:
                        return False
                    if current_digit == sudoku[k][j]:
                        occurence_column += 1
                    if sudoku[k][j] > len(sudoku[0]) or not isinstance(sudoku[k][j], int):
                        return False
                    if occurence_column > 1:
                        return False
                    k += 1
                j += 1
            i += 1
        return True


    print(check_sudoku(incorrect))
    # # >>> False
    #
    print(check_sudoku(correct))
    # # >>> True
    #
    print(check_sudoku(incorrect2))
    # # >>> False
    #
    print(check_sudoku(incorrect3))
    # # >>> False

    print(check_sudoku(incorrect4))
    # >>> False

    print(check_sudoku(incorrect5))
    # >>> False

    # b = ['banana', 'apple', 'microsoft']
    #
    # # in phyton we can swap the value just like this
    # b[0], b[2] = b[2], b[0]
    #
    # print(b)
    #
    # for_loops()
    # modular()
    #
    # s = 'CidatuUcityda'
    #
    # print(s[6] + s[2:4] + s[7:13])
    #
    #
    # def factorial(n):
    #     if n == 1 or n == 0:
    #         return n
    #     return n * factorial(n - 1)
    #
    #
    # print(factorial(5))
    #
    #
    # def find_last(string, target):
    #     last_post = string.find(target)
    #     while True:
    #         pos = string.find(target, last_post + 1)
    #         if pos == -1:
    #             return last_post
    #         last_post = pos
    #
    #
    # print(find_last('aaaa', 'a'))
    #
    # print(find_last('aaaaa', 'aa'))
    #
    # print(find_last('aaaa', 'b'))
    #
    # print(find_last("111111111", "1"))
    #
    # print(find_last("222222222", ""))
    #
    # print(find_last("", "3"))
    #
    # print(find_last("", ""))
    #
    # def stamps(num):
    #     a = 0
    #     b = 0
    #     c = 0
    #     while num - 5 >= 0:
    #         num = num - 5
    #         a += 1
    #
    #     while num - 2 >= 0:
    #         num = num - 2
    #         b += 1
    #
    #     while num - 1 >= 0:
    #         num = num - 1
    #         c += 1
    #
    #     return a, b, c
    #
    #
    # print(stamps(0))
