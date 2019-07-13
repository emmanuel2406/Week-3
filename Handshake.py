T = int(input())
array = []
for i in range(T):
    array.append(int(input()))
for a in array:
    print(a*(a-1)//2)