array = []
for i in range(int(input())):
    array.append(list(map(int , input().split(' '))))
for pair in array:
    product = pair[0] * pair[1]
    factors = []
    for num in range(1,min(pair) + 1):
        if pair[0] % num == 0 and pair[1] % num  == 0:
            factors.append(num)
    print(int(product / (max(factors)** 2)))
