array = []
for i in range(int(input())):
    array.append(int(input()))
for case in array:
    ans = 0
    for num in range(1, case + 1):
        ans += num**2 - (num - 1)**2
    print(ans)
