#Uses python3

import sys

def lcs2_recursion(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    elif a[0] == b[0]:
        return 1 + lcs2_recursion(a[1:],b[1:])
    else:
        return max((lcs2_recursion(a[1:],b)),lcs2_recursion(a,b[1:]))


def lcs2(a,b):
    r, c = len(a), len(b)
    if r == 0 or c == 0:
        return 0
    cache = [[0 for _ in range(c+1)] for _ in range(r+1)]
    for i in range(1, len(cache)):
        for j in range(1, len(cache[0])):
            if a[i-1] == b[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j],cache[i][j-1])
    return cache[i][j]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
