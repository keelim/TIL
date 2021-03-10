from collections import defaultdict


def bfs(start: int, distances: list, data: dict):

    q = [start]
    visited = set([start])

    while q:
        x = q.pop(0)
        for nx in data[x]:
            if nx not in visited:
                visited.add(nx)
                q.append(nx)
                distances[nx] = distances[x] + 1


def solution(n:int, edge:list):
    # 그래프 만들기
    data = defaultdict(list)

    for ele1, ele2 in edge:
        data[ele1].append(ele2)
        data[ele2].append(ele1)

    # bfs 탐색 (최단 거리를 구해야 하므로.)
    distances = [0]*(n+1)
    bfs(1, distances, data)

    max_distance = max(distances)

    return distances.count(max_distance)
