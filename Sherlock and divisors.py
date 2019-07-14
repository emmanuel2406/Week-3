array = []
for i in range(int(input())):
    array.append(int(input()))
for case in array:
    count = 0
    for num in range(1, case + 1):
        if case % num == 0 and num % 2 == 0:
            count += 1
    print(count)
