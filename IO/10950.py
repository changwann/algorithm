t = int(input())
result = []
for i in range(t):
    a, b = input().split()
    result.append(int(a)+int(b))
for i in range(t):
    print(result[i])
