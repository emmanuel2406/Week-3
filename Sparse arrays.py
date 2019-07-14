strings = []
queries = []
for i in range(int(input())):
    strings.append(input())
for j in range(int(input())):
    queries.append(input())
for query in queries:
    print(strings.count(query))
