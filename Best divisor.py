def str_sum(n):
    output = 0
    for char in str(n):
        output += int(char)
    return output
n = int(input("Enter n\n"))
best_div = n
array = []
for num in range(n - 1,0,-1):
    if n % num == 0:
        array.append(num)
for factor in array:
    if str_sum(factor) > str_sum(best_div):
        best_div = factor
    elif  str_sum(factor) == str_sum(best_div):
        best_div = factor
print(best_div)
    
