from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heaps = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(heaps, (-freqs[f], f))

        result = []
        # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            result.append(heapq.heappop(heaps)[1])

        return result
