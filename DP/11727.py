n = int(input())
d = [1, 3] + [0] * (n-1)
for i in range(2, n):
    d[i] = d[i-1] + 2 * d[i-2]
print(d[n-1] % 10007)
