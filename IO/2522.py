n = int(input())  # 3
for i in range(n):  # 0, 1, 2
    print(" "*(n-i-1) + "*"*(i+1))
for i in range(n-2, -1, -1):  # 1, 0
    print(" "*(n-i-1) + "*"*(i+1))
