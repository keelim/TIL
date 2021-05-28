import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        min_heap = []
        for ele1, ele2 in people:
            heapq.heappush(min_heap, (-ele1, ele2))
        result =[]

        while min_heap:
            ele1, ele2 = heapq.heappop(min_heap)
            result.insert(ele2, (-ele1, ele2))
        return result

