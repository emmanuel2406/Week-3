array = list(map(int, input().split(' ')))
output = 1
for num in array:
    if num % 2 == 1:
        output = output * ((num + 1) /2)
    else:
        output = output * (num/2)
print(int(output))