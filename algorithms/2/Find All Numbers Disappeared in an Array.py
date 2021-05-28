class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = dict()
        for ele in s:
            dict1[ele] = dict1.get(ele, 0) + 1
        
        for i, ch in enumerate(s):
            if(dict1[ch]==1):
                return i
            else:
                continue
        return -1