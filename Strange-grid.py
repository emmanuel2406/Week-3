inp = input().split(' ')
r = int(inp[0])
c = int(inp[1])
odds = [1, 3, 5, 7, 9]
evens = [0, 2, 4, 6, 8]
tens = 0
unit = 0
tens = 10 * ((r+1)//2 - 1)
if r % 2 == 0:
    unit = odds[c-1]
else:
    unit = evens[c-1]
print(tens + unit)
