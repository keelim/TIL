from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([ele in jewels for ele in stones])

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict1 = Counter(stones)
        cnt = 0
        for ele in jewels:
            cnt+=dict1[ele]        
        return cnt