n = int(input("Number of sets of points\n"))
array = []
for i in range(n):
    array.append(input().split(' '))
for pair in array:
    pair = list(map(int,pair))
    x = 0
    y = 0
    if pair[0] < pair[2]:
        x = pair[2] + abs(pair[0] - pair[2])
    elif pair[0] > pair[2]:
        x = pair[2] - abs(pair[0] - pair[2])
    if pair[1] < pair[3]:
        y = pair[3] + abs(pair[1] - pair[3])
    elif pair[1] > pair[3]:
        y = pair[3] - abs(pair[1] - pair[3])
    print(x,y)
