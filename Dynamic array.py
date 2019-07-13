inp = input()
N = int(inp.split(' ')[0])
seqList = []
for i in range (N):
    seqList.append([])
query = []
for i in range(int(inp.split(' ')[1])):
    query.append(input().split(' '))
lastAnswer = 0
for q in query:
    seqList[(int(q[1]) ^ lastAnswer) % N].append(int(q[2]))
    lastAnswer = int(q[2])
    if q[0] == 2:
        print("lastAnswer = ", lastAnswer)
#program does not work