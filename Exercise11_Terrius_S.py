row = int(input())
star = 1
space = row - 1

for i in range(row):
    print(" " * space + "*" * star)
    star += 2
    space -= 1
