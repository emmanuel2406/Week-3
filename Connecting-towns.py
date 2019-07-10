test_cases = int(input())
array = []
for i in range(test_cases):
    input()
    array.append(input())
for route in array:
    product = 1
    for num in route.split(' '):
        product *= int(num)
    print(product)