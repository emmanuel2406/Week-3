grid = []
for i in range(6):
    grid.append(input().split(' '))
sums = []
for row in grid[:4]:
    for num in row[:4]:
        sum = int(num)
        sum += int(row[row.index(num) + 1])
        sum += int(row[row.index(num) + 2])
        sum += int(grid[grid.index(row) + 1][row.index(num) + 1])
        sum += int(grid[grid.index(row) + 2][row.index(num) + 1])
        sum += int(grid[grid.index(row) + 2][row.index(num) + 2])
        sum += int(grid[grid.index(row) + 2][row.index(num)])
        sums.append(sum)
print(max(sums))
        