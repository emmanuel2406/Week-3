array = []
for i in range(int(input())):
    array.append(list(map(int, input().split(' '))))
for case in array:
    balls = []
    for j in range(case[0]):
        balls.append(j)
    length = len(balls)
    output = []
    while len(output) != length:
        balls = balls[::-1]
        output.append(balls[0])
        balls.pop(0)
    print(output.index(case[1]))
