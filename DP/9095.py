t = int(input())
for _ in range(t):
    n = int(input())
    d = [1, 2, 4, 7] + [0] * n
    if n > 4:
        for i in range(4, n+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n-1])
