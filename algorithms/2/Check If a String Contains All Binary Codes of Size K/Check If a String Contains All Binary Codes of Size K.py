class Solution:
    def hasAllCodes1(self, s: str, k: int) -> bool:
        for ele in range(0, 2**(k)):
            temp = bin(ele).replace('0b', '').zfill(k)
            if s.find(temp) < 0:
                return False
        return True

    def hasAllCodes(self, s: str, k: int) -> bool:
        hash = set()
        for i in range(len(s)-k+1):
            hash.add(s[i:+k])

        return len(hash) == 2**k
