from collections import deque
from heapq import heapify
import heapq

def solution(priorities: list, location: list) -> int:
    answer = 0

    a = [[value, index] for index, value in enumerate(priorities)]
    
    print(a)
    heapify(a)
    print(a)


    while d:
        item = d.popleft()

        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer

def solution(priorities: list, location: list) -> int:
    answer = 0
    q = [[value, index] for index, value in enumerate(priorities)]
    pq = heapify(priorities[::])

    while pq:
        val, idx = q.pop(0)
        
        if heapq.nlargest(1) == val:
            heapq.heappop(pq)
            answer +=1

            if idx == location:
                break
    return answer
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
