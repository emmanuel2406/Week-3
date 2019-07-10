inp = input("Input:\n")
n = int(inp.split(' ')[0])
d = int(inp.split(' ')[1])
d = d % n
array = input()
array = array.split(' ')
output = ''
for char in array[d:]:
    output += char
for character in array[:d]:
    output += character
print(' '.join(output))
