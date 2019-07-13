def isprime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
N = int(input('N?\n'))
array = []
for j in range(N):
    array.append(int(input()))
for inp1 in array:
    l = []
    for inp2 in range(1,inp1 + 1):
        count = 0
        for num in range(1,inp2 + 1):
            if inp2 % num == 0 and isprime(num) is True:
                count += 1
        l.append(count)
    print(max(l))