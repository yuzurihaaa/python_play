def make_hashtable(nbuckets):
    a = []
    for e in range(0, nbuckets):
        a.append([])
    return a


if __name__ == '__main__':
    print(make_hashtable(6))
    if 4 % 2:
        print('true')
    else:
        print('false')