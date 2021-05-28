data = [[] for _ in range(20010)]
dist = [-1]*20010

def bfs():
    max_value = 0
    q=[[1, 0]]
    dist[1] = 0

    while q:
        x, value = q.pop(0);

        for nx in data[x]:
            if dist[nx] == -1:
                dist[nx] = value+1
                q.append([nx, value+1])
                max_value = max(max_value, value+1)

    return max_value

def solution(n, edge):
    answer = 0

    for ele1, ele2, in edge:
        data[ele1].append(ele1)
        data[ele2].append(ele2)

    value = bfs()

    for i in range(2, n+1):
        if dist[i] == value:
            answer += 1

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
