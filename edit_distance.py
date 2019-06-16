# Uses python3
def edit_distance(s, t):
    r,c =  len(s),len(t)
    cache = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

    for i in range(len(cache[0])):
        cache[0][i] = i
    for j in range(len(cache)):
        cache[j][0] = j

    for i in range(1, len(cache)):
        for j in range(1, len(cache[0])):
            if s[i-1] == t[j-1]:
                cache[i][j] = cache[i-1][j-1]
            else:
                cache[i][j] = 1+ min(cache[i-1][j],cache[i][j-1],cache[i-1][j-1])
    return cache[r][c]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
