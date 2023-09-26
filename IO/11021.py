t = int(input())
result = []
for i in range(t):
    a, b = map(int, input().split())
    result.append(a+b)
for i in range(t):
    print(f"Case #{i+1}: {result[i]}")
