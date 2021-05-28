from bisect import bisect_right
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        ans, A = [], sorted(A)
        for num in B:
            val = bisect_right(A, num)
            ans.append(A.pop(0) if val == len(A) else A.pop(val))
        return ans
