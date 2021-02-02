from sys import stdin

read = stdin.readline
dic1 = {}

for i in range(read()):
    dic1[i+1] = set

for j in range(int(read)):
    a, b = map(int, read().split())
    dic1[a].add(b)
    dic1[b].add(a)

def dfs(start, dict1):
    for i in dict1[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dict1)

def bfs(start):
    queue = [start]
    while queue:
        for i in dic1[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

visited =[]
dfs(1)
# bfs(1)
print(len(visited-1))


