inp = input()
n = int(inp.split(' ')[0])
m = int(inp.split(' ')[1])
array = []
grid = []
for i in range(m):
    grid.append(input().split(' '))
for j in range(n):
    array.append(0)
for row in grid:
    for num in array[int(row[0])-1:int(row[1])]:
        array[array.index(num)] += int(row[2])

print(max(array))