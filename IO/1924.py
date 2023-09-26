x, y = map(int, input().split())
z = 0

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

for i in range(1, x):
    if i in month_31:
        z += 31
    elif i in month_30:
        z += 30
    else:
        z += 28
y += z
y %= 7

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(day[y-1])
