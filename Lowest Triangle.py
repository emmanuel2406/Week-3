inp = input()
b = int(inp.split(' ')[0])
a = int(inp.split(' ')[1])
ans1 = a*2 /b
ans2 = a*2 // b
if ans1 == ans2:
    print(ans2)
else:
    print(ans2 + 1)