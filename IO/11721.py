s = list(input())
cnt = 0
for i in s:
    cnt += 1
    print(i, end="")
    if cnt % 10 == 0:
        cnt = 0
        print()
