class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for ele1 in words:
            temp_set = set(ele1)
            
            for ele2 in temp_set:
                if allowed.find(ele2) == -1:
                    count+=1
                    break
        return len(words) - count

    def countConsistentStrings2(self, allowed: str, words: List[str]) -> int:
        return sum(not set(w) - set(allowed) for w in words)

    def countConsistentStrings3(self, allowed: str, words: List[str]) -> int:
        res = len(words)
        m_set = set(allowed)
        
        for ele1 in words:
            for ele2 in ele1:
                if ele2 not in m_set:
                    res-=1
                    break
        return res
        